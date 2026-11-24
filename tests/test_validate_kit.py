"""Offline tests for tools/validate_kit.py. Run: python3 -I -m unittest discover -s tests"""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT / "tools"))

import validate_kit  # noqa: E402


class RealKit(unittest.TestCase):
    def test_real_kit_is_valid(self):
        self.assertEqual(validate_kit.validate(KIT), [])

    def test_exactly_33_checks(self):
        self.assertEqual(len(validate_kit.list_check_files(KIT)), 33)

    def test_spoken_checks_are_first_three(self):
        names = [p.name for p in validate_kit.list_check_files(KIT)][:3]
        self.assertTrue(names[0].startswith("01-"))
        titles = [p.read_text(encoding="utf-8").splitlines()[0].lower() for p in validate_kit.list_check_files(KIT)[:3]]
        self.assertIn("source", titles[0])
        self.assertIn("lead magnet", titles[1])
        self.assertIn("buy", titles[2])


class Mutations(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.root = self.tmp / "kit"
        shutil.copytree(KIT, self.root, ignore=shutil.ignore_patterns("__pycache__", ".git"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def first_check(self):
        return validate_kit.list_check_files(self.root)[4]

    def problems(self):
        return validate_kit.validate(self.root)

    def test_missing_check_is_reported(self):
        self.first_check().unlink()
        joined = " ".join(self.problems())
        self.assertIn("expected 33 check files", joined)

    def test_missing_field_is_reported(self):
        p = self.first_check()
        p.write_text(p.read_text(encoding="utf-8").replace("## How to fix", "## Fix"), encoding="utf-8")
        self.assertTrue(any("How to fix" in x for x in self.problems()))

    def test_long_dash_is_reported(self):
        p = self.first_check()
        p.write_text(p.read_text(encoding="utf-8") + "\nbad " + chr(0x2014) + " dash\n", encoding="utf-8")
        self.assertTrue(any("U+2014" in x for x in self.problems()))

    def test_en_dash_is_reported(self):
        p = self.first_check()
        p.write_text(p.read_text(encoding="utf-8") + "\nbad " + chr(0x2013) + " dash\n", encoding="utf-8")
        self.assertTrue(any("U+2013" in x for x in self.problems()))

    def test_private_link_is_reported(self):
        p = self.first_check()
        bad = "https://" + "drive" + ".google" + ".com/file"
        p.write_text(p.read_text(encoding="utf-8") + "\n" + bad + "\n", encoding="utf-8")
        self.assertTrue(any("forbidden text" in x for x in self.problems()))

    def test_local_path_is_reported(self):
        p = self.first_check()
        p.write_text(p.read_text(encoding="utf-8") + "\n/" + "Users" + "/someone/file\n", encoding="utf-8")
        self.assertTrue(any("forbidden text" in x for x in self.problems()))

    def test_github_deep_link_is_reported(self):
        p = self.first_check()
        link = "https://github.com/onittindwani-ai/dial-warrant-checklist" + "/rel" + "eases/latest"
        p.write_text(p.read_text(encoding="utf-8") + "\n" + link + "\n", encoding="utf-8")
        self.assertTrue(any("repo home only" in x for x in self.problems()))

    def test_repo_home_link_is_allowed(self):
        p = self.first_check()
        link = "https://github.com/onittindwani-ai/dial-warrant-checklist."
        p.write_text(p.read_text(encoding="utf-8") + "\n" + link + "\n", encoding="utf-8")
        self.assertEqual(self.problems(), [])

    def test_source_not_in_sources_doc_is_reported(self):
        p = self.first_check()
        p.write_text(p.read_text(encoding="utf-8") + "\n- Source URL: https://example.org/not-listed\n  Rule or section: x\n  Date read: 2026-11-24\n", encoding="utf-8")
        self.assertTrue(any("not listed in docs/03-SOURCES.md" in x for x in self.problems()))

    def test_missing_status_is_reported(self):
        p = self.first_check()
        p.write_text(p.read_text(encoding="utf-8").replace("Status: [ ] Pass", "State: [ ] Pass"), encoding="utf-8")
        self.assertTrue(any("Status line" in x for x in self.problems()))

    def test_wrong_spoken_title_is_reported(self):
        p = validate_kit.list_check_files(self.root)[0]
        p.write_text(p.read_text(encoding="utf-8").replace("# Check 01: Name the source of every number", "# Check 01: Something else"), encoding="utf-8")
        self.assertTrue(any("spoken check 1" in x for x in self.problems()))


if __name__ == "__main__":
    unittest.main()
