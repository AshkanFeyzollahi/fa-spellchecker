Quickstart
===============================================================================

**fa-spellchecker** is designed to be easy to use to get basic spell checking.

Basic Usage
-------------------------------------------------------------------------------

Spell checker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting up the spell checker requires importing and initializing the instance.

.. code:: python

    from faspellchecker import SpellChecker

    spellchecker = SpellChecker()

Ways to check if a word is in the dictionary:

.. code:: python

    from faspellchecker import SpellChecker

    spellchecker = SpellChecker()

    'سلام' in spellchecker.dictionary # True

    # find those words from a list of words that are found in the dictionary
    spellchecker.known(['صابون', 'سابون']) # {'صابون'}

    # find those words from a list of words that are not found in the dictionary
    spellchecker.unknown(['صابون', 'سابون']) # {'سابون'}

Once a word is identified as misspelled, you can find the likeliest replacement:

.. code:: python

    from spellchecker import SpellChecker

    spellchecker = SpellChecker()

    misspelled = spell.unknown(['صابون', 'سابون'])  # {'سابون'}

    for word in misspelled:
        spellchecker.correction(word)  # 'صابون'

Or if the word identified as the likeliest is not correct, a list of candidates can also be pulled:

.. code:: python

    from spellchecker import SpellChecker

    spellchecker = SpellChecker()

    misspelled = spell.unknown(['صابون', 'سابون'])  # {'سابون'}

    for word in misspelled:
        spellchecker.candidates(word)  # {'مابون', 'سابو', 'ساسون', 'تابون', 'صابون', 'گابون', 'سالون'}

Dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dictionary is where you can add, remove & etc. words to spell checker. Actually there are many other usages which can be found at below!

Initializing a dictionary object to use with spell checker or using default dictionary that come with spell checker itself:

.. code:: python

    from faspellchecker import SpellChecker, Dictionary

    # Initializing dictionary separately
    dictionary = Dictionary("example-dictionary")

    spellchecker1 = SpellChecker(dictionary)

    # Or getting default dictionary object from spellchecker
    spellchecker2 = SpellChecker()

    dictionary = spellchecker2.dictionary

Adding new words/terms to dictionary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the dictionary
    dictionary = spellchecker.dictionary

    # Add the word you wish to add, by the way frequency field is optional!
    dictionary.insert_word("اشکان", frequency=90)

    # Now test it!
    "اشکان" in dictionary # True

Removing words/terms from dictionary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the dictionary
    dictionary = spellchecker.dictionary

    # Add the word you wish to add
    dictionary.delete_word("درخت")
    # equivalent: del dictionary["درخت"]

    # Now test it!
    "درخت" in dictionary # False

Setting a new frequency to words in dictionary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the dictionary
    dictionary = spellchecker.dictionary

    # Test a correction
    spellchecker.correction("سللم") # 'سالم'

    # Set the frequency of the word
    dictionary.set_word_frequency("سلام", 9999)
    # equivalent: dictionary["سلام"] = 9999

    # Now test the correction again
    spellchecker.correction("سللم") # 'سلام'

Increasing frequency of words in dictionary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the dictionary
    dictionary = spellchecker.dictionary

    # Test a correction
    spellchecker.correction("سللم") # 'سالم'

    # Increase the frequency of the word
    dictionary.increase_word_frequency("سلام", 9999)
    # equivalent: dictionary["سلام"] += 9999

    # Now test the correction again
    spellchecker.correction("سللم") # 'سلام'

Decreasing frequency of words in dictionary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the dictionary
    dictionary = spellchecker.dictionary

    # Test a correction
    spellchecker.correction("سللم") # 'سالم'

    # Increase the frequency of the word
    dictionary.decrease_word_frequency("سالم", 9999)
    # equivalent: dictionary["سالم"] -= 9999

    # Now test the correction again
    spellchecker.correction("سللم") # maybe 'سلام' or something else than 'سالم'
