# Import dependencies
from hazm import word_tokenize

from faspellchecker import SpellChecker
from faspellchecker.utils import ignore_non_persian_words

# Define a sentence of Persian words
a_persian_sentence = "من به پارک رفتم و در آنجا با دوشت هایم بازی کردم"

# Tokenize the sentence into a list of words
tokenized_sentence = word_tokenize(a_persian_sentence)

# Ignore the non Persian words (in this case there are no non Persian words
# based on function `is_word_persian`, so this line will return the give list
# itself)
tokenized_sentence = ignore_non_persian_words(tokenized_sentence)

# Initialize a faspellchecker.SpellChecker instance
spellchecker = SpellChecker()

# Find all misspelled words
for misspelled_word in spellchecker.unknown(tokenized_sentence):
    # And display a list of correct words based on misspelled word
    print(spellchecker.candidates(misspelled_word))
