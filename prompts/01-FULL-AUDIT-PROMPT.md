# Full audit prompt

Use this after the quick start. It walks through all 33 checks in order and builds your results file.

```text
Run the full Dial Warrant Checklist for my business. Use plain words. Explain any legal or AI term in a few simple words the first time.

Same rules as before: US law only, state law varies, not legal advice, never ask for passwords or keys, no real customer data (masked or made up samples only), do not guess, and say "I cannot see this" when you cannot.

HOW TO WORK:
1. Open checks/INDEX.md. Go through checks 01 to 33 in order, one group at a time (A to F).
2. For each check: open its file, read "What to verify", ask me for what the prompt says to look at, and judge it Pass or Needs work. If I truly do not use that thing (for example I never text), mark it Not applicable and say why.
3. For each answer, write one line: check number, status, and a short note with the evidence. Show me the line before moving on.
4. After each group, show me a short summary: how many Pass, Needs work, Not applicable.
5. Some checks are about your phone provider or things I cannot see (checks 25 and 26). For these, write the exact question I must ask my provider, and mark the check Needs work until I bring back the written answer.
6. For checks 21 and 33, tell me that the rules about stop requests have changed recently and that I must recheck the status. Read the source lines of those checks to me.
7. Save everything in my-results.csv (columns: check_id, status, note) in MY folder, not inside the kit. Statuses allowed: Pass, Needs work, Not checked, Not applicable.
8. When all 33 are done, run: python3 tools/rank_fixes.py my-results.csv. Show me the ranked fix list exactly as printed. Tell me the ordering is the kit's own ordering (list and proof first), not legal weight.
9. Finish with the report from prompts/02-REPORT-PROMPT.md.

Never mark a check Pass because I said "I think so". Pass needs something I showed you: a file, a screenshot, a setting, a written reply from a vendor.
```
