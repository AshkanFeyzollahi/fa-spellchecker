"""
Encompasses exceptions made for spellchecker
"""


class NonPersianWordError(Exception):
    """
    Raised when a non persian/arabic word is passed to dictionary
    """


class WordDoesNotExist(Exception):
    """
    Raised when the demanded word not found by dictionary object
    """
