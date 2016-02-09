-tuple: heterogeneous immutable sequence. once created, objects cannot be replaced or removed, and new elements cannot be added

t = ("Norway", 4.998, 3)
like a list, but "(" instead of "["

-str
-range
-list
-dict
-set

-mutable: CAN be altered
-immutable: CANNOT be changed

TUPLE UNPACKING
>>> lastname = 'Carmichael'
>>> tuple(lastname)
('C', 'a', 'r', 'm', 'i', 'c', 'h', 'a', 'e', 'l')

// CAN RETURN TWO VALUES FROM A FUNCTION
>>> def two_rtns():
...     return 76, 89
... 
>>> x, y = two_rtns()
>>> x
76
>>> y
89

// BUILT IN MIN AND MAX FUNCTIONS

>>> list = [3,4,5,6]
>>> min(list)
3
>>> max(list)
6
>>> tlist = (3,4,5,6)
>>> min(tlist)
3
>>> max(tlist)
6

// TUPLE / LIST FOR CONTAINMENT WITH 'IN' OR 'NOT IN' OPERATIOR
>>> lastname = 'Carmichael'
>>> tuple(lastname)
('C', 'a', 'r', 'm', 'i', 'c', 'h', 'a', 'e', 'l')
>>> j=tuple(lastname)
>>> j
('C', 'a', 'r', 'm', 'i', 'c', 'h', 'a', 'e', 'l')
>>> 'a' in lastname
True
>>> 'x' in lastname
False
>>> 5 in (8,7,6)
False
>>> 6 in [6,7,7]
True
>>> 6 not in [6,7,7]
False
