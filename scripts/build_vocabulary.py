"""
The script that used to build vocabularies with word frequency
"""

import gzip
import json
from pathlib import Path

from faspellchecker.utils import is_persian_word

# Find `fa-spellchecker/resources` folder
vocabulary_resources = Path("resources/")

collected_contents = []

# Get all resources from the `fa-spellchecker/resources` folder
for resource in vocabulary_resources.glob("./*"):
    # Open and read resource file
    with open(resource) as f:
        # And add the content of resource file to `collected_contents`
        collected_contents.append(f.read())

# Convert `collected_contents` into a string of words those were collected from resources
collected_contents = "\n".join(collected_contents)

vocabulary_json = {}

# Split collected contents into a list of words
for word in collected_contents.split():
    # If the word is already in `vocabulary_json`, then just increase its frequency
    if word in vocabulary_json:
        vocabulary_json[word] = vocabulary_json[word] + 1

        continue

    # If not, then check if the word is a persian word
    if is_persian_word(word):
        # If it's, then add it to `vocabulary_json`
        vocabulary_json[word] = 1

# Then open a gzip-compressed file
vocabulary_gzip_file = gzip.open("faspellchecker/fa-vocabulary.json.gz", "wt")

# Then save collected words into it!
json.dump(vocabulary_json, vocabulary_gzip_file)
