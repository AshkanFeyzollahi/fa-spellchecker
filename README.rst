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

**fa-spellchecker** only supports the Persian language! and it requires `Python>=3.7` to work properly. For information on how the Persian vocabulary was created and how it can be updated and improved, please see the **Vocabulary Creation and Updating** section of the readme!

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

Vocabulary Creation and Updating
-------------------------------------------------------------------------------

The creation of the vocabulary is, unfortunately, not an exact science. I have provided a script that, given a text file of words & sentences (in this case from the txt files in the folder `resources <resources/>`__) it will generate a *Persian* word frequency list based on the words found within the text.

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
