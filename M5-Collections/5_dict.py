dict: unordered mapping from unique, immutable keys to mutable values
keys must be unique, even if values are 
arbitrary order

>>> urls = {'Google':'http://google.com', 
...     'Pluralsight':'http://pluralsight.com'}
>>> urls
{'Google': 'http://google.com', 'Pluralsight': 'http://pluralsight.com'}
>>> urls['Google']
'http://google.com'
>>> urls['Pluralsight']
'http://pluralsight.com'
>>> 

# can convert list to dict

>>> names_and_ages = [('Alice',32),('Bobbi',48),('Cecily',6)]
>>> mydict = dict(names_and_ages)
>>> mydict
{'Alice': 32, 'Bobbi': 48, 'Cecily': 6}
>>> 

# can convert key val pairs to dict

>>> phonetic = dict(a='alf', b='bravo', c='charlie')
>>> phonetic
{'a': 'alf', 'b': 'bravo', 'c': 'charlie'}
>>> 

# copying dicts: d.copy() or pass dict into the dict constructor

>>> phonetic
{'a': 'alf', 'b': 'bravo', 'c': 'charlie'}
>>> phon_backup = phonetic.copy()
>>> phon_backup
{'a': 'alf', 'b': 'bravo', 'c': 'charlie'}

>>> phon_backup2 = dict(phonetic)
>>> phon_backup2
{'a': 'alf', 'b': 'bravo', 'c': 'charlie'}
>>> 

# update a dictionary with another dictionary
# if value already exists, then will replace current value
>>> phonetic
{'a': 'alf', 'b': 'bravo', 'c': 'charlie'}
>>> mydict
{'Alice': 32, 'Bobbi': 48, 'Cecily': 6}
>>> mydict.update(phonetic)
>>> mydict
{'b': 'bravo', 'Cecily': 6, 'a': 'alf', 'Alice': 32, 'Bobbi': 48, 'c': 'charlie'}
>>> phonetic
{'a': 'alf', 'b': 'bravo', 'c': 'charlie'}
>>> 

>>> stocks = {'GOOG': 891, 'AAPL': 416, 'IBM': 194}
>>> stocks
{'GOOG': 891, 'AAPL': 416, 'IBM': 194}
>>> stocks.update({'GOOG': 1444, 'YHOO':25, 'AAPL':766})
>>> stocks
{'GOOG': 1444, 'AAPL': 766, 'IBM': 194, 'YHOO': 25}
>>> 

# dicts are iterable
>>> for k in stocks:
...     print(k,stocks[k])
... 
GOOG 1444
AAPL 766
IBM 194
YHOO 25

# or...
>>> for k in stocks:                                                          
...     print("{theKey} is currently valued at ${theValue}".format(theKey=k, theValue=stocks[k]))
... 
GOOG is currently valued at $1444
AAPL is currently valued at $766
IBM is currently valued at $194
YHOO is currently valued at $25
>>> 

# only print the values ...
>>> for v in stocks.values():
...     print(v)
... 
1444
766
194
25
>>> 

# only print the keys, although this is the same as default (see 2 above)
>>> for k in stocks.keys():
...     print(k)
... 
GOOG
AAPL
IBM
YHOO
>>> 

# to print in tandem use items()
>>> for k,v in stocks.items():                                                
...     print("STOCK: {theStockname}, PRICE: $ {theStockprice}".format(theStockname=k, theStockprice=v))
... 
STOCK: GOOG, PRICE: $ 1444
STOCK: AAPL, PRICE: $ 766
STOCK: IBM, PRICE: $ 194
STOCK: YHOO, PRICE: $ 25
>>> 

# membership operators work only on the keys
>>> 'GOOG' in stocks
True
>>> 'IBM' not in stocks
False
>>> 'TEAM' in stocks
False
>>> 

# currency symbols
>>> currency_symbols = dict(usd='\u0024')
>>> currency_symbols 
{'usd': '$'}
>>> currency_symbols.update({'GBP':'\u00a3'})
>>> currency_symbols
{'GBP': '£', 'usd': '$'}
>>> currency_symbols.update({'USD':'\u0024','KRW':'\u20a9', 'EUR':'\u20ac'})
>>> currency_symbols
{'GBP': '£', 'USD': '$', 'EUR': '€', 'KRW': '₩', 'usd': '$'}
>>> currency_symbols.update({'JPY':'\u00a5'})
>>> currency_symbols
{'EUR': '€', 'usd': '$', 'GBP': '£', 'USD': '$', 'JPY': '¥', 'KRW': '₩'}
>>> 'EUR' in currency_symbols
True
>>> del currency_symbols['usd']
>>> currency_symbols
{'EUR': '€', 'GBP': '£', 'USD': '$', 'JPY': '¥', 'KRW': '₩'}
>>> 

# the values are mutable (changeable)
>>> chem_elems = {'hydrogen':[1,2,3], 'oxygen':[6,7], 'lithium':[4,5,8]}
>>> chem_elems
{'hydrogen': [1, 2, 3], 'oxygen': [6, 7], 'lithium': [4, 5, 8]}
>>> chem_elems['hydrogen']
[1, 2, 3]
>>> chem_elems['hydrogen'] += [3489, 7847]
>>> chem_elems
{'hydrogen': [1, 2, 3, 3489, 7847], 'oxygen': [6, 7], 'lithium': [4, 5, 8]}
>>> 
# add elements to dict
>>> chem_elems['nitrogen'] = [13,14,15,16]
>>> chem_elems
{'hydrogen': [1, 2, 3, 3489, 7847], 'nitrogen': [13, 14, 15, 16], 'oxygen': [6, 7], 'lithium': [4, 5, 8]}
>>> 
# pretty print
>>> from pprint import pprint as pp
>>> pp(chem_elems)
{'hydrogen': [1, 2, 3, 3489, 7847],
 'lithium': [4, 5, 8],
 'nitrogen': [13, 14, 15, 16],
 'oxygen': [6, 7]}













