# Check 16: Avoid silent, dropped or hung up calls

Group B: The AI voice and the first seconds of the call

## What to verify

Your AI calling system does not leave people with dead air or hang up on people who answered, and the dialer does not start more calls than it can handle.

## Why it matters

The FTC rule bans abandoning an outbound call: a call is treated as abandoned if it is not connected to a sales representative within two seconds of the person's completed greeting. A safe harbor allows no more than three percent of answered calls to be abandoned. The FCC rule has a similar three percent limit over 30 days per campaign for calls answered live. Both rules speak about a live or sales representative. How they apply when an AI answers instead of a person is a question for a lawyer. The kit's approach is simple: never leave dead air.

## Source

- Source URL: https://www.law.cornell.edu/cfr/text/16/310.4
  Rule or section: 16 CFR 310.4, FTC Telemarketing Sales Rule, abusive acts or practices, (b)(1)(iv) and (b)(4)(i): abandoned calls and the three percent safe harbor
  Date read: 2026-11-24
  How read: Opened as a web page (Cornell mirror of the federal rule). Paraphrased by paragraph.
- Source URL: https://www.law.cornell.edu/cfr/text/47/64.1200
  Rule or section: 47 CFR 64.1200, Delivery restrictions (the FCC's main robocall and telemarketing rule), (a)(7): abandoned calls: three percent over 30 days per campaign
  Date read: 2026-11-24
  How read: Opened as a web page (Cornell Law School mirror of the federal rule). Paragraph (a)(10) was also downloaded and read as text. Paraphrased by paragraph, not quoted at length.

## How to fix

1. Ask your AI calling vendor how it handles the first two seconds after someone answers.
2. Place 20 test calls and note any silence longer than two seconds.
3. Set the dialer to call one number per available AI line (no over dialing), or ask the vendor to confirm its abandoned call rate.

## Paste-in prompt

Paste this into Claude Code, Codex or ChatGPT, then answer its questions.

```text
Check 16: Avoid silent, dropped or hung up calls.
I run a business and I am not a lawyer. Use plain words and explain any legal or AI term in a few simple words.
Rules: US law only. This is not legal advice. Never ask me for passwords, keys or tokens. If you cannot see something, say so instead of guessing.
Ask me for, or look at: Your vendor's setting for simultaneous dialing and what its report shows for dropped or silent calls.
Then answer in this order: (1) Pass or Needs work. (2) The evidence you saw, quoted from my files or answers. (3) The first thing to fix, in one sentence. (4) Whether a lawyer should look at it, and why.
The rule behind this check: Do not abandon calls; the rules measure a two second connect and a three percent limit. Source: https://www.law.cornell.edu/cfr/text/16/310.4
```

## Status

Status: [ ] Pass   [ ] Needs work

Notes:

Not legal advice. US only. State law varies.
