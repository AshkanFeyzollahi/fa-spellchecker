#
# fa-spellchecker documentation build configuration file
#

import os
import sys

sys.path.insert(0, os.path.abspath("../../"))
from faspellchecker import __author__, __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]

source_suffix = ".rst"

master_doc = "index"

project = "fa-spellchecker"
copyright = "2024, {}".format(__author__)
author = __author__

version = __version__
release = __version__

language = "en"

exclude_patterns = []

pygments_style = "sphinx"

todo_include_todos = True

html_theme = "alabaster"

html_sidebars = {
    "**": [
        "relations.html",
        "searchbox.html",
    ]
}

htmlhelp_basename = "fa-spellchecker-doc"

latex_elements = {}

latex_documents = [
    (
        master_doc,
        "fa-spellchecker.tex",
        "fa-spellchecker Documentation",
        author,
        "manual",
    ),
]

man_pages = [
    (master_doc, "fa-spellchecker", "fa-spellchecker Documentation", [author], 1)
]

texinfo_documents = [
    (
        master_doc,
        "fa-spellchecker",
        "fa-spellchecker Documentation",
        author,
        "fa-spellchecker",
        "Pure Python Persian Spell Checker.",
        "Miscellaneous",
    ),
]
