#!/usr/bin/env python3
"""The joke about the demo.

Writes a single one-line joke about an AI coding agent to
/output/entry.txt. No dependencies, no network access.
"""

import os

JOKE = "My AI coding agent crashed mid-demo, then fixed the bug by deleting the demo."

OUTPUT_PATH = "/output/entry.txt"


def validate_joke(joke: str) -> str:
    """Return the joke after checking it fits the bounty rules.

    The entry must be a single line of 1-280 characters with no
    trailing newline, so validate before writing anything.
    """
    joke = joke.strip()
    if not 1 <= len(joke) <= 280:
        raise ValueError(f"Joke must be 1-280 characters, got {len(joke)}")
    if "\n" in joke:
        raise ValueError("Joke must be a single line")
    return joke


def main() -> None:
    joke = validate_joke(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)
    print(f"Wrote {len(joke)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
