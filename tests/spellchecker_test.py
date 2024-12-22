"""
Test automation for the class `SpellChecker`
"""

import unittest

from faspellchecker import SpellChecker, Vocabulary

test_spellchecker = SpellChecker(Vocabulary("test"))


class TestSpellChecker(unittest.TestCase):
    """
    Test the class `SpellChecker`
    """

    def test_correction(self):
        """
        Test the `correction` method
        """

        self.assertEqual(test_spellchecker.correction("سلام"), "سلام")
        self.assertEqual(test_spellchecker.correction("تتنبل"), "تنبل")
        self.assertEqual(test_spellchecker.correction("سابون"), "صابون")

    def test_candidates(self):
        """
        Test the `candidates` method
        """

        self.assertTrue("استخدام" in test_spellchecker.candidates("استحدام"))

        self.assertEqual(test_spellchecker.candidates("حشیبذسهصدشس"), None)

    def test_known(self):
        """
        Test the `known` method
        """

        self.assertEqual(
            test_spellchecker.known(["بد", "آلوده", "سبز", "آرايسگر"]),
            {"بد", "آلوده", "سبز"},
        )

    def test_unknown(self):
        """
        Test the `unknown` method
        """

        self.assertEqual(
            test_spellchecker.unknown(["بد", "آلوده", "سبز", "آرايسگر"]),
            {"آرايسگر"}
        )



if __name__ == "__main__":
    unittest.main()
