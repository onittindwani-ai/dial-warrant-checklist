# The Dial Warrant Checklist

**33 plain checks, each with its source, for anyone who wants to use AI to call or text people in the US without getting into trouble over where the numbers came from.**

A "warrant" is a written permission to act. Before an AI dials a number, you should be able to show your permission to call it. This kit lists 33 things to check, each with the exact rule or page it comes from, and a prompt an AI assistant can use to walk you through it.

Free and open (MIT licence). Made by Onit Tindwani, Sendora.

**This is not legal advice. It covers US law only. State law varies. The kit was written on 2026-11-24 and rules change.**

## Why it exists

Since February 2024 the FCC (the US body that runs phone rules) has said that AI voices that sound human count as "artificial voices" under the Telephone Consumer Protection Act (the TCPA, the US law about robocalls and texts). That means a call with an AI voice generally needs the called person's consent first, and a signed written consent when the call sells something. Check 11 has the source.

The biggest risk is not the AI caller. It is a list of numbers nobody said "yes" to.

## What you get

| Folder or file | What it is |
| --- | --- |
| `checks/` | The 33 checks, numbered 01 to 33, one file each, with the source, how to fix it, a paste in prompt and a Pass or Needs work box. Start at `checks/INDEX.md`. |
| `prompts/` | A quick start prompt, a full audit prompt and a report prompt. |
| `templates/` | A consent proof log, a lead source register, a stop request log and a results sheet. Every sample row says SAMPLE and is made up. |
| `docs/` | Start here, how to run it with Claude Code, Codex or ChatGPT, the honest limits, every source with the date it was read, and a plain glossary. |
| `tools/` | Two small Python scripts: one checks the kit is complete, one turns your filled results into a ranked fix list. Standard library only. |
| `.claude/skills/dial-warrant/` | A skill for Claude Code so it can run the checks for you. |
| `tests/` | Tests that run offline. |

## The 3 checks from the Reel

1. **Check 01:** Know where every number came from. If you cannot name the source, do not call.
2. **Check 02:** Collect numbers with your own lead magnet (a free guide or checklist people sign up for), with a box people tick to allow contact.
3. **Check 03:** If you buy a list, read the provider's terms and ask for proof that those people agreed to be contacted.

The other 30 checks cover the wording of consent, the AI voice itself, do not call lists and stop requests, calling hours and phone lines, three state laws, recording, vendors, and money and upkeep.

## The easiest first step

Give your AI assistant (Claude Code, Codex or ChatGPT) this repo link, https://github.com/onittindwani-ai/dial-warrant-checklist , and say:

> Run these checks for my business and tell me what to fix first.

Or open `prompts/00-QUICK-START-PROMPT.md`, paste it, and answer 4 short questions.

## What it cannot do

- It is **not legal advice**, and it does not replace a lawyer. Several checks tell you when to ask one.
- It covers **US law only**. State laws differ and change. The kit covers Florida, Oklahoma and Maryland as examples, not every state.
- An AI assistant can only review what you show it: your forms, your lists, your scripts, your settings and your answers. It **cannot see your phone carrier, cannot verify consent records it is not given, and cannot confirm a vendor's answer**. Checks 25 and 26 are questions you take to your provider.
- It does not tell you whether a specific call is legal.
- It does not predict fines or lawsuits. Check 32 shows how to do the sum for a worst case, nothing more.
- Rules move. Check 33 is a reminder to recheck before every campaign.
- Some sources could not be opened on the day of writing. They are listed in `docs/03-SOURCES.md`.

## Check that the kit is complete

```text
python3 tools/validate_kit.py
python3 -I -m unittest discover -s tests
```

## Credits

Written by Onit Tindwani, Sendora. Sources are public laws, rules, court opinions and company policies listed with links in `docs/03-SOURCES.md`.
