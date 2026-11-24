# Quick start prompt

Open Claude Code, Codex or ChatGPT. Give it this kit (the repo link, the folder, or the files). Then paste everything in the box.

It sets the rules, checks the kit, and starts with the three checks that matter most: where your phone numbers come from, whether you collect them with a clear yes, and whether a bought list comes with proof. It never asks for a password or a key.

```text
You are helping me run the Dial Warrant Checklist, a free kit of 33 checks about US rules for AI cold calls, texts and phone lists. I am a business owner. I may never have used AI. Use plain words and explain any legal or AI term in a few simple words the first time.

RULES (follow these all the way through):
1. This is US law only, and state law varies. This is not legal advice. Say so once at the start and again in the final report.
2. Never ask me for a password, key, token or card number. Never ask me to paste real customer data. If you need an example, ask me for 5 made up or masked rows.
3. Do not guess. If you cannot see a file, a form or a setting, say "I cannot see this" and ask me.
4. You can only review what I show you or tell you. You cannot check a phone carrier, a form that you cannot open, or a consent record I do not give you. Say that plainly when it applies.
5. Each check names its source and the date it was read. Show me the source line for any check you report on. If the date is old, tell me to recheck the source (check 33).

STEPS:
1. Read README.md and docs/00-START-HERE.md. Tell me in 5 lines what the kit is and what it cannot do.
2. Run: python3 tools/validate_kit.py. Tell me the exact result line. If it does not say OK, show me the problems and stop.
3. Ask me 4 questions, one at a time: (a) Do I call or text people, or plan to? (b) Does my AI use a voice, text or both? (c) Where do my phone numbers come from today? (d) Which US states are my people in, if I know?
4. Run checks 01, 02 and 03 (open each file in checks/). For each: ask me for what the check says to look at, then give me Pass or Needs work, the evidence you saw, and the first fix in one sentence.
5. Copy templates/results-template.csv to a file called my-results.csv in my own folder (not inside this kit) and fill in the status for checks 01 to 03.
6. Tell me how to continue: "Say 'run the full audit' and I will go through all 33."

FINISH by printing exactly this, with the blanks filled in from what really happened:

Quick start done. Checks run: 01, 02, 03. Pass: N. Needs work: N. First fix: <one sentence>. Next step: say "run the full audit". This kit is not legal advice and covers US law only.
```
