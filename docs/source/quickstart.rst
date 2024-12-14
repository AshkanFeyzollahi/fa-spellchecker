Quickstart
===============================================================================

**fa-spellchecker** is designed to be easy to use to get basic spell checking.

Installation
-------------------------------------------------------------------------------

The easiest and recommended way to install is using **Pip**:

.. code:: bash

    pip install fa-spellchecker

But to build it from its source:

.. code:: bash

    git clone https://github.com/AshkanFeyzollahi/fa-spellchecker.git
    cd fa-spellchecker
    python -m build

Basic Usage
-------------------------------------------------------------------------------

Spell checker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting up the spell checker requires importing and initializing the instance.

.. code:: python

    from faspellchecker import SpellChecker

    spellchecker = SpellChecker()

Ways to check if a word is in the vocabulary:

.. code:: python

    from faspellchecker import SpellChecker

    spellchecker = SpellChecker()

    'سلام' in spellchecker.vocabulary # True

    # find those words from a list of words that are found in the vocabulary
    spellchecker.known(['صابون', 'سابون']) # {'صابون'}

    # find those words from a list of words that are not found in the vocabulary
    spellchecker.known(['صابون', 'سابون']) # {'سابون'}

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

Vocabulary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vocabulary is where you can add, remove & etc. words to spell checker. Actually there are many other usages which can be found at below!

Initializing a vocabulary object to use with spell checker or using default vocabulary that come with spell checker itself:

.. code:: python

    from faspellchecker import SpellChecker, Vocabulary

    # Initializing vocabulary separately
    vocabulary = Vocabulary("example-vocabulary")

    spellchecker1 = SpellChecker(vocabulary)

    # Or getting default vocabulary object from spellchecker
    spellchecker2 = SpellChecker()

    vocabulary = spellchecker2.vocabulary

Adding new words/terms to vocabulary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the vocabulary
    vocabulary = spellchecker.vocabulary

    # Add the word you wish to add, by the way frequency field is optional!
    vocabulary.insert_word("اشکان", frequency=90)

    # Now test it!
    "اشکان" in vocabulary # True

Removing words/terms from vocabulary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the vocabulary
    vocabulary = spellchecker.vocabulary

    # Add the word you wish to add
    vocabulary.delete_word("درخت")

    # Now test it!
    "درخت" in vocabulary # False

Setting a new frequency to words in vocabulary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the vocabulary
    vocabulary = spellchecker.vocabulary

    # Test a correction
    spellchecker.correction("سللم") # 'سالم'

    # Set the frequency of the word
    vocabulary.set_word_frequency("سلام", 9999)

    # Now test the correction again
    spellchecker.correction("سللم") # 'سلام'

Increasing frequency of words in vocabulary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the vocabulary
    vocabulary = spellchecker.vocabulary

    # Test a correction
    spellchecker.correction("سللم") # 'سالم'

    # Increase the frequency of the word
    vocabulary.increase_word_frequency("سلام", 9999)

    # Now test the correction again
    spellchecker.correction("سللم") # 'سلام'

Decreasing frequency of words in vocabulary:

.. code:: python

    from faspellchecker import SpellChecker

    # Initialize spellchecker
    spellchecker = SpellChecker()

    # Get the vocabulary
    vocabulary = spellchecker.vocabulary

    # Test a correction
    spellchecker.correction("سللم") # 'سالم'

    # Increase the frequency of the word
    vocabulary.decrease_word_frequency("سالم", 9999)

    # Now test the correction again
    spellchecker.correction("سللم") # maybe 'سلام' or something else than 'سالم'
