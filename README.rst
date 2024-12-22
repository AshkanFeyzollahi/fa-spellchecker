Persian SpellChecker
===============================================================================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/
    :alt: License
.. image:: https://img.shields.io/github/v/release/AshkanFeyzollahi/fa-spellchecker
    :target: https://github.com/AshkanFeyzollahi/fa-spellchecker/releases/
    :alt: GitHub Release
.. image:: https://img.shields.io/pypi/v/fa-spellchecker
    :target: https://pypi.org/project/fa-spellchecker/
    :alt: PyPI - Version
.. image:: https://img.shields.io/pypi/dm/fa-spellchecker
    :target: https://pypi.org/project/fa-spellchecker/
    :alt: PyPI - Downloads
.. image:: https://img.shields.io/readthedocs/fa-spellchecker
    :target: https://fa-spellchecker.readthedocs.io/en/latest/
    :alt: Read the Docs

Pure Python Persian Spell Checking based on `Peter Norvig's blog post <https://norvig.com/spell-correct.html>`__ on setting up a simple spell checking algorithm and also inspired by `pyspellchecker <https://github.com/barrust/pyspellchecker>`__.

As said in **pyspellchecker**, It uses a Levenshtein Distance algorithm to find permutations within an edit distance of 2 from the original word. It then compares all permutations (insertions, deletions, replacements, and transpositions) to known words in a word frequency list. Those words that are found more often in the frequency list are more likely the correct results.

**fa-spellchecker** is **ONLY** made for the language **Persian**, and it requires `Python>=3.7` to work properly. For information on how the Persian vocabulary was created and how it can be updated and improved, please see the **Vocabulary Creation and Updating** section of the readme!

Installation
-------------------------------------------------------------------------------

.. warning::

    When installing **fa-spellchecker**, always prefer latest version or v0.1.2 and later.

To start using **fa-spellchecker** in your Python3 projects, you have to install it which is done by ways below:

    1. Package could be installed by using the python package manager **Pip**:

    .. code:: bash

        pip install fa-spellchecker

    2. Building package from its source:

    .. code:: bash

        git clone https://github.com/AshkanFeyzollahi/fa-spellchecker.git
        cd fa-spellchecker
        python -m build


Quickstart
-------------------------------------------------------------------------------

To get started using **fa-spellchecker**, you must install it, if it's not installed already check the **Installation** section in readme! Here are some examples for **fa-spellchecker**:

    1. A simple Persian word correction example:

    .. code:: python

        # Import SpellChecker object from faspellchecker
        from faspellchecker import SpellChecker

        # Initialize a faspellchecker.SpellChecker instance
        spellchecker = SpellChecker()

        # Correct the Persian misspelled word
        print(spellchecker.correction('سابون')) # 'صابون'

    2. An advanced correction for Persian words found in a sentence with the help of `hazm <https://github.com/roshan-research/hazm>`__:

    .. code:: python

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

For more information on how to use this package, check out `On-line documentations <https://fa-spellchecker.readthedocs.io/en/latest/>`__!

Vocabulary Creation and Updating
-------------------------------------------------------------------------------

I have provided a script that, given a text file of words & sentences (in this case from the txt files in the folder `resources <resources/>`__) it will generate a *Persian* word frequency list based on the words found within the text.

Adding new files to `resources <resources/>`__ will lead to force the `scripts/build_vocabulary.py` to use them as a resource to build a Persian vocabulary file which then that vocabulary file will be used by `faspellchecker`.

The easiest way to build Persian vocabulary files using the `scripts/build_vocabulary.py`:

.. code:: bash

    git clone https://github.com/AshkanFeyzollahi/fa-spellchecker.git
    cd fa-spellchecker
    python scripts/build_vocabulary.py

Any help in updating and maintaining the vocabulary would be greatly desired. To do this, a `discussion <https://github.com/AshkanFeyzollahi/fa-spellchecker/discussions>`__ could be started on GitHub or pull requests to update the include and exclude files could be added.

Credits
-------------------------------------------------------------------------------

* `Peter Norvig <https://norvig.com/spell-correct.html>`__ blog post on setting up a simple spell checking algorithm.
* `persiannlp/persian-raw-text <https://github.com/persiannlp/persian-raw-text>`__ Contains a huge amount of Persian text such as Persian corpora. VOA corpus was collected from this repository in order to create a word frequency list!
