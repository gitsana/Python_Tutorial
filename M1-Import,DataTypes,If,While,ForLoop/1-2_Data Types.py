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
bool([])	# False (empty list)
bool([1,2,4])	# True (not empty list)
bool("")	# False
bool("x")	# True
bool("False")	# True -- be careful!
