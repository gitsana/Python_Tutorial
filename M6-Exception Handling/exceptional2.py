'''A module for demo-ing exceptions'''
import sys
from math import log

def convert_to_int(s):
	x = -1
	try:
		return int(s)
		print("Conversion succeeded! x =", x)
	except (ValueError,TypeError) as e:
		print("Conversion error: {}".format(str(e)), file=sys.stderr)
		return -1

def string_log(s):
	v = convert_to_int(s)
	return log(v)

def square_root(x):
	guess = x
	i = 0

	while guess * guess != x and i < 20:
		guess = (guess + x / guess) / 2.0
		i += 1
	return guess

def main():
	print(square_root(9))
	print(square_root(2))
	print(square_root(64))
	try:
		print(square_root(-1))
	except ZeroDivisionError:
		print("Cannot compute the square_root of a negative numero")
	print("Program execution continues normally here")

if __name__ == '__main__':
	main()