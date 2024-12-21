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

        # Test persian words (all)
        self.assertEqual(test_spellchecker.correction("سلام"), "سلام")
        self.assertEqual(test_spellchecker.correction("طنبل"), "تنبل")
        self.assertEqual(test_spellchecker.correction("سابون"), "صابون")

    def test_candidates(self):
        """
        Test the `candidates` method
        """

        # Test persian verb
        self.assertTrue("استخدام" in test_spellchecker.candidates("استحدام"))

        # Something that doesn't exist in vocabulary, so returns None
        self.assertEqual(test_spellchecker.candidates("حشیبذسهصدشس"), None)

    def test_known(self):
        """
        Test the `known` method
        """

        # Test Persian adjectives
        self.assertEqual(
            test_spellchecker.known(["بد", "آلوده", "سبز", "آرايسگر"]),
            {"بد", "آلوده", "سبز"},
        )

        # Test non Persian words
        self.assertEqual(
            test_spellchecker.known(["something", "is", "gonna", "happen"]),
            {"something", "is", "gonna", "happen"}
        )

        # Test both Persian & non Persian words in a single list
        self.assertEqual(
            test_spellchecker.known(["بد", "آلوده", "سبز", "آرايسگر", "something", "is", "gonna", "happen"]),
            {"بد", "آلوده", "سبز", "something", "is", "gonna", "happen"},
        )

    def test_unknown(self):
        """
        Test the `unknown` method
        """

        # Test persian adjectives
        self.assertEqual(
            test_spellchecker.unknown(["بد", "آلوده", "سبز", "آرايسگر"]),
            {"آرايسگر"}
        )

        # Test non Persian words
        self.assertEqual(
            test_spellchecker.known(["something", "is", "gonna", "happen"]),
            {}
        )

        # Test both Persian & non Persian words in a single list
        self.assertEqual(
            test_spellchecker.known(["بد", "آلوده", "سبز", "آرايسگر", "something", "is", "gonna", "happen"]),
            {"آرايسگر"}
        )



if __name__ == "__main__":
    unittest.main()
