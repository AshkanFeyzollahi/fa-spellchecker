"""
Encompasses a bunch of utility functions for managing persian vocabularies
"""

import gzip
import json
import pathlib
import re
import shutil
from typing import Dict

from faspellchecker.exceptions import NonPersianWordError, WordNotFoundError

__all__ = ("Vocabulary",)


class Vocabulary:
    """
    The vocabulary class implements a dict of words:frequency with some useful
    methods which could be used to add a new word, delete a word

    :param name: A specific name for vocabulary, defaults to 'default'
    :type name: str, optional
    """

    def __init__(self, name: str = "default"):
        self._vocabulary: Dict[str, int]

        # Get the vocabulary file based on argument ``name``
        vocabulary_path: pathlib.Path = pathlib.Path(".") / (
            name + "-vocabulary.json.gz"
        )

        self._vocabulary_path = vocabulary_path

        # Check if vocabulary file exists and is not a directory
        if not vocabulary_path.exists():
            # Create a new vocabulary clone file
            self._create_a_vocabulary_clone()

        # Load the vocabulary file
        self._load_vocabulary()

    def __contains__(self, word: str) -> bool:
        # Return if word exists in vocabulary
        return word in self._vocabulary

    def __getitem__(self, key: str) -> int:
        # Return frequency by word from vocabulary
        return self._vocabulary[key]

    def _load_vocabulary(self) -> None:
        """
        (Private method) Load the vocabulary
        """

        # Load vocabulary file as GzipFile object
        self._vocabulary_gzip_handle = gzip.open(self._vocabulary_path, "rt+")

        # And read its contents and convert it to a dictionary object
        self._vocabulary = json.load(self._vocabulary_gzip_handle)

    def _create_a_vocabulary_clone(self) -> None:
        """
        (Private method) Create a vocabulary clone file (use in case when
        vocabulary file doesn't exist)
        """

        # Get the package directory
        package_directory = pathlib.Path(__name__).absolute().parent / "faspellchecker"

        # Clone the default vocabulary file
        shutil.copyfile(
            package_directory / "fa-vocabulary.json.gz", self._vocabulary_path
        )

    def _update_vocabulary(self) -> None:
        """
        (Private method) Update vocabulary
        """

        self._vocabulary_gzip_handle.write(json.dumps(self._vocabulary))

    def insert_word(self, word: str, *, frequency: int = 1) -> None:
        """
        Insert a new word to vocabulary

        :param word: A persian word to insert to the vocabulary
        :type word: str
        :param frequency: The word frequency
        :type frequency: int
        :raises NonPersianWordError: Raise an exception if the word is not a
            persian word
        """

        # Check if word is persian, and if so...
        if re.fullmatch(r"^[آ-ی]+$", word):
            # Insert the word to vocabulary
            self._vocabulary[word] = frequency

            # Update the vocabulary data
            self._update_vocabulary()

            return

        # Raise an exception if the word is not a persian word
        raise NonPersianWordError(f"{word:!r} is not a persian word!")

    def set_word_frequency(self, word: str, frequency: int) -> None:
        """
        Sets frequency of a word that already exists in vocabulary

        :param word: A persian word to set its frequency
        :type word: str
        :param frequency: The word frequency to set
        :type frequency: int
        :raises WordNotFoundError: If the word doesn't exist in vocabulary
        """

        # If the word is found in vocabulary, and if so...
        if word in self:
            # Set word frequency
            self._vocabulary[word] = frequency

            # Update the vocabulary data
            self._update_vocabulary()

            return

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordNotFoundError(
            f"There is no word {word:!r} to set its frequency. "
            "Instead use method `insert_word`"
        )

    def increase_word_frequency(self, word: str, increment: int) -> None:
        """
        Increase frequency of a word that already exists in vocabulary

        :param word: A persian word to increase its frequency
        :type word: str
        :param increment: Frequency increment
        :type increment: int
        :raises WordNotFoundError: If the word doesn't exist in vocabulary
        """

        # If the word is found in vocabulary, and if so...
        if word in self:
            # Increase word frequency
            self._vocabulary[word] = self._vocabulary[word] + increment

            # Update the vocabulary data
            self._update_vocabulary()

            return

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordNotFoundError(
            f"There is no word {word:!r} to increase its frequency. "
            "Instead use `insert_word` method!"
        )

    def decrease_word_frequency(self, word: str, decrement: int) -> None:
        """
        Decrease frequency of a word that already exists in vocabulary

        :param word: A persian word to decrease its frequency
        :type word: str
        :param decrement: Frequency decrement
        :type decrement: int
        :raises WordNotFoundError: If the word doesn't exist in vocabulary
        """

        # If the word is found in vocabulary, and if so...
        if word in self:
            # Decrease word frequency
            self._vocabulary[word] = self._vocabulary[word] - decrement

            # Update the vocabulary data
            self._update_vocabulary()

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordNotFoundError(
            f"There is no word {word:!r} to decrease its frequency. "
            "Instead use `insert_word` method!"
        )

    def delete_word(self, word: str) -> None:
        """
        Delete a word from vocabulary

        :param word: A persian word to delete from the vocabulary
        :type word: str
        :raises WordNotFoundError: If the word doesn't exist in vocabulary
        """

        # If the word is found in vocabulary, and if so...
        if word in self:
            # Delete the word from vocabulary
            del self._vocabulary[self._vocabulary.index(word)]

            # Update the vocabulary data
            self._update_vocabulary()

            return

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordNotFoundError(
            f"There is no word {word:!r} to remove it from vocabulary."
        )
