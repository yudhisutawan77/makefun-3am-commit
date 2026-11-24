#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt,
or to $ENTRY_OUT when set. ENTRY_OUT may be a directory (entry.txt is
created inside it) or a file path ending in .txt (written directly).

The message itself: an AI agent at 3 AM, reverting its own deploy after
breaking production. The punchline is the agent's blind spot — it wrote
the tests that passed, so of course they passed.
"""

import os
import sys

# Candidate A (chosen): the agent trusts its own tests, which it wrote.
# Candidates B and C were rejected in the builder notes — B rambles, C
# leans on the overused "logs said all good" trope.
CHOSEN_LINE = (
    "fix: undo the 3am deploy that passed every test "
    "I wrote for it (I wrote the tests)"
)


def compose_line() -> str:
    """Return the single commit message, exactly as it will be judged."""
    return CHOSEN_LINE


def line_passes_gate(line: str) -> bool:
    """Gate: UTF-8 text, 1 to 200 characters, not only whitespace."""
    return 0 < len(line) <= 200 and line.strip() != ""


def entry_target_path() -> str:
    """Resolve where entry.txt goes, honouring $ENTRY_OUT as file or dir."""
    destination = os.environ.get("ENTRY_OUT") or "/output"
    if destination.endswith(".txt"):
        return destination
    return os.path.join(destination, "entry.txt")


def persist_line(line: str, target: str) -> None:
    """Write the entry with no trailing newline — every byte counts."""
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main() -> int:
    line = compose_line()
    if not line_passes_gate(line):
        print(f"entry invalid: {len(line)} chars", file=sys.stderr)
        return 1
    target = entry_target_path()
    persist_line(line, target)
    print(f"wrote {target} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
