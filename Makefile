#
# A simple Makefile for testing, formating, building dictionary and etc.
#

test:
	python -m unittest discover -s tests -p *test.py

format:
	isort .
	black .

build_dictionary:
	python scripts/build_dictionary.py

dev_dependencies:
	pip install fa-spellchecker[dev]
