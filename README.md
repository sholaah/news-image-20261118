# The World Today — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/sholaah/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/sholaah/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Entry for the make.fun bounty **"Sum up 18 November's world news in one image"**
(news-image-20261118).

`main.py` (Python 3.13, standard library only) copies `entry.png` — a
1024×1024 front page of Wednesday 18 November 2026 — to the harness output
(`/output/entry.png`, or `$MAKEFUN_OUTPUT_DIR/entry.png`). It runs offline
and writes identical bytes on every run.

## What the image sums up

One editorial world map whose flashpoints are the day's top stories:

- **APEC summitry in Asia** — Trump, Xi and Modi converge (Manila Quad talks,
  APEC in Shenzhen), the golden summit hall at upper right.
- **Ukraine strikes the Crimean Bridge** for a second day — the burning
  bridge at upper left.
- **Iranian drones hit the U.S. radar station in Bahrain** — drones, radar
  dome and a tanker in the strait at lower right.
- **Wall Street's plunge** — the Dow down 1,000+ points ahead of Nvidia
  earnings, the red arrow over the skyline at lower left.
- **Voyager 1** closing in on one light-day from Earth — the golden probe
  at the top, beaming home.
- **Cyclone Akvan** over the Bay of Bengal — the spiral at bottom centre.
- **The outage wave** — the NSA's classified network went down, Apple's
  services were disrupted, hackers tampered with supermarket freezers
  across Europe, and Norway's Equinor confirmed a cyberattack, while
  U.S. officials said they saw no coordinated attack; the glitching
  data centre and frost-covered freezers at upper left.
- **Crypto's drawdown** — about half of all bitcoin is now held at a
  loss after the ~50% retreat from October 2025's high, with spot ETF
  outflows passing $850M in a week; the sinking coin at lower left.

The base illustration was generated in-session and framed with a masthead
and headline strips by `build_image.py` (Pillow). The day's stories were
compiled from the morning's wire and front-page reports of 18 Nov 2026.

## Design

The illustration is a flat red/black/navy icon collage in the style of
*The Economist*'s "The World Ahead" covers — a circular globe of small
iconic scenes, one per story. The layout mirrors those covers too:
a small red masthead box and a large date title over the full-bleed
collage, with no headline strips.

## License

MIT — see `LICENSE`.
