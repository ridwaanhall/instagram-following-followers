# igstats design brief

This is the brief the interface is built against. Read it before touching a
template or `assets/css/app.css`.

## The prompt

> Redesign igstats, a free Django tool that reads a person's own Instagram data
> export and tells them who doesn't follow them back, who they don't follow
> back, and who is mutual. The visitor arrives with one job: get the list. The
> interface should feel like a precise, trustworthy instrument: calm paper
> surfaces, ink-black type, one warm signal colour, numbers set in a monospace.
> No purple-to-pink gradients, no glassmorphism, no bouncing icons, no emoji,
> no arrow characters: every glyph is an inline SVG. Put the analyzer in the
> hero so a returning visitor can drop a ZIP without scrolling. Turn the results
> page into a working tool: stat row, ratios, and one tabbed list with search,
> sort, copy and CSV export. Every page works at 360 px, has visible focus
> states, supports light and dark, and prints cleanly.

## Principles

1. **The tool is the page.** The analyzer (ZIP / JSON files / paste) is one
   component with three tabs. It sits in the home hero and on each method page;
   each tab posts to its own endpoint, so the backend is unchanged.
2. **Honest copy.** Uploads are processed on the server in memory and never
   stored (see `/privacy/`). Never claim "processed in your browser".
3. **One accent, three semantic colours.** Colour carries meaning in results
   only: signal = don't follow back, sea = mutual, ink-blue = fans.
4. **Quiet motion.** 150 ms colour/transform transitions; respects
   `prefers-reduced-motion`.

## Tokens

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `paper` | `#F6F4EF` | `#12110F` | page background |
| `surface` | `#FFFFFF` | `#1B1A17` | cards, inputs |
| `sunken` | `#EFECE5` | `#0D0C0B` | wells, table heads |
| `line` | `#E2DED4` | `#2C2A26` | borders |
| `ink` | `#16140F` | `#F2EFE8` | primary text |
| `muted` | `#6B665C` | `#A39E93` | secondary text |
| `signal` | `#E0482B` | `#FF6A4D` | brand accent, "don't follow back" |
| `sea` | `#127A5B` | `#3CC194` | mutual, success |
| `azure` | `#2F54D6` | `#7C95FF` | fans, info |

Radius: 10 px controls, 16 px cards. Shadows: one soft level only.

## Type

- Display: **Bricolage Grotesque** (variable, self-hosted) for headings.
- Text: **Hanken Grotesk** (variable, self-hosted) for body and UI.
- Numbers and usernames: **JetBrains Mono** (variable, self-hosted).
- CJK falls back to the system stack. No third-party font host (the privacy
  notice promises none).

Scale: 12 / 14 / 16 / 18 / 22 / 28 / 40 / 56. Headings use tight tracking
(-0.02em), body 1.6 line-height.

## Components

Buttons (`btn-primary`, `btn-secondary`, `btn-ghost`), inputs and dropzones,
tabs (`role=tablist`, arrow-key navigation), dropdown (language menu, built on
`<details>`), accordion (FAQ, `<details>`), stat tiles, alert/toast for Django
messages, list rows with avatar initial, empty states, stepper (guide), sticky
table of contents (privacy). All are defined in `assets/css/app.css` under
`@layer components`.

## Pages

| URL | Purpose |
| --- | --- |
| `/` | Hero + analyzer, how it works, what you get, FAQ |
| `/zip/`, `/upload/`, `/text/` | Analyzer with that method's tab open + method-specific help |
| results (POST) | Dashboard: stats, ratios, 30-day activity, tabbed lists |
| `/tutorial/` | Export guide as a stepper with notes sidebar |
| `/privacy/` | Long-form notice with sticky contents |
| 404 / 500 | Short, useful, on-brand |
