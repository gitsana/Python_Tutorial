str: homogeneous immutable sequence of Unicode codepoints (characters)

>>> len("llannfair")
9
>>> "new" + "found" + "land"
'newfoundland'
>>> s = "new"
>>> s += "found"
>>> s += "land"
>>> s
'newfoundland'

--- PREFERRED METHOD OF CONCATENATION STRING IS 'JOIN' METHOD ---

>>> colors = ','.join(['red','blue','yellow','green'])
>>> colors
'red,blue,yellow,green'
>>> colors.split(',')
['red', 'blue', 'yellow', 'green']
>>> ''.join(['jum','bo','jack'])
'jumbojack'

--- PARTITION METHOD ---

>>> "unforgetable".partition("forget")
('un', 'forget', 'able')
>>> 
>>> departure, separator, arrival = "London:Edinburgh".partition(':')
>>> departure
'London'
>>> arrival
'Edinburgh'
>>> separator
':'
>>> 
>>> origin, _, destination = "Seattle-Boston".partition("-")
>>> origin
'Seattle'
>>> destination
'Boston'
>>> _
'-'

---- FORMAT METHOD ----
>>> "The age of {0} is {1}".format('Jim',21)
'The age of Jim is 21'
>>> "The age of {} is {}".format('Jim',21)
'The age of Jim is 21'
>>> 
>>> "Current position is {latitude} {longitude}.".format(latitude="60N", longitude="5E")
'Current position is 60N 5E.'
>>> 
>>> "The age of {0} is {1}. {0}'s birthday is on {2}. {2} is also {0}'s sister's birthday!".format('Jim',21,'October 31st')
"The age of Jim is 21. Jim's birthday is on October 31st. October 31st is also Jim's sister's birthday!"
>>> 
>>> pos = (65.2, 23.1, 82.2)
>>> "Galactic position... x={p[0]} , y={p[1]} , z={p[2]}".format(p=pos)
'Galactic position... x=65.2 , y=23.1 , z=82.2'

>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> "Math constants: pi = {m.pi}, e = {m.e}".format(m=math)
'Math constants: pi = 3.141592653589793, e = 2.718281828459045'
>>> "Math constants: pi = {m.pi:.3f}, e = {m.e:.3f}".format(m=math)
'Math constants: pi = 3.142, e = 2.718' # formatted 3 decimal places





























