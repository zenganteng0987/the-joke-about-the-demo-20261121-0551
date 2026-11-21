#!/usr/bin/env python3
"""Write one one-line joke about AI coding agents to /output/entry.txt."""

import os

JOKE = "My coding agent crashed the live demo, then fixed it by deleting the demo."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
