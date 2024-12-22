# Import SpellChecker object from faspellchecker
from faspellchecker import SpellChecker

# Initialize a faspellchecker.SpellChecker instance
spellchecker = SpellChecker()

# Correct the Persian misspelled word
print(spellchecker.correction("سابون"))  # 'صابون'
