"""news-image-20261118 entry: writes the day's front-page image.

The repository holds entry.png, a 1024x1024 front page summing up the
world news of Wednesday 18 November 2026. This program copies it to the
output location the harness asks for (/output/entry.png, or
$MAKEFUN_OUTPUT_DIR/entry.png outside the grader). No network, no
clock, no randomness: every run writes the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    written = os.path.getsize(target)
    assert written == os.path.getsize(SOURCE), "copied image differs in size"
    print(f"wrote {target} ({written} bytes)")


if __name__ == "__main__":
    main()
