"""
Some utilities written for use with/in faspellchecker
"""

import re

__all__ = ("is_persian_word",)


def is_persian_word(word: str) -> bool:
    """
    Checks if a word is Persian
    
    :param word: The word to check
    :type word: str
    :return: Is Persian?
    :rtype: bool
    """

    return re.fullmatch("^[آ-ی]$+", word) is not None
