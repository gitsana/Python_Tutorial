set: unordered collection of unique, immutable objects. unordered.
- like a dict, is curly-braced but not key-val pairs
- create an empty set with set()

>>> myset = {6, 6, 7}
>>> myset
{6, 7}
>>> type(myset)
<class 'set'>
>>> emptyset = set()
>>> emptyset
set()
>>> 

# also create set with set constructor
>>> mylist = [2,2,4,5,6,4,7,3,3]
>>> myset = set(mylist)
>>> mylist
[2, 2, 4, 5, 6, 4, 7, 3, 3]
>>> myset
{2, 3, 4, 5, 6, 7}
>>> 
# iterable
>>> for i in myset:
...     print(i)
... 
2
3
4
5
6
7

# membership
>>> 3 in myset
True
>>> 4 not in myset
False

# add element to set
>>> myset.add(54)
>>> myset
{2, 3, 4, 5, 6, 7, 54}
>>> 

# add a list or another set
>>> myset.update([74,75])
>>> myset
{2, 3, 4, 5, 6, 7, 74, 75, 54}
>>> myset2 = {9.55, 7.223}
>>> myset.update(myset2)
>>> myset
{2, 3, 4, 5, 6, 7, 7.223, 9.55, 74, 75, 54}
>>> 

# removing elems
>>> myset.remove(7)	# error if not there already
>>> myset
{2, 3, 4, 5, 6, 7.223, 9.55, 74, 75, 54}
>>> myset.discard(2) # less fussy no error
>>> myset
{3, 4, 5, 6, 7.223, 9.55, 74, 75, 54}
>>> 

# making copies (shallow copy)
# copy function
>>> myset = {'orchid','orange blossom','freesia'}
>>> myset
{'orange blossom', 'freesia', 'orchid'}
>>> flower_set = myset.copy()
>>> flower_set
{'orange blossom', 'freesia', 'orchid'}
>>> 
# constructor method
>>> flower_power = set(flower_set)
>>> flower_power
{'orange blossom', 'freesia', 'orchid'}
>>> 

# set algebra
# union - all elements in both sets, even if not in other set. COMMUTATIVE
>>> iphone_apps = {'twitter','facebook','coffee_bagel','weather_channel'}
>>> android_apps = {'twitter','angry_birds','facebook'}
>>> iphone_apps.union(android_apps)
{'weather_channel', 'coffee_bagel', 'angry_birds', 'facebook', 'twitter'}

# intersection - present in both sets. COMMUTATIVE
>>> iphone_apps.intersection(android_apps)
{'facebook', 'twitter'}
>>> android_apps.intersection(iphone_apps)
{'facebook', 'twitter'}
>>> 

# difference - all that are in the first set, minus the ones that are 
# 	in the second set. NOT COMMUTATIVE
>>> iphone_apps.difference(android_apps)
{'weather_channel', 'coffee_bagel'}
>>> android_apps.difference(iphone_apps)
{'angry_birds'}

# symmetric_difference - in one or other, but no both. is COMMUTATIVE
>>> android_apps.symmetric_difference(iphone_apps)
{'angry_birds', 'weather_channel', 'coffee_bagel'}

# subset, superset, and disjoint sets
>>> professionals = {'Jack','Susie','Sally','Timmy'}
>>> lawyers = {'Jack','Susie'}
>>> doctors = {'Sally','Timmy','Jack'}
>>> professionals.add('Haley')
>>> professionals
{'Susie', 'Timmy', 'Jack', 'Sally', 'Haley'}
>>> therapists = {'Haley'}
>>> lawyers.issubset(professionals)
True
>>> professionals.issuperset(lawyers)
True
>>> doctors.isdisjoint(lawyers)
False
>>> doctors.isdisjoint(therapists)
True
>>> 
















