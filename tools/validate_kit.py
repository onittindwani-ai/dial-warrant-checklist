#!/usr/bin/env python3
"""Validate the Dial Warrant Checklist kit.

Standard library only. Run from the kit folder:

    python3 tools/validate_kit.py

It checks that there are exactly 33 numbered checks, that every check has the
same fields, that every source link also appears in docs/03-SOURCES.md, that
checks 01 to 03 are the three spoken in the Reel, and that no file holds a
long dash or a private link.
"""
import re
import sys
from pathlib import Path

EXPECTED_CHECKS = 33
REPO_HOME = "github.com/onittindwani-ai/dial-warrant-checklist"
TEXT_SUFFIXES = {".md", ".py", ".csv", ".txt", ".json", ".yml", ".yaml", ""}
SKIP_DIRS = {"__pycache__", ".git"}
CHECK_FILE = re.compile(r"^(\d{2})-[a-z0-9-]+\.md$")

REQUIRED_HEADINGS = [
    "## What to verify",
    "## Why it matters",
    "## Source",
    "## How to fix",
    "## Paste-in prompt",
    "## Status",
]
REQUIRED_FIELD_PREFIXES = ["Source URL:", "Rule or section:", "Date read:"]

# Long dashes and look alikes, built from code points so this file stays clean.
FORBIDDEN_CHARS = {
    chr(0x2010): "hyphen (U+2010)",
    chr(0x2011): "non breaking hyphen (U+2011)",
    chr(0x2012): "figure dash (U+2012)",
    chr(0x2013): "en dash (U+2013)",
    chr(0x2014): "em dash (U+2014)",
    chr(0x2015): "horizontal bar (U+2015)",
    chr(0x2212): "minus sign (U+2212)",
}

# Private or personal link patterns, split so this file does not match itself.
FORBIDDEN_TEXT = [
    "drive" + ".google",
    "docs" + ".google",
    "notion" + ".so",
    "notion" + ".site",
    "mail" + "to:",
    "/" + "Users/",
]

# Keywords that tie checks 01 to 03 to the three checks spoken in the Reel.
SPOKEN_KEYWORDS = {
    1: ["source"],
    2: ["lead magnet", "consent"],
    3: ["buy", "terms", "proof"],
}


def list_check_files(root):
    folder = Path(root) / "checks"
    files = []
    if folder.is_dir():
        for p in sorted(folder.iterdir()):
            if CHECK_FILE.match(p.name):
                files.append(p)
    return files


def parse_check(text):
    """Return a dict with the title, the source URLs and the heading set."""
    lines = text.splitlines()
    title = lines[0] if lines else ""
    return {
        "title": title,
        "headings": {line.strip() for line in lines if line.startswith("## ")},
        "urls": [line.split("Source URL:", 1)[1].strip() for line in lines if line.strip().startswith("- Source URL:")],
        "n_url": sum(1 for line in lines if "Source URL:" in line),
        "n_rule": sum(1 for line in lines if "Rule or section:" in line),
        "n_date": sum(1 for line in lines if "Date read:" in line),
        "has_status": any(line.startswith("Status:") for line in lines),
        "has_prompt_block": "```text" in text,
    }


def check_checks(root):
    problems = []
    files = list_check_files(root)
    if len(files) != EXPECTED_CHECKS:
        problems.append("expected %d check files, found %d" % (EXPECTED_CHECKS, len(files)))
    numbers = [int(CHECK_FILE.match(p.name).group(1)) for p in files]
    if numbers != list(range(1, len(numbers) + 1)) or (numbers and numbers[-1] != EXPECTED_CHECKS):
        problems.append("check numbers must run 01 to %02d with no gaps, found %s" % (EXPECTED_CHECKS, numbers))
    sources_path = Path(root) / "docs" / "03-SOURCES.md"
    sources_text = sources_path.read_text(encoding="utf-8") if sources_path.is_file() else ""
    if not sources_text:
        problems.append("docs/03-SOURCES.md is missing or empty")
    for p in files:
        text = p.read_text(encoding="utf-8")
        info = parse_check(text)
        number = int(CHECK_FILE.match(p.name).group(1))
        if not info["title"].startswith("# Check %02d:" % number):
            problems.append("%s: first line must start with '# Check %02d:'" % (p.name, number))
        for h in REQUIRED_HEADINGS:
            if h not in info["headings"]:
                problems.append("%s: missing heading '%s'" % (p.name, h))
        if info["n_url"] < 1:
            problems.append("%s: no Source URL" % p.name)
        if not (info["n_url"] == info["n_rule"] == info["n_date"]):
            problems.append("%s: Source URL, Rule or section and Date read must appear the same number of times" % p.name)
        if not info["has_status"]:
            problems.append("%s: missing a Status line" % p.name)
        if not info["has_prompt_block"]:
            problems.append("%s: missing the paste-in prompt block" % p.name)
        for url in info["urls"]:
            if url not in sources_text:
                problems.append("%s: source URL not listed in docs/03-SOURCES.md: %s" % (p.name, url))
        if number in SPOKEN_KEYWORDS:
            title_lower = info["title"].lower()
            for word in SPOKEN_KEYWORDS[number]:
                if word not in title_lower:
                    problems.append("%s: title should mention '%s' (spoken check %d)" % (p.name, word, number))
    return problems


def iter_text_files(root):
    for p in sorted(Path(root).rglob("*")):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        if p.suffix.lower() in TEXT_SUFFIXES:
            yield p


def check_forbidden(root):
    problems = []
    github = re.compile(r"github\.com/[^\s)>\]\"'`]*")
    for p in iter_text_files(root):
        rel = p.relative_to(root)
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append("%s: not valid UTF-8 text" % rel)
            continue
        for ch, label in FORBIDDEN_CHARS.items():
            if ch in text:
                problems.append("%s: contains %s" % (rel, label))
        for bad in FORBIDDEN_TEXT:
            if bad in text:
                problems.append("%s: contains forbidden text '%s'" % (rel, bad))
        for match in github.findall(text):
            cleaned = match.rstrip(".,;:")
            if cleaned != REPO_HOME:
                problems.append("%s: GitHub link must be the repo home only, found '%s'" % (rel, cleaned))
    return problems


def check_readme(root):
    readme = Path(root) / "README.md"
    if not readme.is_file():
        return ["README.md is missing"]
    if str(EXPECTED_CHECKS) not in readme.read_text(encoding="utf-8"):
        return ["README.md does not mention the number of checks (%d)" % EXPECTED_CHECKS]
    return []


def check_required_files(root):
    required = [
        "README.md", "LICENSE", "CHANGELOG.md", "AGENTS.md", "CLAUDE.md",
        "docs/00-START-HERE.md", "docs/01-HOW-TO-RUN.md", "docs/02-HONEST-LIMITS.md",
        "docs/03-SOURCES.md", "docs/04-GLOSSARY.md",
        "prompts/00-QUICK-START-PROMPT.md", "prompts/01-FULL-AUDIT-PROMPT.md", "prompts/02-REPORT-PROMPT.md",
        "templates/consent-proof-log.csv", "templates/lead-source-register.csv",
        "templates/stop-request-log.csv", "templates/results-template.csv",
        ".claude/skills/dial-warrant/SKILL.md",
        "tools/validate_kit.py", "tools/rank_fixes.py",
    ]
    return ["missing file: %s" % r for r in required if not (Path(root) / r).is_file()]


def validate(root):
    problems = []
    problems += check_required_files(root)
    problems += check_checks(root)
    problems += check_readme(root)
    problems += check_forbidden(root)
    return problems


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parents[1]
    problems = validate(root)
    count = len(list_check_files(root))
    if problems:
        print("PROBLEMS (%d):" % len(problems))
        for item in problems:
            print(" - " + item)
        return 1
    print("OK: %d checks, all fields present, sources listed, no long dashes, no private links" % count)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
