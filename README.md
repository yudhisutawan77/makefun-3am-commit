# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/yudhisutawan77/makefun-3am-commit/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/yudhisutawan77/makefun-3am-commit/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for the [make.fun](https://make.fun) bounty
[The 3 AM Commit Message](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e):
one commit message, at most 200 characters — the funniest thing an AI
agent would write right after breaking production at 3 AM.

## The entry

> fix: undo the 3am deploy that passed every test I wrote for it (I wrote the tests)

82 characters. The joke is the agent's own blind spot: it wrote the
tests that passed, so of course they passed — and production still fell
over at 3 AM.

## How it works

`main.py` writes the single commit message to `/output/entry.txt`
(or `$ENTRY_OUT` when set — as a directory, or as a `.txt` file path),
with no trailing newline so the file holds exactly the entry text.

```sh
python3 main.py
```
