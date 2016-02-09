Common exceptions-use when possible, instead of making your own:
IndexError: index is out of range
KeyError: lookup in mapping fails - lookup of non-existant key is mapping
ValueError: object is of the right type, but contain an inappropriate value 
	(such as when trying to convert to 'int' type from a non-numeric string)
TypeError: tend not to guard against these in Python bc limits reuse potential of code
	usually not worth checking for types

	"Ask for forgiveness rather than permission" is preferred rather than the 
	"Look before you leap" philosophy -- so no checks whether it's the right type, 
	file exists, etc -- just let it flow and if something goes wrong exception handles it

Programmer errors such as indendation or syntax errors should not normally be handled
Exceptional conditions can be signaled using the raise keyword.
	raise WITHOUT an argument re-raises the current exception
# try-finally
# finally gets executed NO MATTER HOW the try-block exits
import os
import sys

def make_at(path, dir_name):
	original_path = os.getcwd()
	try:
		os.chdir(path)
		os.mkdir(dir_name)
	except OSError as e:
		print(e, file=sys.stderr)
		raise
	finally:
		os.chdir(original_path) #final dir change back will take place in all circumstances


