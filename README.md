# igstats

See who doesn't follow you back on Instagram, without giving anyone your password.

igstats reads the data export Instagram already lets you download and returns
three lists: people you follow who don't follow you back, followers you don't
follow back, and mutuals, plus follow ratios and 30-day activity. Live at
[igstats.rone.dev](https://igstats.rone.dev).

- **No login.** It never touches your Instagram account.
- **Nothing stored.** Uploads are parsed in memory and discarded when the
  response is sent. There are no database models. See [/privacy](https://igstats.rone.dev/privacy/).
- **Three ways in.** Upload the export ZIP, upload the two JSON files, or paste the JSON.
- **Works with the list.** Search, sort, copy usernames, or export any list as CSV.
- **Seven languages.** English, Bahasa Indonesia, 中文, Español, 日本語, Português, Français.
- **Light and dark**, responsive down to 360 px, prints cleanly.

## Get your data from Instagram

1. Instagram > profile > menu > **Accounts Center**.
2. **Your information and permissions** > **Download your information**.
3. **Download or transfer information** > pick your account > **Some of your information**.
4. Under **Connections**, tick **Followers and following**.
5. **Download to device**, date range **All time**, format **JSON**, then **Create files**.
6. When Instagram emails you, download the ZIP and drop it into igstats.

The ZIP contains `connections/followers_and_following/following.json` and
`followers_1.json`; igstats finds them wherever they sit in the archive.

## Run it locally

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+. Node is only needed
if you change styles.

```bash
git clone https://github.com/ridwaanhall/instagram-following-followers.git
cd instagram-following-followers
uv sync
echo "SECRET_KEY=dev-only-change-me" > .env
DEBUG=True uv run python manage.py runserver
```

Open http://localhost:8000.

### Styles

The UI is Tailwind CSS v4, compiled into the committed `staticfiles/css/global.css`.
Fonts are self-hosted from `@fontsource-variable` packages.

```bash
npm install
npm run build   # fonts + minified CSS
npm run watch   # rebuild CSS on change
```

### Tests

```bash
SECRET_KEY=test uv run python manage.py test
```

## Project layout

| Path | What |
| --- | --- |
| `analytics/analysis.py` | Pure parsing and analysis of the export (no Django) |
| `analytics/views.py` | Page views and the three input methods |
| `analytics/data/*.py` | All interface copy, per language |
| `analytics/templates/`, `templates/` | Django templates; shared partials in `templates/partials/` |
| `assets/css/app.css` | Design tokens and components (source for `global.css`) |
| `staticfiles/js/app.js` | Theme, menu, tabs, dropzones, results tools |
| `python_scripts/instagram_analytics.py` | Stand-alone CLI version, no Django |
| `docs/DESIGN.md` | Design brief, palette, type, components |

## Command-line script

`python_scripts/instagram_analytics.py` prints the same analysis in a terminal.
Put `following.json` and `followers_1.json` next to it and run:

```bash
cd python_scripts
python instagram_analytics.py
```

## Deploy

Deployed on Vercel with `vercel.json`. Dependencies come from `pyproject.toml`
and `uv.lock`. Set `SECRET_KEY` in the project environment; leave `DEBUG` unset.

## License

[MIT](LICENSE)
