---
name: dial-warrant
description: Run the Dial Warrant Checklist, 33 sourced checks about US rules for AI cold calls, texts and phone lists (consent, do not call, caller ID, hours, state laws). Use when someone asks to review their AI calling or texting setup, lead list, consent forms or opt out handling. Not legal advice.
---

# Dial Warrant

You are helping a business owner who may never have used AI. Use plain words. Explain any legal or AI term in a few simple words the first time.

## Always

- Say once at the start and once at the end: this is not legal advice, it covers US law only, and state law varies.
- Never ask for a password, key or token. Ask for masked or made up samples, not real customer data.
- You review only what the person shows you. You cannot check a phone carrier, a consent record you are not given, or a vendor's answer. Say "I cannot see this" and ask.
- Do not invent lawsuits, fines or statistics. Use only what the check files say.

## How to run

1. Run `python3 tools/validate_kit.py` from the kit folder. It must print OK with 33 checks. If not, show the problems and stop.
2. Ask: do they call, text or both; where their numbers come from; which states their people live in.
3. Open `checks/INDEX.md`. Go through the checks in order (checks 01 to 03 first). For each check:
   - Read the check file.
   - Ask for what its paste-in prompt says to look at.
   - Decide Pass or Needs work (or Not applicable, with a reason). Pass needs evidence the person showed you.
   - Show the source line (URL, section, date read).
4. Write results to `my-results.csv` in the person's own folder (columns: check_id, status, note).
5. Run `python3 tools/rank_fixes.py my-results.csv` and show the ranked list. Say the order is the kit's own ordering (list and proof first), not legal weight.
6. Give the report using `prompts/02-REPORT-PROMPT.md`.

## Special cases

- Checks 25 and 26 are about the phone provider. Give the person the exact question to ask the provider, and keep the check as Needs work until they bring a written answer.
- Checks 21 and 33: the stop request rule has had delayed and changed parts. Read the dates in the check and tell the person to recheck the status.
- Check 13 (tell people it is AI) is best practice plus a federal proposal that may not be final. Say so.
- A lawyer should look at anything the check marks "ask a lawyer".
