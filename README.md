# Scope Pitch

Static pitch site for Scope.

## Live site

- GitHub Pages fallback: https://nickperillo.github.io/augmentl-scope-pitch/
- Branded URL: https://pitch.augmentl.com
- Legacy Netlify URL: https://augmentl-scope-pitch.netlify.app

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

The repo now auto-publishes to GitHub Pages on every push to `main`.

- GitHub Pages URL: `https://nickperillo.github.io/augmentl-scope-pitch/`

The branded Netlify-hosted domain is currently blocked by the Netlify account state:

- `Account credit usage exceeded - new deploys are blocked until credits are added`

So `pitch.augmentl.com` can be restored later, but the working public fallback is GitHub Pages for now.
