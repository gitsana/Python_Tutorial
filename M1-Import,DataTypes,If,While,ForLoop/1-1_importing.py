import this
import math
from math import factorial

help(math)
help(math.factorial)
help(math.pow)

for i in range(10):
	print(2**i)

for i in range(10):
	print(pow(2,i))


# types: int, float, bool

# convert string to int
int('456')

# convert int to float
float(7)

float("nan")

# null value is None in python (case sensitive)
a = None
a is None # this prints 'True'

# bools: 0 is false-y, all other values are truth-y
bool(0.0) 	# False
bool(42) 	# True
bool(-1)	# True