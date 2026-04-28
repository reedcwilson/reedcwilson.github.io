# reedcwilson.github.io

This repository publishes Reed Wilson's Hugo site using the Blowfish theme and GitHub Pages.
Deployment runs from the `main` branch through GitHub Pages Actions.

## Local development

```bash
git submodule update --init --recursive
hugo server
```

## Production build

```bash
hugo --gc --minify
```
