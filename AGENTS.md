# Reed Wilson's Hugo Blog — Agent Guide

This repository publishes Reed Wilson's personal blog using [Hugo](https://gohugo.io) and the [Blowfish](https://blowfish.pages.dev/) theme. Deployment runs from `main` via GitHub Pages Actions.

## Content Workflow

All article content lives in **Obsidian** at `~/Notes/Blog/`. The directory structure maps to Hugo sections:

| Obsidian path | Hugo section | URL prefix |
|---|---|---|
| `~/Notes/Blog/posts/*.md` | `content/posts/` | `/posts/` |
| `~/Notes/Blog/ideas/*.md` | `content/ideas/` | `/ideas/` |
| `~/Notes/Blog/links/*.md` | `content/links/` | `/links/` |

### Publishing a new article

1. **Write the note** in Obsidian at `~/Notes/Blog/posts/<title>.md` (or move it there from `ideas/`).
2. **Ensure front-matter has `draft: false`** — articles with `draft: true` are excluded from production builds.
3. **Run the sync script to build and push:**

   ```bash
   python3 scripts/sync_obsidian_blog.py --publish
   ```

   This will:
   - Mirror the note into `content/` as a Hugo page bundle (`index.md`)
   - Copy any local assets (images, etc.) from Obsidian's `_resources` folders
   - Run `hugo --gc --minify` to rebuild the site
   - Commit and push to `origin/main`, triggering GitHub Pages deployment

### Syncing without publishing

To only sync content (no build/commit/push):

```bash
python3 scripts/sync_obsidian_blog.py
```

### Moving an article between sections

Move the `.md` file in Obsidian, then re-run the sync script. The script will rename the Hugo bundle and clean up the old directory automatically.

## Local Development

```bash
git submodule update --init --recursive
hugo server -D   # includes drafts for local preview
```

Or use the helper script:

```bash
./scripts/serve.sh
```

## Production Build

```bash
hugo --gc --minify
```

The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs this automatically on every push to `main`.

## Troubleshooting

- **Article not appearing after push:** Check that the note has `draft: false` in its front-matter and that it's in one of the recognized sections (`posts/`, `ideas/`, `links/`).
- **Sync errors about unmanaged bundles:** The sync script refuses to overwrite existing Hugo content that wasn't created by a previous sync. Delete the conflicting bundle directory or move the source note first.
- **Missing images:** Obsidian wiki-image embeds (`![[image.png]]`) are automatically converted to Markdown image links and assets are copied into the page bundle's `_resources` folder during sync.
