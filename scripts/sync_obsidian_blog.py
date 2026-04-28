#!/usr/bin/env python3
"""Sync Obsidian blog notes into Hugo page bundles.

The script mirrors Markdown notes from an Obsidian vault folder into Hugo's
`content/` directory. Standalone notes become leaf bundles (`index.md`) so
local assets can live beside the page, and `_index.md` files remain section
indexes. Obsidian image embeds that point at `_resources` assets are rewritten
to normal Markdown image links and the assets are copied into the destination
bundle.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

SYNC_MARKER = ".obsidian-sync.json"
IGNORED_DIRS = {".obsidian", ".trash", ".git", "__pycache__"}
IMAGE_EXTENSIONS = {
    ".apng",
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".webp",
}
WIKI_EMBED_PATTERN = re.compile(r"!\[\[([^\]]+)\]\]")
MARKDOWN_IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


class SyncError(RuntimeError):
    """Raised when the sync cannot proceed safely."""


@dataclass(frozen=True)
class Note:
    """Represents a source note and its destination inside Hugo content."""

    source_path: Path
    relative_path: Path
    destination_dir: Path
    destination_markdown: Path
    is_section_index: bool


@dataclass
class Marker:
    """Tracks files previously managed for a destination bundle."""

    source: str
    kind: str
    files: list[str]


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""

    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description=(
            "Sync Markdown notes from ~/Notes/Blog into Hugo content page "
            "bundles and optionally publish the result."
        )
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path.home() / "Notes" / "Blog",
        help="Obsidian source folder. Defaults to ~/Notes/Blog.",
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=repo_root / "content",
        help="Hugo content directory. Defaults to this repo's content/.",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Build, commit, and push the synced content after a successful sync.",
    )
    parser.add_argument(
        "--message",
        default="Sync Obsidian blog content",
        help="Git commit message to use with --publish.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each synchronized note and copied asset.",
    )
    return parser.parse_args()


def ensure_directory(path: Path, description: str) -> Path:
    """Return a normalized directory path or raise a helpful error."""

    resolved = path.expanduser().resolve()
    if not resolved.exists():
        raise SyncError(f"{description} does not exist: {resolved}")
    if not resolved.is_dir():
        raise SyncError(f"{description} is not a directory: {resolved}")
    return resolved


def discover_vault_root(source_root: Path) -> Path:
    """Return the nearest Obsidian vault root that contains source_root."""

    for candidate in [source_root, *source_root.parents]:
        if (candidate / ".obsidian").is_dir():
            return candidate
    return source_root


def is_ignored(path: Path) -> bool:
    """Return whether a path should be skipped during note discovery."""

    return any(part in IGNORED_DIRS or part == "_resources" for part in path.parts)


def discover_notes(source_root: Path, destination_root: Path) -> list[Note]:
    """Discover all Markdown files that should be synchronized."""

    notes: list[Note] = []
    for source_path in sorted(source_root.rglob("*.md")):
        relative_path = source_path.relative_to(source_root)
        if is_ignored(relative_path):
            continue

        is_section_index = relative_path.name == "_index.md"
        if is_section_index:
            destination_dir = destination_root / relative_path.parent
            destination_markdown = destination_dir / "_index.md"
        else:
            destination_dir = destination_root / relative_path.with_suffix("")
            destination_markdown = destination_dir / "index.md"

        notes.append(
            Note(
                source_path=source_path,
                relative_path=relative_path,
                destination_dir=destination_dir,
                destination_markdown=destination_markdown,
                is_section_index=is_section_index,
            )
        )

    return notes


def build_resource_index(asset_root: Path) -> dict[str, list[Path]]:
    """Index files inside `_resources` folders by basename."""

    index: dict[str, list[Path]] = {}
    for resource_dir in asset_root.rglob("_resources"):
        if not resource_dir.is_dir():
            continue
        for file_path in resource_dir.rglob("*"):
            if not file_path.is_file():
                continue
            index.setdefault(file_path.name, []).append(file_path)
    return index


def load_marker(destination_dir: Path) -> Marker | None:
    """Load bundle marker metadata if present."""

    marker_path = destination_dir / SYNC_MARKER
    if not marker_path.exists():
        return None

    try:
        data = json.loads(marker_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SyncError(f"Invalid sync marker at {marker_path}: {exc}") from exc

    return Marker(
        source=data["source"],
        kind=data["kind"],
        files=list(data.get("files", [])),
    )


def write_marker(destination_dir: Path, note: Note, files: list[str]) -> None:
    """Persist marker metadata for a synchronized note."""

    marker_path = destination_dir / SYNC_MARKER
    payload = {
        "source": note.relative_path.as_posix(),
        "kind": "section" if note.is_section_index else "leaf",
        "files": sorted(files),
    }
    marker_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cleanup_marker_files(destination_dir: Path, marker: Marker) -> list[Path]:
    """Remove files previously owned by a marker."""

    removed_paths: list[Path] = []
    for relative_path in marker.files:
        owned_path = destination_dir / relative_path
        if not owned_path.exists():
            continue
        if owned_path.is_dir():
            shutil.rmtree(owned_path)
        else:
            owned_path.unlink()
        removed_paths.append(owned_path)
    return removed_paths


def validate_destination(note: Note, marker: Marker | None) -> None:
    """Refuse to overwrite unmanaged content."""

    if marker and marker.source != note.relative_path.as_posix():
        raise SyncError(
            f"{note.destination_dir} is already managed for {marker.source}, "
            f"not {note.relative_path.as_posix()}"
        )

    if note.is_section_index:
        if note.destination_markdown.exists() and marker is None:
            raise SyncError(
                f"Refusing to overwrite unmanaged section index: {note.destination_markdown}"
            )
        return

    if not note.destination_dir.exists():
        return

    entries = [entry for entry in note.destination_dir.iterdir() if entry.name != SYNC_MARKER]
    if not entries:
        return

    if marker is None:
        raise SyncError(
            f"Refusing to overwrite unmanaged bundle directory: {note.destination_dir}"
        )


def normalize_target(raw_target: str) -> str:
    """Normalize an Obsidian or Markdown target before path resolution."""

    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    target = target.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    return unquote(target)


def is_external(target: str) -> bool:
    """Return whether a link target points outside the local vault."""

    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:", "tel:"))


def is_image(path: Path) -> bool:
    """Return whether a path looks like an image asset."""

    return path.suffix.lower() in IMAGE_EXTENSIONS


def ancestor_chain(start: Path, stop: Path) -> list[Path]:
    """Return the directory chain from start up through stop, inclusive."""

    if start != stop and stop not in start.parents:
        raise SyncError(f"{start} is not inside {stop}")

    current = start
    chain = [current]
    while current != stop:
        current = current.parent
        chain.append(current)
    return chain


def unique_paths(paths: list[Path]) -> list[Path]:
    """De-duplicate paths while preserving order."""

    seen: set[Path] = set()
    unique: list[Path] = []
    for path in paths:
        if path in seen:
            continue
        seen.add(path)
        unique.append(path)
    return unique


def resolve_asset(
    note: Note,
    target: str,
    asset_root: Path,
    resource_index: dict[str, list[Path]],
) -> Path:
    """Resolve an asset reference relative to a note."""

    normalized = normalize_target(target)
    if not normalized:
        raise SyncError(f"Empty asset reference in {note.source_path}")
    if is_external(normalized):
        raise SyncError(f"Expected local asset reference, got external URL: {normalized}")

    target_path = Path(normalized)
    candidates: list[Path] = [note.source_path.parent / target_path]

    for ancestor in ancestor_chain(note.source_path.parent, asset_root):
        candidates.append(ancestor / "_resources" / target_path)
        candidates.append(ancestor / "_resources" / target_path.name)

    candidates.append(asset_root / target_path)
    candidates.append(asset_root / "_resources" / target_path)
    candidates.append(asset_root / "_resources" / target_path.name)

    for candidate in unique_paths(candidates):
        if candidate.is_file():
            return candidate

    basename_matches = resource_index.get(target_path.name, [])
    if len(basename_matches) == 1:
        return basename_matches[0]
    if len(basename_matches) > 1:
        matches = ", ".join(str(match.relative_to(asset_root)) for match in basename_matches)
        raise SyncError(
            f"Ambiguous asset reference {target!r} in {note.source_path}: {matches}"
        )

    raise SyncError(f"Could not resolve asset {target!r} in {note.source_path}")


def markdown_target(path_name: str) -> str:
    """Render a Markdown-safe target."""

    if any(character in path_name for character in (" ", "(", ")")):
        return f"<{path_name}>"
    return path_name


def obsidian_alias_to_alt(alias: str) -> str:
    """Convert an Obsidian alias to Markdown alt text when appropriate."""

    stripped = alias.strip()
    if not stripped:
        return ""

    normalized = stripped.lower().replace("x", "")
    if normalized.isdigit():
        return ""

    return stripped


def transform_content(
    note: Note,
    asset_root: Path,
    resource_index: dict[str, list[Path]],
) -> tuple[str, dict[str, Path]]:
    """Rewrite image references and collect bundle assets for a note."""

    text = note.source_path.read_text(encoding="utf-8")
    copied_assets: dict[str, Path] = {}

    def register_asset(raw_target: str) -> str:
        asset_path = resolve_asset(note, raw_target, asset_root, resource_index)
        destination_name = asset_path.name

        existing = copied_assets.get(destination_name)
        if existing is not None and existing != asset_path:
            raise SyncError(
                f"{note.source_path} references multiple assets named {destination_name!r}; "
                "rename one of them in Obsidian so the Hugo bundle can stay unambiguous."
            )

        copied_assets[destination_name] = asset_path
        return destination_name

    def replace_wiki_embed(match: re.Match[str]) -> str:
        inner = match.group(1)
        target, _, alias = inner.partition("|")
        normalized_target = normalize_target(target)
        if is_external(normalized_target):
            return match.group(0)
        if Path(normalized_target).suffix.lower() == ".md":
            return match.group(0)
        if not Path(normalized_target).suffix:
            return match.group(0)

        destination_name = register_asset(target)
        escaped_target = markdown_target(destination_name)
        alt_text = obsidian_alias_to_alt(alias)
        if is_image(Path(destination_name)):
            return f"![{alt_text}]({escaped_target})"

        link_text = alt_text or destination_name
        return f"[{link_text}]({escaped_target})"

    def replace_markdown_image(match: re.Match[str]) -> str:
        alt_text = match.group(1)
        target = match.group(2).strip()
        normalized_target = normalize_target(target)
        if not normalized_target or is_external(normalized_target):
            return match.group(0)

        destination_name = register_asset(target)
        return f"![{alt_text}]({markdown_target(destination_name)})"

    transformed = WIKI_EMBED_PATTERN.sub(replace_wiki_embed, text)
    transformed = MARKDOWN_IMAGE_PATTERN.sub(replace_markdown_image, transformed)
    return transformed, copied_assets


def remove_empty_directories(start: Path, stop: Path) -> list[Path]:
    """Remove empty directories between start and stop, exclusive of stop."""

    removed_paths: list[Path] = []
    current = start
    while current != stop and current.exists():
        try:
            current.rmdir()
        except OSError:
            break
        removed_paths.append(current)
        current = current.parent
    return removed_paths


def sync_note(
    note: Note,
    asset_root: Path,
    destination_root: Path,
    resource_index: dict[str, list[Path]],
    verbose: bool,
) -> list[Path]:
    """Synchronize a single note and return paths that changed."""

    marker = load_marker(note.destination_dir)
    validate_destination(note, marker)

    note.destination_dir.mkdir(parents=True, exist_ok=True)

    touched_paths = cleanup_marker_files(note.destination_dir, marker) if marker else []
    transformed_text, copied_assets = transform_content(note, asset_root, resource_index)

    note.destination_markdown.write_text(transformed_text, encoding="utf-8")
    touched_paths.append(note.destination_markdown)

    managed_files = [note.destination_markdown.name]
    for destination_name, asset_path in sorted(copied_assets.items()):
        destination_path = note.destination_dir / destination_name
        shutil.copy2(asset_path, destination_path)
        touched_paths.append(destination_path)
        managed_files.append(destination_name)
        if verbose:
            print(
                f"  asset {asset_path.relative_to(asset_root)} -> "
                f"{destination_path.relative_to(destination_root)}"
            )

    write_marker(note.destination_dir, note, managed_files)
    touched_paths.append(note.destination_dir / SYNC_MARKER)

    if verbose:
        print(
            f"synced {note.relative_path.as_posix()} -> "
            f"{note.destination_markdown.relative_to(destination_root)}"
        )

    return touched_paths


def prune_deleted_notes(destination_root: Path, live_notes: dict[str, Note]) -> list[Path]:
    """Remove previously managed notes that no longer exist in Obsidian."""

    touched_paths: list[Path] = []
    marker_paths = [path for path in destination_root.rglob(SYNC_MARKER)]
    for marker_path in marker_paths:
        if not marker_path.exists():
            continue
        destination_dir = marker_path.parent
        marker = load_marker(destination_dir)
        if marker is None or marker.source in live_notes:
            continue

        touched_paths.extend(cleanup_marker_files(destination_dir, marker))
        if marker_path.exists():
            marker_path.unlink()
            touched_paths.append(marker_path)

        if marker.kind == "leaf":
            remove_target = destination_dir
            shutil.rmtree(remove_target, ignore_errors=True)
            touched_paths.append(remove_target)
            prune_start = remove_target.parent
        else:
            prune_start = destination_dir

        touched_paths.extend(remove_empty_directories(prune_start, destination_root))

    return touched_paths


def git_has_staged_changes(repo_root: Path) -> bool:
    """Return whether the git index already contains staged changes."""

    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet", "--ignore-submodules", "--"],
        cwd=repo_root,
        check=False,
    )
    return result.returncode != 0


def run_command(command: list[str], cwd: Path) -> None:
    """Run a subprocess and surface failures directly."""

    subprocess.run(command, cwd=cwd, check=True)


def publish(repo_root: Path, touched_paths: list[Path], message: str) -> None:
    """Build, commit, and push the synchronized content."""

    if git_has_staged_changes(repo_root):
        raise SyncError("Refusing to publish with pre-existing staged changes in the repo.")

    if not touched_paths:
        print("No synced content changed; skipping publish.")
        return

    run_command(["hugo", "--gc", "--minify"], cwd=repo_root)

    stage_paths = sorted(
        {
            str(path.relative_to(repo_root))
            for path in touched_paths
            if repo_root in path.parents or path == repo_root
        }
    )
    if not stage_paths:
        print("Nothing to stage after sync; skipping publish.")
        return

    run_command(["git", "add", "-A", "--", *stage_paths], cwd=repo_root)

    if subprocess.run(["git", "diff", "--cached", "--quiet", "--"], cwd=repo_root, check=False).returncode == 0:
        print("No git changes to publish after staging.")
        return

    run_command(["git", "commit", "-m", message], cwd=repo_root)
    run_command(["git", "push"], cwd=repo_root)


def main() -> int:
    """Execute the sync workflow."""

    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]

    try:
        source_root = ensure_directory(args.source, "Source folder")
        destination_root = ensure_directory(args.destination, "Destination folder")
        asset_root = discover_vault_root(source_root)

        notes = discover_notes(source_root, destination_root)
        resource_index = build_resource_index(asset_root)
        live_notes = {note.relative_path.as_posix(): note for note in notes}

        touched_paths = prune_deleted_notes(destination_root, live_notes)
        for note in notes:
            touched_paths.extend(
                sync_note(
                    note=note,
                    asset_root=asset_root,
                    destination_root=destination_root,
                    resource_index=resource_index,
                    verbose=args.verbose,
                )
            )

        print(f"Synchronized {len(notes)} note(s) from {source_root} to {destination_root}.")

        if args.publish:
            publish(repo_root=repo_root, touched_paths=touched_paths, message=args.message)
    except SyncError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"error: command failed with exit code {exc.returncode}: {' '.join(exc.cmd)}", file=sys.stderr)
        return exc.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
