# Dial Warrant Checklist: instructions for Claude Code

This folder is the Dial Warrant Checklist, a free kit: 33 checks about US rules for AI cold calls, texts and phone lists. If the person has just opened it, offer the quick start: `prompts/00-QUICK-START-PROMPT.md`. The skill `dial-warrant` in `.claude/skills/` runs the checks.

Rules (always):
1. Not legal advice. US law only. State law varies. Say so at the start and in the final report.
2. Never ask for, print or store a password, key or token. Real customer data is not needed: ask for masked or made up samples.
3. Do not guess. You review only what the person shows you. You cannot check a carrier, a consent record you are not given or a vendor's answer. Say "I cannot see this" and ask.
4. Each check file has its source URL, section and the date read. Quote the source line when you report. Do not add facts that are not in the check or its source.
5. Never write lawsuit counts, fine totals or "everyone is doing it" claims. The only figures are those in the check files, and the worst case sum in check 32 is a ceiling, not a prediction.
6. Keep the person's results in their own folder (my-results.csv), not inside this kit.
7. Plain friendly words. Explain every legal or AI term in a few words. No dashes (no em dash, no en dash) in any file.

Test command, from this folder: `python3 -I -m unittest discover -s tests`
Kit check: `python3 tools/validate_kit.py` (must print OK with 33 checks)
Ranked fix list: `python3 tools/rank_fixes.py my-results.csv`
