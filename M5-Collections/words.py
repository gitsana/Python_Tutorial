#!/usr/bin/env python3
#shebang
# indent with 4 spaces
# save with UTF-8 encoding
""" Retrieve and print words from a URL.
Usage: python3 words.py <URL>
"""
from urllib.request import urlopen

def fetch_words():
	"""Fetch a list of words from a URL.

	Args:
		url: The URL of a UTF-8 text document

	Returns: 
		A list of strings containing the words from the document
	"""
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
			line_words = line.decode('UTF-8').split()
			for word in line_words:
				story_words.append(word)

def print_words(story_words):
	""" print items one per line

	Args: an iterable series of printable items

	Returns: Nothing
	"""
	paragraph = ""
	for word in story_words:
		paragraph = paragraph + word + " "
	print("--------------PRINT WORDS FUNCTION--------------",paragraph)

def main():
	words = fetch_words()
	print_words(words)

print(__name__)
if __name__ == '__main__':
	main()

# to execute from REPL: 
	# >> python3 words.py
# import "words.py" to REPL: 
	# >> python3
	# >> import words
	# >> words.fetch_words()
# import function "fetch_words()" from "words.py" to REPL and execute:
	# >> python3
	# >> from words import fetch_words
	# >> fetch_words()
# >> from words import(fetch_words,print_words)

####### docstrings
# >>> from words import *
# words
# >>> help(fetch_words)

####### docstrings for whole program
# $ python3
# >>> import words
# words
# >>> help(words)

# python module: convenient import with API
# python script: convenient execution from cmd line
# python program: composed of many modules







