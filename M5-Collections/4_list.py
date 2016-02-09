list: heterogeneous mutable sequence

>>> s = "show how to index into sequences".split(" ")
>>> s
['show', 'how', 'to', 'index', 'into', 'sequences']
>>> slice1 = s[2:5]
>>> slice1
['to', 'index', 'into']
>>> fullstr = ' '.join(s)
>>> fullstr
'show how to index into sequences'
>>> len(fullstr)
32

'''negative indexing'''
>>> print(s[-1])
sequences
>>> s[-6]
'show'
>>> s[1:-1]
['how', 'to', 'index', 'into']
>>> s[:3]
['show', 'how', 'to']
>>> s[3:]

# method to copy full list
['index', 'into', 'sequences']
>>> full_slice = s[:]
>>> full_slice
['show', 'how', 'to', 'index', 'into', 'sequences']

# other methods to copy list
>>> f = s.copy()
>>> f
['show', 'how', 'to', 'index', 'into', 'sequences']
>>> 

# find element in a list, then use that index to find that element by index
>>> mylist = "the quick brown fox jumped over the moon".split()
>>> mylist
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'moon']
>>> ind = mylist.index('jumped')
>>> ind
4
>>> mylist[ind]
'jumped'
# count occurrences in a list
>>> mylist.count('the')
2
# test for membership or non-membership
>>> mylist
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'moon']
>>> 'brown' in mylist
True
>>> 'factory' in mylist
False
>>> 'factory' not in mylist
True
# remove elements from list: "del" and "remove"
>>> mylist
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'moon']
>>> del mylist[2]
>>> mylist
['the', 'quick', 'fox', 'jumped', 'over', 'the', 'moon']
>>> mylist.remove('the')
>>> mylist
['quick', 'fox', 'jumped', 'over', 'the', 'moon']	# only removed first one
# using both del and index together
>>> mylist
['quick', 'fox', 'jumped', 'the', 'moon']
>>> del mylist[mylist.index('moon')]
>>> mylist
['quick', 'fox', 'jumped', 'the']
>>> 

# insert into list: seq.insert(index,item)

>>> stmt = 'I think I my rocket'.split()
>>> stmt
['I', 'think', 'I', 'my', 'rocket']
>>> stmt.insert(3, 'launched')
>>> stmt
['I', 'think', 'I', 'launched', 'my', 'rocket']
>>> ' '.join(stmt)
'I think I launched my rocket'

# extending lists

>>> m = [1,2,3]
>>> n = [11,22,33]
>>> k = m + n 	# simply add them
>>> k
[1, 2, 3, 11, 22, 33]
>>> k += 17
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> k += [17]	# the '+=' operator
>>> k
[1, 2, 3, 11, 22, 33, 17]
>>> k.extend[18]		# extend method
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> k.extend([18])
>>> k
[1, 2, 3, 11, 22, 33, 17, 18]
>>> 

# reverse a list
>>> m
[1, 2, 3]
>>> m.reverse()
>>> m
[3, 2, 1]
>>> 

# sort a list
>>> j = [33, 24, 1, 75, 800, 2, -8]
>>> j.sort()
>>> j
[-8, 1, 2, 24, 33, 75, 800]

# sort a list in reverse
>>> j = [33, 24, 1, 75, 800, 2, -8]
>>> j
[33, 24, 1, 75, 800, 2, -8]
>>> j.sort(reverse=True)
>>> j
[800, 75, 33, 24, 2, 1, -8]
>>> 

# sort by key on a callable function of the list items, in this case 'len'
# ordering by smallest to largest
>>> h = 'Jerry said all fabulous things in onomatopoeia rabidly I think'.split()
>>> h
['Jerry', 'said', 'all', 'fabulous', 'things', 'in', 'onomatopoeia', 'rabidly', 'I', 'think']
>>> h.sort(key=len)
>>> h
['I', 'in', 'all', 'said', 'Jerry', 'think', 'things', 'rabidly', 'fabulous', 'onomatopoeia']

# using both key and reverse
>>> h
['Jerry', 'said', 'all', 'fabulous', 'things', 'in', 'onomatopoeia', 'rabidly', 'I', 'think']
>>> h.sort(key=len,reverse=True)
>>> h
['onomatopoeia', 'fabulous', 'rabidly', 'things', 'Jerry', 'think', 'said', 'all', 'in', 'I']
>>> 

# assigning sorted list to other var, without sorting the list itself
>>> f = [4, 55, 3]
>>> f
[4, 55, 3]
>>> y = sorted(f)
>>> y
[3, 4, 55]
>>> f
[4, 55, 3]
>>> 

# same with reverse
>>> p = [9,3,4,1]
>>> p
[9, 3, 4, 1]
>>> q = reversed(p) # figure out how to print out in python3?





































