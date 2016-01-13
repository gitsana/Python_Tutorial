
# collections:
# str, bytes, list, dict

######### STRINGS ############

"first" "second" # returns string 'firstsecond'

# multi line strings
# way 1 -- 3 double quotes
"""This is a multi
line
string"""

# way 2 -- 3 single quotes
'''This is a multi
line
string'''

# way 3 - escape chars
m = 'This string\nspans\nmultiple lines'


mystr = 'parrot'
mystr[5] # 't'
help(str)
mystr.capitalize() # prints, but is immutable
mystr2 = mystr.capitalize()

######### LISTS ############

mylist = []
mylist.append(1.68)

intlist = [1, 4, 21, 78]
strlist = ['apple', 'orange', 'yellow']
mixlist = ['hi', 21.43, 16, True]

charlist = list('listofchars') # creates list of CHARS

######## DICT #############
# key-value pairs
d1 = {'alice':'A+','charlie':'D', 'bob':'C+', 'jack':'B-' }
d1['MARIGOLD'] = 'B+' # add new
d1['alice'] = 'A-'	# change existing

emptylist = {}















