"""
Test automation for the class `Dictionary`
"""

import unittest

from faspellchecker import Dictionary, SpellChecker
from faspellchecker.exceptions import NonPersianWordError, WordDoesNotExist

test_dictionary = Dictionary("test")
test_spellchecker = SpellChecker(test_dictionary)


class TestDictionary(unittest.TestCase):
    """
    Test the class `Dictionary`
    """

    def test_insert_word(self):
        """
        Test the `Dictionary` insert_word method
        """

        test_dictionary.insert_word("لیبخالیبع")
        self.assertIn("لیبخالیبع", test_dictionary)

        with self.assertRaises(NonPersianWordError):
            test_dictionary.insert_word("hello")

    def test_set_word_frequency(self):
        """
        Test the `Dictionary` set_word_frequency method
        """

        test_dictionary.set_word_frequency("سالم", -1)
        self.assertNotEqual(test_spellchecker.correction("سللم"), "سالم")

        test_dictionary["سالم"] = 99999
        self.assertEqual(test_spellchecker.correction("سللم"), "سالم")

        test_dictionary.set_word_frequency("سالم", -1)

    def test_increase_word_frequency(self):
        """
        Test the `Dictionary` increase_word_frequency method
        """

        if "سلام" not in test_dictionary:
            test_dictionary.insert_word("سلام")

        test_dictionary.increase_word_frequency("سلام", 9999)
        self.assertEqual(test_spellchecker.correction("سللم"), "سلام")

        test_dictionary["سالم"] += 99999
        self.assertEqual(test_spellchecker.correction("سللم"), "سالم")

    def test_decrease_word_frequency(self):
        """
        Test the `Dictionary` decrease_word_frequency method
        """

        test_dictionary.decrease_word_frequency("سالم", 9999)
        self.assertNotEqual(test_spellchecker.correction("سللم"), "سالم")

        test_dictionary["سالم"] -= 9999

    def test_delete_word(self):
        """
        Test the `Dictionary` delete_word method
        """

        test_dictionary.delete_word("سلام")
        self.assertNotIn("سلام", test_dictionary)

        with self.assertRaises(WordDoesNotExist):
            del test_dictionary["سلام"]


if __name__ == "__main__":
    unittest.main()
