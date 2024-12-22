# Import dependencies
from hazm import word_tokenize

from faspellchecker import SpellChecker

# Define a sentence of Persian words
a_persian_sentence = "من به پارک رفتم و در آنجا با دوشت هایم بازی کردم"

# Tokenize the sentence into a list of words
tokenized_sentence = word_tokenize(a_persian_sentence)

# Initialize a faspellchecker.SpellChecker instance
spellchecker = SpellChecker()

# Find all misspelled words
for misspelled_word in spellchecker.unknown(tokenized_sentence):
    # And display a list of correct words based on misspelled word
    print(spellchecker.candidates(misspelled_word))
