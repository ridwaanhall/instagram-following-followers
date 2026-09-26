# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this is

igstats: a Django 6 app that reads a user's own Instagram data export (ZIP,
two JSON files, or pasted JSON) and shows who doesn't follow back, who they
don't follow back, and mutuals. Deployed on Vercel at igstats.rone.dev.

## Commands

```bash
uv sync                                            # install Python deps (pyproject.toml + uv.lock)
DEBUG=True uv run python manage.py runserver       # dev server on :8000 (needs SECRET_KEY in .env)
SECRET_KEY=test uv run python manage.py test       # test suite
npm install && npm run build                       # rebuild CSS + fonts after template/CSS changes
```

`staticfiles/css/global.css` is a build artifact but is committed (Vercel does
not run the Node build). Rebuild and commit it whenever templates or
`assets/css/app.css` change, or new Tailwind classes will be missing.

## Architecture

- `analytics/analysis.py` - pure functions: username extraction, `analyze()`.
  Keep it free of Django imports. Profile URLs are parsed with `urlparse` and
  the host compared exactly; never use substring checks like `'instagram.com/' in href`.
- `analytics/views.py` - `BaseAnalyticsView.read_input()` is the only thing
  each input method implements; raise `ValueError(message)` for user errors.
- `analytics/utils.py` - language detection, content getters, the
  `inject_i18n_context` context processor (base strings + `UiData`).
- `analytics/data/*.py` - all copy, keyed by language (`en`, `id`, `zh`, `es`,
  `ja`, `pt`, `fr`). New UI strings go in `UiData.py` for **every** language.
  `PrivacyData.py` is intentionally English-only.
- `analytics/middleware.py` - picks the language from session, `?lang=`, or
  `Accept-Language`.
- Templates: `templates/base.html`, `templates/partials/` (icon, logo,
  analyzer, language menu), `analytics/templates/analytics/`.
  `method.html` is the shared layout for `/zip/`, `/upload/`, `/text/`.

## Rules

- **Privacy promises are load-bearing.** No models, no writing uploads to disk,
  no third-party scripts, fonts, or analytics. If behaviour changes,
  `analytics/data/PrivacyData.py` must change with it. Never claim processing
  happens "in the browser"; it happens in server memory.
- **Redirects**: only follow user-supplied URLs after
  `url_has_allowed_host_and_scheme` (see `safe_next_url`).
- **Icons are inline SVG** via `{% include "partials/icon.html" with name="..." %}`.
  No emoji, no arrow characters in copy or templates.
- **Design system**: read `docs/DESIGN.md` first and run its anti-slop
  checklist. One background, no cards or shadows, whitespace and 1 px
  hairlines (`rows`, `section`, `border-rule`) to separate content. Use the
  tokens and classes in `assets/css/app.css` (`display`, `h2`, `h3`, `lede`,
  `kicker`, `btn`, `btn-accent`, `btn-line`, `tabs`/`tab`, `field`, `drop`).
  Support light and dark, 360 px width, visible focus states.
- Do not name a class after a Tailwind utility (e.g. `overline`, `container`);
  Tailwind will merge its own rule into it.
- Floats rendered into CSS need `|unlocalize` (some languages use a decimal comma).
- Keep `python_scripts/instagram_analytics.py` stand-alone (stdlib only).
- Add or update tests in `analytics/tests.py` for behaviour changes.
