# igstats design brief (v3)

Read this before touching a template, `assets/css/app.css`, or `staticfiles/js/app.js`.

## The prompt

> Design igstats as a quiet, typographic tool, the way a Swiss designer would
> set a newspaper page: one background colour, a strict grid, whitespace as the
> main separator, 1 px hairlines only where whitespace is not enough. No cards,
> no shadows, no gradients, no glass, no rounded pill blobs, no icon-in-a-circle
> feature grids, no emoji, no arrow characters. Every icon is a thin inline SVG.
>
> Type does the work. A literary serif (Newsreader) for headlines and big
> numbers, a sturdy grotesk (Schibsted Grotesk) for everything else, a mono
> (Geist Mono) only for usernames, file names and figures in tables. Colour is
> ink on paper plus one accent, used only for the primary action and for the
> one number people come for: who does not follow them back.
>
> The visitor has one job: drop an export, read three lists. The analyzer is
> the hero. The results page reads like a printed report: a row of large
> figures separated by hairlines, a sentence of ratios, then the lists as ruled
> rows with search, sort, copy and CSV. Every page works at 360 px, in light and
> dark, with visible focus rings, and prints cleanly.

## Anti-slop checklist

Reject a change if it adds any of these:

- A bordered or shadowed box around a section or a group of text (cards).
- A background colour change to separate sections (the page is one colour).
- Gradients, blurred blobs, glows, glassmorphism, dotted backgrounds.
- Icons inside tinted circles or squares; three-column "feature" grids of them.
- Emoji or arrow glyphs in copy or markup.
- Centered paragraphs longer than one line. Text is left-aligned.
- More than one accent colour on a page outside the results data.
- Bounce, pulse or scale-on-hover animations.

Allowed boxes: form controls (inputs, the drop area, buttons), the dropdown
menu, and tables. These are controls, not decoration.

## Grid and spacing

- Container 72rem, gutter 20 px mobile / 32 px desktop.
- 12-column grid on desktop; content usually spans 7, asides 4 with 1 gap.
- Spacing scale (px): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
  Section rhythm: 96 desktop / 64 mobile, separated by a hairline rule.
- Measure: body copy max 64ch, lede max 52ch.

## Colour

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `bg` | `#FAFAF7` | `#111110` | the only background |
| `ink` | `#111110` | `#EDEDE8` | text, primary button |
| `ink-2` | `#55544F` | `#A3A29B` | secondary text |
| `ink-3` | `#8C8B84` | `#6E6D67` | captions, placeholders |
| `rule` | `#E4E3DC` | `#2A2A27` | hairlines |
| `rule-2` | `#CFCEC6` | `#3A3A36` | control borders |
| `field` | `#F2F1EC` | `#1A1A18` | inside inputs and the drop area only |
| `accent` | `#D23F1F` | `#F2643F` | primary action, "not following back" |

Results use ink for mutuals and followers; the accent is reserved for the
"not following back" figure and its tab marker.

## Type

| Role | Font | Size / leading |
| --- | --- | --- |
| Display | Newsreader 400, optical size on, -0.02em | 44/1.02 mobile, 72/1.0 desktop |
| H2 | Newsreader 400 | 30/1.1 mobile, 40/1.05 desktop |
| H3 | Schibsted Grotesk 600 | 17/1.35 |
| Body | Schibsted Grotesk 400 | 16/1.6 |
| Small / label | Schibsted Grotesk 500 | 13/1.4 |
| Kicker | Schibsted Grotesk 600, uppercase, +0.08em | 11/1 |
| Mono | Geist Mono 400-500 | 13-14 |
| Figures | Newsreader 400, lining + tabular nums | 40-64 |

All fonts self-hosted (the privacy notice promises no third-party hosts). CJK
falls back to system fonts with no negative tracking.

## Components

- **Header**: wordmark "igstats" in Newsreader, text nav links, language menu,
  theme toggle. Hairline under the header, same background.
- **Links in text**: ink with a 1 px underline in `rule-2`, accent on hover.
- **Buttons**: `btn` (solid ink, 36 px tall, 8 px radius), `btn-accent`,
  `btn-line` (1 px border), `btn-text` (no border). Icons 16 px, 1.5 stroke.
- **Tabs**: text tabs with a 2 px underline on the selected one; sit on a hairline.
- **Drop area**: dashed `rule-2` border, `field` fill, 12 px radius; turns
  solid ink when a file is chosen.
- **Input / textarea / select**: `field` fill, `rule-2` border, ink border on focus.
- **Rows**: hairline-separated list rows; no avatars.
- **Figures**: big serif number over a small label, separated by vertical hairlines.
- **Accordion**: question rows on hairlines with a plus that turns into a minus.
- **Dropdown**: the one floating surface: `bg`, `rule` border, soft shadow.
- **Alert**: accent left rule and text, no fill.

## Page map

| URL | Layout |
| --- | --- |
| `/` | Display headline + lede (7 cols) beside the analyzer (5 cols). Then "What you get": three ruled rows with a serif number, title and sentence. Then "How it works": four numbered columns on a top rule. Then FAQ as a ruled accordion. Footer. |
| `/zip/`, `/upload/`, `/text/` | Title + lede, then analyzer (7 cols) and the method's notes as plain text (4 cols). Tabs navigate between the three URLs. |
| results | Report title, actions on the right. Figure row (5 figures). Ratio sentence line and 30-day line. Ruled tabs, toolbar, ruled rows. |
| `/tutorial/` | Numbered steps as a ruled ordered list (7 cols), notes/files/tips as plain text sections (4 cols), then links to the three methods as a ruled list. |
| `/privacy/`, `/terms/` | Shared `legal.html`: contents column (3 cols) and the document (8 cols), numbered H2s, table with hairlines. |
| 404 / 500 | Large serif code, one sentence, two buttons, left-aligned. |

## Motion

One easing (`cubic-bezier(0.2, 0.7, 0.2, 1)`), transform and opacity only.

- Page load: title, lede and first block rise 14 px in sequence (70 ms steps).
- Scroll: sections fade up once (`data-reveal`), their rows stagger 60 ms.
- Tabs fade in 240 ms; menus pop from 98% scale; the accordion animates height
  where `interpolate-size` is supported.
- Results figures count up; ratio lines grow from the left.
- Buttons: 1 px press, arrow icons nudge 2 px on hover.
- Theme switch: one View Transition cross-fade with every element transition
  suspended, so no part of the page lags behind.
- Page to page: cross-document view transition fade.
- Everything stops under `prefers-reduced-motion`.

## Controls

Every button, input and select is 36 px tall (`h-9`), 13.5 px text.
