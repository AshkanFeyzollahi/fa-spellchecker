"""
Test automation for the utilities
"""

import unittest

from faspellchecker.utils import ignore_non_persian_words, is_word_persian


class TestUtilities(unittest.TestCase):
    """
    Test the utilities
    """

    def test_is_word_persian(self):
        """
        Test the function `is_word_persian`
        """

        self.assertTrue(is_word_persian("سالم"))
        self.assertTrue(is_word_persian("سللم"))

        self.assertFalse(is_word_persian("۱کالا"))
        self.assertFalse(is_word_persian("دوست صمیمی"))
        self.assertFalse(is_word_persian("صابون\n"))
        self.assertFalse(is_word_persian("مجموعهA"))

        self.assertFalse(is_word_persian("hello"))

    def test_ignore_non_persian_words(self):
        """
        Test the function `ignore_non_persian_words`
        """

        self.assertEqual(
            ignore_non_persian_words(
                ["سالم", "سللم", "۱کالا", "دوست صمیمی", "صابون\n", "مجموعهA", "hello"]
            ),
            ["سالم", "سللم"],
        )
