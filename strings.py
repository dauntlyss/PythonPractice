
# Strings

# -You can use str(soemthing) to case something to a string to get access the the string methods on it.
# -f strings can be used on single, double or triple quotes
# -Can't change characters in string'
# -Can concatenate strings
# -Can multiply strings to make more
# -Can iterate over the characters of a string


# **Count**
#     Returns the number of times some character occurs in a string. Is case sensitive. Will return 0 if no occurences.
#     In [87]: msg = 'whats up buttercup. I am so proud of your exercise today. Great headspace!'

#     In [88]: msg.count('a')
#     Out[88]: 6

#     In [89]: msg.count('G')
#     Out[89]: 1


# **Ends with / Starts with**

    # In [90]: msg.endswith('!')
    # Out[90]: True

    # In [91]: msg.startswith('when')
    # Out[91]: False



# **Find**
# Finds the first occurence of a string within a string, and returns its index

#     In [92]: msg.find(' ') (contains several spaces but returns the first one)
#     Out[92]: 5

#     In [93]: msg.find('up') (can search for multiple characters, but will return the index of the first character in the search-string)
#     Out[93]: 6

#     In [94]: msg.find('loser') (will return -1 if not found)
#     Out[94]: -1



# **Join**
# Uses the character to join the elements of an iterable together into a string. 
# In [95]: naughty_foods
# Out[95]:
# ['chicken sandwich',
#  'burger',
#  'snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'snickers']

# In [96]: "|".join(naughty_foods)
# Out[96]: 'chicken sandwich|burger|snickers|skittles|candy corn|starburst|wildberry skittles|snickers'



# **Lower | Upper

# In [98]: 'WHAT'.lower()
# Out[98]: 'what'

# In [99]: 'what'.upper()
# Out[99]: 'WHAT'



# ** Replace **
# Replaces all occurences of the first argument with the second argument, creates an entirly new string with the changes.

# In [103]: phrase = 'what what in the butt'.capitalize()

# In [104]: phrase.replace(' ', '-') (Replaced the space with the hyphen)
# Out[104]: 'What-what-in-the-butt'

# In [105]: phrase.replace(' ', '-', 1)
# Out[105]: 'What-what in the butt'



# ** Split**
# Splits the string at every argument, and returns a list object
# sodas = 'sprite,coke,fanta,mr.pibb'

# In [107]: sodas.split(',')
# Out[107]: ['sprite', 'coke', 'fanta', 'mr.pibb']

# In [108]: sodas_list = sodas.split(',')



# **Splitlines**
# Turns multi line strings into a list
# In [112]: """ I
#      ...: am
#      ...: tired
#      ...: of
#      ...: this
#      ...: video
#      ...: """.splitlines()
# Out[112]: [' I', 'am', 'tired', 'of', 'this', 'video']




# **Strip**
#Returns a copy of the string with leading and trailing whitespace removed
# In [114]: "   goood golly   ".strip()
# Out[114]: 'goood golly'