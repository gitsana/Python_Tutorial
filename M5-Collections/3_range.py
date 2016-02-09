range: arithmetic progression of integers. iterable.

>>> t = [6, 10, 35, 22]
>>> for p in enumerate(t):
...     print(p)
... 
(0, 6)
(1, 10)
(2, 35)
(3, 22)

>>> for i, v in enumerate(t):
...    print("i={},v={}".format(i,v))
... 
i=0,v=6
i=1,v=10
i=2,v=35
i=3,v=22

>>> for i in range(5,20,3):
...     print(i)
... 
5
8
11
14
17
