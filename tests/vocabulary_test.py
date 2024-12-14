"""
Test automation for the class `Vocabulary`
"""

import unittest

from faspellchecker import Vocabulary
from faspellchecker.exceptions import NonPersianWordError


class TestVocabulary(unittest.TestCase):
    """
    Test the class `Vocabulary`
    """

    def test_insert_word(self):
        """
        Test the `Vocabulary` insert_word method
        """

        vocabulary = Vocabulary("test")

        vocabulary.insert_word("لیبخالیبع")
        self.assertTrue("لیبخالیبع" in vocabulary)

        with self.assertRaises(NonPersianWordError):
            vocabulary.add_word("hello")

    def test_set_word_frequency(self):
        """
        Test the `Vocabulary` set_word_frequency method
        """

        # TODO: Implement tests for method `set_word_frequency`

    def test_increase_word_frequency(self):
        """
        Test the `Vocabulary` increase_word_frequency method
        """

        # TODO: Implement tests for method `increase_word_frequency`

    def test_decrease_word_frequency(self):
        """
        Test the `Vocabulary` decrease_word_frequency method
        """

        # TODO: Implement tests for method `decrease_word_frequency`

    def test_delete_word(self):
        """
        Test the `Vocabulary` delete_word method
        """

        vocabulary = Vocabulary("test")

        vocabulary.delete_word("لیبخالیبع")
        self.assertFalse("لیبخالیبع" in vocabulary)


if __name__ == "__main__":
    unittest.main()
