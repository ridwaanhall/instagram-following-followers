"""
Generate the favicon set and the Open Graph image.

    uv run --with pillow --with fonttools --with brotli python scripts/make-icons.py

The mark is two overlapping circles (following, followers) with the overlap
(mutuals) in the accent colour, on an ink tile. Newsreader for the OG image is
read from the self-hosted woff2 in staticfiles/font.
"""

import io
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "staticfiles"
IMAGES = STATIC / "images"

INK = (17, 17, 16)
PAPER = (250, 250, 247)
ACCENT = (210, 63, 31)
MUTED = (85, 84, 79)

# Geometry on a 64-unit grid: circles r=14 at x=25 and x=39, y=32.
SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#111110"/>
<path d="M32 20.1a14 14 0 0 1 0 23.8 14 14 0 0 1 0-23.8z" fill="#D23F1F"/>
<circle cx="25" cy="32" r="14" fill="none" stroke="#FAFAF7" stroke-width="3"/>
<circle cx="39" cy="32" r="14" fill="none" stroke="#FAFAF7" stroke-width="3"/>
</svg>
"""


def draw_mark(size, rounded=True, pad=0.0):
    """Render the mark at `size` px with 4x supersampling. `pad` shrinks the
    drawing inside a full-bleed tile (for maskable icons)."""
    s = size * 4
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    radius = int(s * 14 / 64) if rounded else 0
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=radius, fill=INK)

    scale = s / 64 * (1 - 2 * pad)
    off = s * pad

    def u(v):
        return off + v * scale

    r = 14 * scale
    w = max(1, round(3 * scale))
    # Lens: intersection of the two discs.
    lens = Image.new("L", (s, s), 0)
    a = Image.new("L", (s, s), 0)
    b = Image.new("L", (s, s), 0)
    ImageDraw.Draw(a).ellipse((u(25) - r, u(32) - r, u(25) + r, u(32) + r), fill=255)
    ImageDraw.Draw(b).ellipse((u(39) - r, u(32) - r, u(39) + r, u(32) + r), fill=255)
    lens.paste(a, mask=b)
    img.paste(Image.new("RGBA", (s, s), ACCENT), mask=lens)
    for cx in (25, 39):
        d.ellipse((u(cx) - r, u(32) - r, u(cx) + r, u(32) + r), outline=PAPER, width=w)
    return img.resize((size, size), Image.LANCZOS)


def newsreader(size):
    font = TTFont(STATIC / "font" / "newsreader-latin-opsz-normal.woff2")
    font.flavor = None
    buf = io.BytesIO()
    font.save(buf)
    buf.seek(0)
    f = ImageFont.truetype(buf, size)
    try:
        f.set_variation_by_axes([400, 48])  # wght, opsz
    except Exception:
        pass
    return f


def og_image():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), PAPER)
    d = ImageDraw.Draw(img)
    img.paste(draw_mark(72), (80, 72), draw_mark(72))
    d.text((170, 84), "igstats", font=newsreader(46), fill=INK)
    d.line((80, 186, w - 80, 186), fill=(228, 227, 220), width=2)
    title = newsreader(96)
    d.text((80, 228), "See who doesn't", font=title, fill=INK)
    d.text((80, 332), "follow you back.", font=title, fill=INK)
    small = newsreader(30)
    d.text((80, 520), "Free. No login. Nothing stored.", font=small, fill=MUTED)
    d.text((w - 80, 520), "igstats.rone.dev", font=small, fill=ACCENT, anchor="ra")
    return img


def main():
    IMAGES.mkdir(exist_ok=True)
    for old in IMAGES.glob("*"):
        old.unlink()
    (STATIC / "favicon.svg").write_text(SVG, encoding="utf-8")
    draw_mark(256).save(STATIC / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    draw_mark(180, rounded=False).save(IMAGES / "apple-touch-icon.png")
    draw_mark(192).save(IMAGES / "icon-192.png")
    draw_mark(512).save(IMAGES / "icon-512.png")
    draw_mark(512, rounded=False, pad=0.12).save(IMAGES / "icon-maskable-512.png")
    og_image().save(IMAGES / "og-image.png", optimize=True)
    for f in sorted([STATIC / "favicon.svg", STATIC / "favicon.ico", *IMAGES.glob("*")]):
        print(f.relative_to(ROOT), f.stat().st_size)


if __name__ == "__main__":
    main()
