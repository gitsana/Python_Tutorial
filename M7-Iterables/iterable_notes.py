# generators
>>> def gen123():
...     yield 1
...     yield 2
...     yield 3
... 
>>> gen1 = gen123()
>>> next(gen1)
1
>>> next(gen1)
2
>>> next(gen1)
3

>>> t = gen123()
>>> for i in t:
...     print (i)
... 
1
2
3
>>> 

# prints UPTO and INCLUDING the yield
>>> def gen246():
...     print("About to yield 2")
...     yield 2
...     print("About to yield 4")
...     yield 4
...     print("About to yield 6")
...     yield 6
... 
>>> mygen = gen246()
>>> next(mygen)
About to yield 2
2
>>> next(mygen)
About to yield 4
4
>>> next(mygen)
About to yield 6
6
