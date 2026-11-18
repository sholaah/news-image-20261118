"""Build entry.png for make.fun news-image-20261118.

The base illustration (assets/) was generated in-session as an editorial
world-map scene of 18 November 2026's top stories:
  - APEC / Quad summit diplomacy in Asia (Trump, Xi, Modi in Manila & Shenzhen)
  - Ukraine's strike on the Crimean Bridge, second day running
  - Iranian drones vs the US radar station in Bahrain, tanker in the strait
  - Wall Street's 1,000-point Dow plunge ahead of Nvidia earnings
  - NASA's Voyager 1 closing in on one light-day from Earth
  - Cyclone Akvan spinning over the Bay of Bengal
This script frames it as a front page: masthead on top, headline strips
below, and exports a PNG of at most 1024x1024 and 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "media-generation-world-18nov-0-3511170e-409b-411a-b1c8-dd35e5807fbe.png")
OUT = os.path.join(HERE, "entry.png")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
NAVY = (9, 24, 43)
GOLD = (242, 193, 78)
WHITE = (245, 247, 250)

W, H = 1024, 1024
TOP_H, BOT_H = 98, 146


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def centered(draw, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((W - (box[2] - box[0])) // 2, y), text, font=fnt, fill=fill)


def main():
    art = Image.open(SRC).convert("RGB")
    art = art.resize((W, H - TOP_H - BOT_H), Image.LANCZOS)
    page = Image.new("RGB", (W, H), NAVY)
    page.paste(art, (0, TOP_H))
    draw = ImageDraw.Draw(page)

    centered(draw, 12, "THE WORLD TODAY", font("DejaVuSans-Bold.ttf", 46), WHITE)
    centered(draw, 66, "WEDNESDAY · 18 NOVEMBER 2026", font("DejaVuSans-Bold.ttf", 22), GOLD)

    headlines = [
        ((242, 193, 78), "APEC SUMMIT: TRUMP, XI & MODI CONVERGE ON ASIA"),
        ((231, 76, 60), "UKRAINE STRIKES CRIMEAN BRIDGE FOR A SECOND DAY"),
        ((230, 126, 34), "IRANIAN DRONES HIT U.S. RADAR IN BAHRAIN"),
        ((93, 173, 226), "DOW PLUNGES 1,000 POINTS · VOYAGER 1 NEARS A LIGHT-DAY"),
    ]
    fnt = font("DejaVuSans-Bold.ttf", 24)
    y = H - BOT_H + 10
    for color, text in headlines:
        draw.rectangle([28, y + 4, 44, y + 20], fill=color)
        draw.text((58, y), text, font=fnt, fill=WHITE)
        y += 34

    page.save(OUT, optimize=True)
    if os.path.getsize(OUT) > 1024 * 1024:
        page.quantize(colors=256, method=Image.MEDIANCUT).save(OUT, optimize=True)
    print("entry.png:", page.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
