"""
Encompasses exceptions made for spellchecker
"""


class NonPersianWordError(Exception):
    """
    Raised when a non persian/arabic word is passed to vocabulary
    """


class WordNotFoundError(Exception):
    """
    Raised when the demanded word not found by vocabulary object
    """
