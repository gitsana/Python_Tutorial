# this is stored as bytes
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
	story_words = []
	for line in story:
		line_words = line.split() # not decoding the bytes into strings
		for word in line_words:
			story_words.append(word)

# this is stored as strings
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
	story_words = []
	for line in story:
		line_words = line.decode('utf-8').split()	# difference here: decoding the bytes
		for word in line_words:
			story_words.append(word)


# Putting it all together:
# * urllib.urlopen()
# * with-statement
# * list
# * for-loop
# * bytes.split()
# * bytes.decode()
# * str.split()
