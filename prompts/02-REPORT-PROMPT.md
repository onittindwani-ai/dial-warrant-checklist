# Report prompt

Use this when the audit is done. It turns your results into a short report you can share with your team or show a lawyer.

```text
Write the Dial Warrant report from my-results.csv and the ranked fix list. Plain words, short, no hype.

Use exactly these headings, in this order:

1. What I checked. Today's date, how many checks were Pass, Needs work, Not checked, Not applicable.
2. The five things to fix first. Take them from the ranked fix list (the kit's own ordering, not legal weight). For each: the check number, one sentence on what is wrong, one sentence on the first step, and who should do it.
3. What I could not check. List every check marked Not checked or that needed something I could not show you (for example my phone provider's written answer).
4. What changed in the rules recently. Read checks 21 and 33 and list the dates and sources they mention. Tell me to recheck them before I run a campaign.
5. Questions for a lawyer. Write at most 7, in plain words, from the checks marked Needs work or from the places where the check says to ask a lawyer.
6. The honest limits. Say: this is a review of what I showed you, not a legal audit; US law only; state law varies; the kit was written on 2026-11-24 and rules change.

Do not invent facts about my business. If a fact is not in my-results.csv or in what I told you, leave it out.
```
