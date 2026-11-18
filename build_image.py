"""Build entry.png for make.fun news-image-20261118.

The base illustration (assets/) was generated in-session as an editorial
world-map scene of 18 November 2026's top stories, then extended with a
cyber-outage vignette and a Bitcoin vignette:
  - APEC / Quad summit diplomacy in Asia (Trump, Xi, Modi in Manila & Shenzhen)
  - Ukraine's strike on the Crimean Bridge, second day running
  - Iranian drones vs the US radar station in Bahrain, tanker in the strait
  - Wall Street's 1,000-point Dow plunge ahead of Nvidia earnings
  - NASA's Voyager 1 closing in on one light-day from Earth
  - Cyclone Akvan spinning over the Bay of Bengal
  - The outage wave (upper left): the NSA's classified network down,
    Apple's services disrupted by an internal update, supermarket
    freezers hacked across Europe, and Equinor confirming the week's
    only acknowledged cyberattack — officials see no coordinated attack
  - Crypto (bottom left): a Bitcoin coin sinking in heavy seas under a
    plunging chart — about half of all bitcoin is now held at a loss
    after the 50% retreat from October 2025's high
This script frames it as a magazine cover in the style of The
Economist's "The World Ahead": a small red masthead box and a large
date title above a full-bleed icon collage, at most 1024x1024, 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "media-generation-world-18nov-economist-0-b39267c1-0dd0-4229-bda6-18d8017ce858.png")
OUT = os.path.join(HERE, "entry.png")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
NAVY = (9, 24, 43)
GOLD = (242, 193, 78)
WHITE = (245, 247, 250)

W, H = 1024, 1024
TOP_H, BOT_H = 190, 0


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def centered(draw, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((W - (box[2] - box[0])) // 2, y), text, font=fnt, fill=fill)


def main():
    art = Image.open(SRC).convert("RGB")
    art = art.resize((W, H - TOP_H - BOT_H), Image.LANCZOS)
    page = Image.new("RGB", (W, H), (247, 244, 235))
    page.paste(art, (0, TOP_H))
    draw = ImageDraw.Draw(page)

    draw.rectangle([312, 14, 712, 58], fill=(227, 18, 11))
    centered(draw, 22, "THE WORLD TODAY", font("DejaVuSans-Bold.ttf", 30), WHITE)
    centered(draw, 72, "18 NOVEMBER 2026", font("DejaVuSans-Bold.ttf", 84), (17, 17, 17))
    centered(draw, 164, "WEDNESDAY · THE DAY IN ONE IMAGE", font("DejaVuSans-Bold.ttf", 20), (90, 90, 90))

    headlines = [
        ((242, 193, 78), "APEC SUMMIT: TRUMP, XI & MODI CONVERGE ON ASIA"),
        ((231, 76, 60), "UKRAINE STRIKES CRIMEAN BRIDGE FOR A SECOND DAY"),
        ((230, 126, 34), "IRANIAN DRONES HIT U.S. RADAR IN BAHRAIN"),
        ((93, 173, 226), "DOW PLUNGES 1,000 POINTS · VOYAGER 1 NEARS A LIGHT-DAY"),
        ((46, 204, 113), "CYBER: NSA NET DOWN · APPLE OUTAGE · EQUINOR HACKED"),
        ((175, 122, 197), "CRYPTO: HALF OF ALL BITCOIN NOW HELD AT A LOSS"),
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
