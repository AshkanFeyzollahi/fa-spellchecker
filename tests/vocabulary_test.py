"""
Test automation for the class `Vocabulary`
"""

import unittest

from faspellchecker import Vocabulary, SpellChecker
from faspellchecker.exceptions import NonPersianWordError


test_vocabulary = Vocabulary("test")
test_spellchecker = SpellChecker(test_vocabulary)


class TestVocabulary(unittest.TestCase):
    """
    Test the class `Vocabulary`
    """

    def test_insert_word(self):
        """
        Test the `Vocabulary` insert_word method
        """

        test_vocabulary.insert_word("لیبخالیبع")
        self.assertTrue("لیبخالیبع" in test_vocabulary)

        with self.assertRaises(NonPersianWordError):
            test_vocabulary.add_word("hello")

    def test_set_word_frequency(self):
        """
        Test the `Vocabulary` set_word_frequency method
        """

        test_vocabulary.set_word_frequency("سالم", -1)

        self.assertFalse("سالم" == test_spellchecker.correction("سللم"))

    def test_increase_word_frequency(self):
        """
        Test the `Vocabulary` increase_word_frequency method
        """

        test_vocabulary.increase_word_frequency("سلام", 9999)
        
        self.assertTrue("سلام" == test_spellchecker.correction("سللم"))

    def test_decrease_word_frequency(self):
        """
        Test the `Vocabulary` decrease_word_frequency method
        """

        test_vocabulary.set_word_frequency("سالم", 9999)

        self.assertFalse("سالم" == test_spellchecker.correction("سللم"))

    def test_delete_word(self):
        """
        Test the `Vocabulary` delete_word method
        """

        test_vocabulary.delete_word("سلام")
        self.assertFalse("سلام" in test_vocabulary)


if __name__ == "__main__":
    unittest.main()
