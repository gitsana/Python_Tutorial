'''A module for demo-ing exceptions'''

def convert_to_int(s):
	try:
		x = int(s)
		print("Conversion succeeded! x =", x)
	except ValueError:
		x = -1
		print("Conversion failed - ValueError")
	except TypeError:
		x = -2
		print("Conversion failed - TypeError")
	return x