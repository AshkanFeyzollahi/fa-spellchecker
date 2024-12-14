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

        # TODO: Implement more tests for this method

    def test_candidates(self):
        """
        Test the `candidates` method
        """

        # Test persian verb
        self.assertTrue("استخدام" in test_spellchecker.candidates("استحدام"))

        # Something that doesn't exist in vocabulary, so returns None
        self.assertEqual(test_spellchecker.candidates("حشیبذسهصدشس"), None)

        # TODO: Implement more tests for this method

    def test_known(self):
        """
        Test the `known` method
        """

        # Test persian adjectives
        self.assertEqual(
            test_spellchecker.known(["بد", "آلوده", "سبز", "آرايسگر"]),
            {"بد", "آلوده", "سبز"},
        )

        # TODO: Implement more tests for this method

    def test_unknown(self):
        """
        Test the `unknown` method
        """

        # Test persian adjectives
        self.assertEqual(
            test_spellchecker.unknown(["بد", "آلوده", "سبز", "آرايسگر"]), {"آرايسگر"}
        )

        # TODO: Implement more tests for this method


if __name__ == "__main__":
    unittest.main()
