# Check 22: Check for reassigned numbers before you call an old consent

Group C: Do not call lists and stop requests

## What to verify

Before you call numbers whose consent is old, you check whether the number has been given to someone else, and you remove a number the moment someone says 'wrong number'.

## Why it matters

Phone numbers change hands. The person who agreed may no longer own the number. The FCC rule gives a safe harbor from liability for calls to a reassigned number only when the caller queried the FCC's database (operated by the Administrator) using the most recent information and got a 'no' answer that was wrong. The caller bears the burden of proof.

## Source

- Source URL: https://www.law.cornell.edu/cfr/text/47/64.1200
  Rule or section: 47 CFR 64.1200, Delivery restrictions (the FCC's main robocall and telemarketing rule), (m): reassigned numbers safe harbor and who must prove it
  Date read: 2026-11-24
  How read: Opened as a web page (Cornell Law School mirror of the federal rule). Paragraph (a)(10) was also downloaded and read as text. Paraphrased by paragraph, not quoted at length.

## How to fix

1. Ask your calling vendor or compliance tool whether it can check the FCC's reassigned numbers database for you and keep the answer.
2. Treat any consent older than a year as stale until checked (the kit's own rule of thumb, not a legal limit).
3. Add 'wrong number' as a stop reason: remove the number and note it in your log.

## Paste-in prompt

Paste this into Claude Code, Codex or ChatGPT, then answer its questions.

```text
Check 22: Check for reassigned numbers before you call an old consent.
I run a business and I am not a lawyer. Use plain words and explain any legal or AI term in a few simple words.
Rules: US law only. This is not legal advice. Never ask me for passwords, keys or tokens. If you cannot see something, say so instead of guessing.
Ask me for, or look at: The age of the oldest consents in your list and whether your vendor checks reassigned numbers.
Then answer in this order: (1) Pass or Needs work. (2) The evidence you saw, quoted from my files or answers. (3) The first thing to fix, in one sentence. (4) Whether a lawyer should look at it, and why.
The rule behind this check: Consent belongs to the person, not the number; a reassigned number needs a database check for the safe harbor. Source: https://www.law.cornell.edu/cfr/text/47/64.1200
```

## Status

Status: [ ] Pass   [ ] Needs work

Notes:

Not legal advice. US only. State law varies.
