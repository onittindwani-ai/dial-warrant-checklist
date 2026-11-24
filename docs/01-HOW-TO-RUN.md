# How to run the checks

The checks are plain files. Any AI assistant that can read them can walk you through them. Here is how to do it with the three common ones.

**Not legal advice. US only. State law varies.**

## What you need

- A folder with this kit on your computer (download the repo from its home page, https://github.com/onittindwani-ai/dial-warrant-checklist , or give your assistant the link).
- Optional: Python 3.9 or newer, only to run the two small scripts (`tools/validate_kit.py` and `tools/rank_fixes.py`). No installs, no packages.
- Your own material to review: your forms, your lead sources, your call script, your opt out settings. Use masked or made up examples. Do not paste real customer data.

## Claude Code

1. Open Claude Code inside the kit folder.
2. Type: `Run these checks for my business and tell me what to fix first.` The skill `dial-warrant` in `.claude/skills/dial-warrant/` loads, or paste `prompts/00-QUICK-START-PROMPT.md`.
3. Answer its questions. It can run the two scripts for you and saves your results in `my-results.csv` in your own folder.

## Codex

1. Open Codex in the kit folder. It reads `AGENTS.md` first.
2. Paste `prompts/00-QUICK-START-PROMPT.md`, then `prompts/01-FULL-AUDIT-PROMPT.md`.
3. It can run the scripts and write `my-results.csv` for you.

## ChatGPT or another chat assistant

A plain chat usually cannot run scripts or read a folder. So:

1. Upload the files in `checks/` and `prompts/` (or paste a check at a time).
2. Paste `prompts/00-QUICK-START-PROMPT.md`. Skip step 2 of that prompt (the script run) and say so.
3. Keep your results in a spreadsheet using `templates/results-template.csv`. If you want the ranked list, run `python3 tools/rank_fixes.py my-results.csv` yourself on any computer with Python, or ask the assistant to rank the Needs work rows in kit order (check number order, Needs work first, then Not checked).

## One check at a time

Every check file has a "Paste-in prompt" section. Paste it into your assistant, answer, then tick Pass or Needs work in the file or in your results sheet.

## Good habits

- Give the assistant only what it needs. Never paste a password, key or token. If it asks for one, stop.
- Mark Pass only when you showed it evidence (a file, a screenshot, a setting, a written reply from a vendor).
- Save your results outside the kit folder so an update to the kit does not overwrite them.
- Recheck before each campaign (check 33).

## What the assistant cannot do

See `docs/02-HONEST-LIMITS.md`. In short: it can only review what you show it.
