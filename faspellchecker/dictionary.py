"""
Encompasses a bunch of utility functions for managing persian vocabularies
"""

import gzip
import json
import pathlib
import shutil
from typing import Dict

from faspellchecker.exceptions import NonPersianWordError, WordDoesNotExist
from faspellchecker.utils import is_persian_word

__all__ = ("Dictionary",)


class Dictionary:
    """
    The dictionary class implements a dict of words:frequency with some useful
    methods which could be used to add a new word, delete a word

    :param name: A specific name for dictionary, defaults to 'default'
    :type name: str, optional
    """

    def __init__(self, name: str = "default"):
        self._dictionary: Dict[str, int]

        # Get the dictionary file based on argument ``name``
        dictionary_path: pathlib.Path = pathlib.Path(".") / (
            name + "-dictionary.json.gz"
        )

        self._dictionary_path = dictionary_path

        # Check if dictionary file exists and is not a directory
        if not dictionary_path.exists():
            # Create a new dictionary clone file
            self._create_a_dictionary_clone()

        # Load the dictionary file
        self._load_dictionary()

    def __contains__(self, word: str) -> bool:
        # Return if word exists in dictionary
        return word in self._dictionary

    def __getitem__(self, key: str) -> int:
        # Return frequency by word from dictionary
        return self._dictionary[key]

    def __setitem__(self, word: str, frequency: int) -> None:
        # Check if word is persian
        if not is_persian_word(word):
            # If not... then raise an exception
            raise NonPersianWordError(f"{word!r} is not a persian word!")

        # Check if word already exists in dictionary
        if word in self:
            # Then set its frequency
            self.set_word_frequency(word, frequency)
        else:
            # Else insert the new word to dictionary with demanded frequency
            self.insert_word(word, frequency)

        # Update dictionary
        self._update_dictionary()

    def __delitem__(self, word: str) -> None:
        # Delete word from dictionary
        self.delete_word(word)

    def _load_dictionary(self) -> None:
        """
        (Private method) Load the dictionary
        """

        # Load dictionary file as GzipFile object
        self._dictionary_readable_gzip_handle = gzip.open(self._dictionary_path, "rt")

        # And read its contents and convert it to a dictionary object
        self._dictionary = json.load(self._dictionary_readable_gzip_handle)

    def _create_a_dictionary_clone(self) -> None:
        """
        (Private method) Create a dictionary clone file (use in case when
        dictionary file doesn't exist)
        """

        # Get the package directory
        package_directory = pathlib.Path(__file__).parent

        # Clone the default dictionary file
        shutil.copyfile(
            package_directory / "fa-dictionary.json.gz", self._dictionary_path
        )

    def _update_dictionary(self) -> None:
        """
        (Private method) Update dictionary
        """

        # Close dictionary gzip file
        self._dictionary_readable_gzip_handle.close()

        # Update dictionary file
        with gzip.open(self._dictionary_path, "wt") as gzip_f:
            json.dump(self._dictionary, gzip_f)

        # Reload dictionary file as GzipFile object
        self._dictionary_readable_gzip_handle = gzip.open(self._dictionary_path, "rt")

    def insert_word(self, word: str, *, frequency: int = 1) -> None:
        """
        Insert a new word to dictionary

        :param word: A persian word to insert to the dictionary
        :type word: str
        :param frequency: The word frequency
        :type frequency: int
        :raises NonPersianWordError: Raise an exception if the word is not a
            persian word
        """

        # Check if word is persian, and if so...
        if is_persian_word(word):
            # Insert the word to dictionary
            self._dictionary[word] = frequency

            # Update the dictionary data
            self._update_dictionary()

            return

        # Raise an exception if the word is not a persian word
        raise NonPersianWordError(f"{word!r} is not a persian word!")

    def set_word_frequency(self, word: str, frequency: int) -> None:
        """
        Sets frequency of a word that already exists in dictionary

        :param word: A persian word to set its frequency
        :type word: str
        :param frequency: The word frequency to set
        :type frequency: int
        :raises WordDoesNotExist: If the word doesn't exist in dictionary
        """

        # If the word is found in dictionary, and if so...
        if word in self:
            # Set word frequency
            self._dictionary[word] = frequency

            # Update the dictionary data
            self._update_dictionary()

            return

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordDoesNotExist(
            f"There is no word {word!r} to set its frequency. "
            "Instead use method `insert_word`"
        )

    def increase_word_frequency(self, word: str, increment: int) -> None:
        """
        Increase frequency of a word that already exists in dictionary

        :param word: A persian word to increase its frequency
        :type word: str
        :param increment: Frequency increment
        :type increment: int
        :raises WordDoesNotExist: If the word doesn't exist in dictionary
        """

        # If the word is found in dictionary, and if so...
        if word in self:
            # Increase word frequency
            self.set_word_frequency(word, self._dictionary[word] + increment)

            return

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordDoesNotExist(
            f"There is no word {word!r} to increase its frequency. "
            "Instead use `insert_word` method!"
        )

    def decrease_word_frequency(self, word: str, decrement: int) -> None:
        """
        Decrease frequency of a word that already exists in dictionary

        :param word: A persian word to decrease its frequency
        :type word: str
        :param decrement: Frequency decrement
        :type decrement: int
        :raises WordDoesNotExist: If the word doesn't exist in dictionary
        """

        # If the word is found in dictionary, and if so...
        if word in self:
            # Decrease word frequency
            self.set_word_frequency(word, self._dictionary[word] - decrement)

            return

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordDoesNotExist(
            f"There is no word {word!r} to decrease its frequency. "
            "Instead use `insert_word` method!"
        )

    def delete_word(self, word: str) -> None:
        """
        Delete a word from dictionary

        :param word: A persian word to delete from the dictionary
        :type word: str
        :raises WordDoesNotExist: If the word doesn't exist in dictionary
        """

        # If the word is found in dictionary, and if so...
        if word in self:
            # Delete the word from dictionary
            self._dictionary.pop(word)

            # Update the dictionary data
            self._update_dictionary()

            return

        # IF THE WORD DOESN'T EXIST IN VOCABULARY, RAISE AN EXCEPTION
        raise WordDoesNotExist(
            f"There is no word {word!r} to remove it from dictionary."
        )
