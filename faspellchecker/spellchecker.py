"""
Spellchecker base module;
"""

import typing

from faspellchecker.dictionary import Dictionary

__all__ = ("SpellChecker",)


class SpellChecker:
    """
    The SpellChecker class encapsulates the basics needed to accomplish a
    simple spell checking algorithm

    :param dictionary: A dictionary for use with spellchecker,
        defaults to None
    :type dictionary: Dictionary, optional
    """

    def __init__(self, dictionary: Dictionary | None = None):
        self._dictionary = dictionary if dictionary is not None else Dictionary()

    @property
    def dictionary(self) -> Dictionary:
        """
        Return the dictionary object.
        """

        return self._dictionary

    def word_frequency(self, word: str) -> typing.Optional[int]:
        """
        Get the frequency of `word`.

        :param word: The word to get its frequency
        :type word: str
        :return: The word frequency
        :rtype: Optional[int]
        """

        return self.dictionary[word]

    def correction(self, word: str) -> str:
        """
        Find the most probable spelling correction for word

        :param word: The word to correct
        :type word: str
        :return: The most likely candidate or None if no correction is present
        :rtype: str
        """

        return max(self.candidates(word), key=self.word_frequency)

    def candidates(self, word: str) -> typing.Optional[typing.Set[str]]:
        """
        Generate possible spelling corrections for the provided word

        :param word: The word for which to calculate candidate spellings
        :type word: str
        :return: The set of words that are possible candidates or None if there
            are no candidates
        :rtype: set | None
        """

        return (
            self.known([word])
            or self.known(self.edit_distance_1(word))
            or self.known(self.edit_distance_2(word))
            or None
        )

    def known(self, words: typing.Iterable[str]) -> typing.Set[str]:
        """
        The subset of `words` that appear in the dictionary of words

        :param words: List of words to determine which are in the dictionary
        :type words: list
        :return: The set of those words from the input that are in the
            dictionary
        :rtype: set
        """

        return set(word for word in words if word in self.dictionary)

    def unknown(self, words: typing.Iterable[str]) -> typing.Set[str]:
        """
        The subset of `words` that doesn't appear in the dictionary of words

        :param words: List of words to determine which are not in the
            dictionary
        :type words: list
        :return: The set of those words from the input that are not in the
            dictionary
        :rtype: set
        """

        return set(word for word in words if word not in self.dictionary)

    def edit_distance_1(self, word: str) -> typing.Set[str]:
        """
        Compute all strings that are one edit away from `word` using only
        the letters in the dictionary

        :param word: The word for which to calculate the edit distance
        :type word: str
        :return: The set of strings that are edit distance one from the
            provided word
        :rtype: set
        """

        letters = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edit_distance_2(self, word: str) -> typing.Set[str]:
        """
        Compute all strings that are two edits away from `word` using only
        the letters in the dictionary

        :param word: The word for which to calculate the edit distance
        :type word: str
        :return: The set of strings that are edit distance two from the
            provided word
        :rtype: set
        """

        return (
            e2 for e1 in self.edit_distance_1(word) for e2 in self.edit_distance_1(e1)
        )
