"""news-image-20261126: copy the pre-rendered front-page image to the output.

The image sums up the world news of Thursday 26 November 2026 in six
panels: the Houthi strike on Saudi Arabia's Ras Tanura refinery (oil
above $94), new US tariffs (up to 15% on Taiwan), Pakistan's first
astronaut joining China's Shenzhou-24 mission to Tiangong, Russian
drone strikes killing 7 in Ukraine, Poland's planned no-fly zone on
the Ukraine border, and US consumer confidence near a 2-year high.

Deterministic: the same bytes are copied on every run. No network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Integrity check: the copy must be byte-for-byte identical.
    if os.path.getsize(src) != os.path.getsize(dst):
        raise RuntimeError("entry.png copy size mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
