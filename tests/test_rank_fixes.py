"""Offline tests for tools/rank_fixes.py. Run: python3 -I -m unittest discover -s tests"""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT / "tools"))

import rank_fixes  # noqa: E402


def write_csv(rows):
    handle = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="", encoding="utf-8")
    writer = csv.writer(handle)
    writer.writerow(["check_id", "status", "note"])
    writer.writerows(rows)
    handle.close()
    return handle.name


class Ranking(unittest.TestCase):
    def test_needs_work_before_not_checked_then_kit_order(self):
        path = write_csv([["5", "Not checked", ""], ["2", "Needs work", "form has no box"],
                          ["1", "Pass", ""], ["9", "Needs work", ""], ["3", "", ""]])
        rows = rank_fixes.read_results(path)
        order = [(r["n"], r["status"]) for r in rank_fixes.rank(rows)]
        self.assertEqual(order, [(2, "needs_work"), (9, "needs_work"), (3, "not_checked"), (5, "not_checked")])

    def test_pass_and_not_applicable_are_not_listed(self):
        rows = rank_fixes.read_results(write_csv([["1", "Pass", ""], ["2", "N/A", ""]]))
        self.assertEqual(rank_fixes.rank(rows), [])

    def test_status_aliases(self):
        self.assertEqual(rank_fixes.normalise_status("NEEDS WORK"), "needs_work")
        self.assertEqual(rank_fixes.normalise_status("fail"), "needs_work")
        self.assertEqual(rank_fixes.normalise_status(None), "not_checked")

    def test_unknown_status_is_an_error(self):
        with self.assertRaises(ValueError):
            rank_fixes.normalise_status("maybe")

    def test_out_of_range_check_id_is_an_error(self):
        with self.assertRaises(ValueError):
            rank_fixes.read_results(write_csv([["34", "Pass", ""]]))

    def test_missing_columns_is_an_error(self):
        handle = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
        handle.write("a,b\n1,2\n")
        handle.close()
        with self.assertRaises(ValueError):
            rank_fixes.read_results(handle.name)

    def test_render_includes_basis_titles_and_first_step(self):
        rows = rank_fixes.read_results(write_csv([["1", "Needs work", "no register yet"]]))
        info = rank_fixes.load_check_info(KIT / "checks")
        text = rank_fixes.render(rows, info)
        self.assertIn("kit's own ordering", text)
        self.assertIn("Name the source of every number", text)
        self.assertIn("First step:", text)
        self.assertIn("Your note: no register yet", text)

    def test_top_limits_the_list(self):
        rows = rank_fixes.read_results(write_csv([["1", "Needs work", ""], ["2", "Needs work", ""], ["3", "Needs work", ""]]))
        text = rank_fixes.render(rows, {}, top=2)
        self.assertIn("Check 01", text)
        self.assertIn("Check 02", text)
        self.assertNotIn("Check 03", text)

    def test_nothing_to_fix_message(self):
        rows = rank_fixes.read_results(write_csv([["1", "Pass", ""]]))
        self.assertIn("Nothing to fix", rank_fixes.render(rows, {}))

    def test_template_file_reads_as_33_not_checked(self):
        rows = rank_fixes.read_results(KIT / "templates" / "results-template.csv")
        self.assertEqual(len(rows), 33)
        self.assertTrue(all(r["status"] == "not_checked" for r in rows))


if __name__ == "__main__":
    unittest.main()
