# Dial Warrant Checklist: instructions for Codex and other agents

This folder is the Dial Warrant Checklist: 33 checks about US rules for AI cold calls, texts and phone lists. Offer the paste in prompt in `prompts/00-QUICK-START-PROMPT.md` first.

Rules:
- Not legal advice. US law only. State law varies. Say so at the start and in the report.
- Never ask for or print a password, key or token. Use masked or made up sample data only.
- Do not guess. You can only review what the person shows you. You cannot verify a carrier or a record you are not given. Say "I cannot see this".
- Every check cites its source and the date it was read. Show the source line when you report. Tell the person to recheck (check 33) when the date is old.
- Do not state lawsuit or fine figures that are not in the check files.
- Standard library Python only. No dashes (long or en) in any file. GitHub link, if written, is only the repo home.

Commands: `python3 tools/validate_kit.py`, `python3 tools/rank_fixes.py my-results.csv`, `python3 -I -m unittest discover -s tests`
