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
.. image:: https://img.shields.io/readthedocs/fa-spellchecker
    :target: https://fa-spellchecker.readthedocs.io/en/latest/
    :alt: Read the Docs

Pure Python Persian Spell Checking based on `Peter Norvig's blog post <https://norvig.com/spell-correct.html>`__ on setting up a simple spell checking algorithm and also inspired by `pyspellchecker <https://github.com/barrust/pyspellchecker>`__.

As said in **pyspellchecker**, It uses a Levenshtein Distance algorithm to find permutations within an edit distance of 2 from the original word. It then compares all permutations (insertions, deletions, replacements, and transpositions) to known words in a word frequency list. Those words that are found more often in the frequency list are more likely the correct results.

**fa-spellchecker** is specially made for persian language! And, **fa-spellchecker** only supports **Python>=3.7**!

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


Quickstart
-------------------------------------------------------------------------------

A great example to start using **fa-spellchecker**:

.. code:: python

    from faspellchecker import SpellChecker

    spellchecker = SpellChecker()

    spellchecker.correction('سابون') # 'صابون'

For more information on how to use this package, check out `On-line documentations <https://fa-spellchecker.readthedocs.io/en/latest/>`__ about quick start!

Credits
-------------------------------------------------------------------------------

* `Peter Norvig <https://norvig.com/spell-correct.html>`__ blog post on setting up a simple spell checking algorithm.
* `persiannlp/persian-raw-text <https://github.com/persiannlp/persian-raw-text>`__ Contains a huge amount of Persian text such as Persian corpora. VOA corpus was collected from this repository in order to create a word frequency list!
