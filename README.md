# Scope Pitch

Static pitch site for Scope.

## Live site

- Public URL: https://pitch.augmentl.com
- Netlify URL: https://augmentl-scope-pitch.netlify.app

## Local source

```bash
cd /Users/cypher/workspace/presentations/scope-pitch
```

## Structure

- `index.html` - main presentation
- `assets/` - screenshots, graphics, and fallback media
- `_redirects` - Netlify redirects
- `tests/` - lightweight presentation checks

## Local preview

Simple static serve:

```bash
python3 -m http.server 3202 --bind 0.0.0.0
```

Then open:

- http://localhost:3202
- or the machine-local/Tailscale host on port `3202`

## Deploy notes

The live branded site is hosted on Netlify at `pitch.augmentl.com`.

If needed, redeploy from this directory using the Netlify API workflow already used for the existing site.
