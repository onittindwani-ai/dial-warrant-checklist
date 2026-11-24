#!/usr/bin/env python3
"""Turn a filled results CSV into a ranked fix list.

Standard library only. Usage from the kit folder:

    python3 tools/rank_fixes.py my-results.csv
    python3 tools/rank_fixes.py my-results.csv --top 10

The results CSV has three columns: check_id, status, note. Status is one of
Pass, Needs work, Not checked, Not applicable (any capitals). A blank status
counts as Not checked.

ORDER BASIS: this is the kit's own ordering, not legal weight and not a risk
statistic. Needs work comes first, then Not checked. Inside each, checks run
in kit order: your list and your proof of consent first (group A), then the
AI voice and the first seconds of the call (B), do not call and stop requests
(C), calling hours and phone lines (D), state laws, recording and vendors (E),
money and upkeep (F). Everything depends on a proven list, so that comes first.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

STATUS_ALIASES = {
    "pass": "pass",
    "needs work": "needs_work",
    "needs_work": "needs_work",
    "fail": "needs_work",
    "not checked": "not_checked",
    "not_checked": "not_checked",
    "": "not_checked",
    "not applicable": "not_applicable",
    "not_applicable": "not_applicable",
    "n/a": "not_applicable",
}
CHECK_FILE = re.compile(r"^(\d{2})-[a-z0-9-]+\.md$")


def normalise_status(value):
    key = (value or "").strip().lower()
    if key not in STATUS_ALIASES:
        raise ValueError("unknown status %r (use Pass, Needs work, Not checked or Not applicable)" % value)
    return STATUS_ALIASES[key]


def read_results(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        needed = {"check_id", "status"}
        if not reader.fieldnames or not needed.issubset({f.strip() for f in reader.fieldnames}):
            raise ValueError("the CSV needs the columns check_id and status (and optionally note)")
        for line_number, row in enumerate(reader, start=2):
            raw_id = (row.get("check_id") or "").strip()
            if not raw_id:
                continue
            if not raw_id.isdigit() or not 1 <= int(raw_id) <= 33:
                raise ValueError("line %d: check_id %r must be a number from 1 to 33" % (line_number, raw_id))
            rows.append({
                "n": int(raw_id),
                "status": normalise_status(row.get("status")),
                "note": (row.get("note") or "").strip(),
            })
    return rows


def load_check_info(checks_dir):
    """Map check number to (title, first fix step) read from the check files."""
    info = {}
    folder = Path(checks_dir)
    if not folder.is_dir():
        return info
    for p in sorted(folder.iterdir()):
        m = CHECK_FILE.match(p.name)
        if not m:
            continue
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        title = lines[0].split(":", 1)[1].strip() if lines and ":" in lines[0] else p.stem
        first_fix = ""
        in_fix = False
        for line in lines:
            if line.startswith("## How to fix"):
                in_fix = True
                continue
            if in_fix and line.startswith("## "):
                break
            if in_fix and re.match(r"^1\.\s", line):
                first_fix = line[3:].strip()
                break
        info[int(m.group(1))] = (title, first_fix)
    return info


def rank(rows):
    order = {"needs_work": 0, "not_checked": 1}
    todo = [r for r in rows if r["status"] in order]
    todo.sort(key=lambda r: (order[r["status"]], r["n"]))
    return todo


def render(rows, info, top=None):
    counts = {"pass": 0, "needs_work": 0, "not_checked": 0, "not_applicable": 0}
    for r in rows:
        counts[r["status"]] += 1
    ranked = rank(rows)
    shown = ranked if top is None else ranked[:top]
    out = [
        "# Your ranked fix list",
        "",
        "Ordering basis: the kit's own ordering (list and proof first). It is not legal weight or a risk statistic. Not legal advice.",
        "",
        "Pass: %d. Needs work: %d. Not checked: %d. Not applicable: %d." % (
            counts["pass"], counts["needs_work"], counts["not_checked"], counts["not_applicable"]),
        "",
    ]
    if not shown:
        out.append("Nothing to fix from this file. Recheck the rules before each campaign (check 33).")
    for position, r in enumerate(shown, start=1):
        title, first_fix = info.get(r["n"], ("Check %02d" % r["n"], ""))
        label = "Needs work" if r["status"] == "needs_work" else "Not checked yet"
        out.append("%d. Check %02d, %s (%s)" % (position, r["n"], title, label))
        if first_fix:
            out.append("   First step: " + first_fix)
        if r["note"]:
            out.append("   Your note: " + r["note"])
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Rank fixes from a filled results CSV.")
    parser.add_argument("results", help="path to your results CSV")
    parser.add_argument("--top", type=int, default=None, help="show only the first N items")
    parser.add_argument("--checks", default=None, help="folder with the check files (default: the kit's checks folder)")
    args = parser.parse_args(argv)
    checks_dir = args.checks or Path(__file__).resolve().parents[1] / "checks"
    try:
        rows = read_results(args.results)
    except (OSError, ValueError) as err:
        print("Error: %s" % err, file=sys.stderr)
        return 2
    print(render(rows, load_check_info(checks_dir), args.top), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
