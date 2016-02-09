
- Not variables but "named references to objects" in Python
- even adding two numbers (like x = 5, then x += 2) is assigning pointer to new total and garbage collecting 5 and 2, and x points to 7
- everything is immutable
>> x = 10
>> y = x
this means both are pointing to "10"
can do 
>> id(x) 
or 
>> id(y) 
and they will both return same id since they're equal

VALUE EQUALITY VS. IDENTITY EQUALITY --- P and Q are not equal!
>>> p = [1,4,7]
>>> q = [1,4,7]
>>> p == q
True
>>> p is p
True
>>> p is q
False
>>> id(p)
4313704008
>>> id(q)
4313704264
>>> 

if you want a function to modify a COPY of an object, it's the responsibility of the function to do the copying -- otherwise it will modify the actual object itself. example:

>>> m = [9,15,24]
>>> def modify(k):
...     k.append(3900)
...     print("k = ", k)
... 
>>> modify(m)
k =  [9, 15, 24, 3900]
>>> 

clearing the screen
>> import os
>> os.system('clear')
OR
>> def clear(): os.system('clear')
..
>> clear()
------------------------------------------------------------------------
# message is positional, border is keyword (optional, so you can but don't have to include it) -- but all positional vars must go before keyword args
>>> def banner(message, border='-'):
...     line = border * len(message)
...     print(line)
...     print(message)
...     print(line)
>>> banner("Results are below")
-----------------
Results are below
-----------------
>>> banner("From Mars to Venus",'#')
##################
From Mars to Venus
##################


------------------------------------------------------------------------
pass by REFERENE (pointers) to the object, NOT by copying VALUES of the opject
------------------------------------------------------------------------
TYPE SYSTEMS - not defined until runtime

>>> def add(a, b):
...     return a + b
... 
>>> add(5, 7)
12
>>> add(3.1, 2.4)
5.5
>>> add("news", "paper")
'newspaper'
>>> add([1,3], [2,4])
[1, 3, 2, 4]
>>> 

------------------------------------------------------------------------
Python Name Scopes

Local - Inside the current function
Enclosing -	Any and all enclosing functions
Global - Top-level of module
Built-in - provided by the "builtins" module

------------------------------------------------------------------------
// scopes.py is a file
>>> import scopes
>>> type(scopes)
<class 'module'>
>>> dir(scopes)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'count', 'set_count', 'show_count']
>>> type(scopes.show_count)
<class 'function'>
>>> dir(scopes.show_count)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> scopes.show_count.__module__
'scopes'
>>> scopes.show_count.__name__
'show_count'
>>> scopes.show_count.__str__
<method-wrapper '__str__' of function object at 0x1013dba60>
>>> scopes.__doc__
'Demonstrate scoping'

------------------------------------------------------------------------
------------------------------------------------------------------------

























