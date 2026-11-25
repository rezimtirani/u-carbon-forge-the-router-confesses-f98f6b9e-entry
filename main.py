"""The Router Confesses.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the excuse a
home Wi-Fi router gives for dropping the connection at the exact
moment a movie reaches its climax. Standard library only.
"""

import os
import sys

ROUTER_CONFESSION = (
    "I didn't drop the connection \u2014 I paused it myself. "
    "The plot twist was so good even my firmware needed a "
    "minute to process it."
)


def router_gate(text):
    """Check the confession against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one excuse from a home
    Wi-Fi router for dropping the connection at a movie's climax.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("confession must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "confession is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("confession must be exactly one line")
    return cleaned


def router_measure(text):
    """Measure the confession for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A confession too short to carry a setup and
    a turn, or one padded out to fill the cap instead of landing
    the punchline, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = router_gate(ROUTER_CONFESSION)
    shape = router_measure(text)
    if shape["words"] < 5:
        raise ValueError("confession is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
