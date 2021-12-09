# Dictionarys are mutable ordered mapping of key value pairs

# -Keys can be any immutable type, not just strings. 
# -Values can be anything

# In [119]: skittle = {'color':'red', 'flavor':'strawberry', 'pack_size':'share'}

# In [120]: skittle
# Out[120]: {'color': 'red', 'flavor': 'strawberry', 'pack_size': 'share'}


# -The IN keyword checks for membership of a key
# In [122]: 'color' in skittle
# Out[122]: True


# -Access a specific value represented by a key with syntax object['key']
# In [123]: skittle['pack_size']
# Out[123]: 'share'

# In [124]: skittle['pack_size'] = 'regular'

# In [125]: skittle
# Out[125]: {'color': 'red', 'flavor': 'strawberry', 'pack_size': 'regular'}


# -can use the GET() attribute to get key-value pairs from the object. You can pass in a default value if nothing is found.
# In [126]: skittle.get('pack_color')

# In [127]: skittle.get('pack_color', 'purple')
# Out[127]: 'purple'

# In [128]: skittle.get('color')
# Out[128]: 'red'


# -Can use the dict() constructor to create a dictionary
# In [131]: dict([[True, 1], [False, 3]])
# Out[131]: {True: 1, False: 3}


# *** Iterating over Dictionaries ***

book = {
    'title': 'misery',
    'author': 'King',
    'length': '263 pages',
    'stats': {
        'rating': 4.25,
        'genre': 'horror',
        'finish_date': '10-12-21'
    }
}

# In [145]: book.keys()
# Out[145]: dict_keys(['title', 'author', 'length', 'stats'])

# In [146]: book.values()
# Out[146]: dict_values(['misery', 'King', '263 pages', {'rating': 4.25, 'genre': 'horror', 'finish_date': '10-12-21'}])

# In [147]: book.items()
# Out[147]: dict_items([('title', 'misery'), ('author', 'King'), ('length', '263 pages'), ('stats', {'rating': 4.25, 'genre': 'horror', 'finish_date': '10-12-21'})])

# In [149]: for pair in book.items():
#      ...:     print(pair)
#      ...:
# ('title', 'misery')
# ('author', 'King')
# ('length', '263 pages')
# ('stats', {'rating': 4.25, 'genre': 'horror', 'finish_date': '10-12-21'})

