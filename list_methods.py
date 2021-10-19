
                            # Slicing A List

# syntax = list_name[startingindex: (non-inclusive)stoppingindex :step] Default is 1

# EXAMPLE: numbers = list(range(1, 100, 1))
# In [11]: numbers[50:61:1]
# Out[11]: [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]

# In [12]: numbers[21:43:5]
# Out[12]: [22, 27, 32, 37, 42]

# Can use shortcuts
# In [23]: nums = list(range(0,10))

# In [24]: nums
# Out[24]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# In [25]: nums[2:] (Skip the first n elements and give me the rest (where n is the start number)from the start point to the end, step by 1)
# Out[25]: [2, 3, 4, 5, 6, 7, 8, 9]

# In [26]: nums[2:4] (Give me STOP number of elements, but start at START index, step by 1)
# Out[26]: [2, 3]

# In [27]: nums[:4] (GIve me the first STOP number of elements. From the beginning to the stop (not including the stop), step by 1)
# Out[27]: [0, 1, 2, 3]

# In [28]: nums[::2] (Iterate over the entire list, stepping by 2)
# Out[28]: [0, 2, 4, 6, 8]

# In [29]: nums[3:0:-1] (Iterate backwards(-1) over the list starting at the start and not including the stop. Remember to count backwards for the start and stop indexes)
# Out[29]: [3, 2, 1]

# In [30]: nums[::-2] (Iterate backwards over the entire list, stepping by 2, Quick way to reverse a list)
# Out[30]: [9, 7, 5, 3, 1]




                            # # *****SPLICING A LIST****** # #

# In [32]: fav_candies = ['snickers', 'skittles', 'fudge']

# In [33]: fav_candies[0:1] = ['candy corn'] (replaces the first element with the new list)

# In [34]: fav_candies
# Out[34]: ['candy corn', 'skittles', 'fudge']

# In [35]: fav_candies[2:] = 'snickers' (shouldnt do this because it makes the string an iterable)

# In [36]: fav_candies
# Out[36]: ['candy corn', 'skittles', 's', 'n', 'i', 'c', 'k', 'e', 'r', 's']

# In [37]: fav_candies[2:] = ['snickers'] (take from the second element on and replace it with the new list)

# In [38]: fav_candies
# Out[38]: ['candy corn', 'skittles', 'snickers']

# In [39]: fav_candies[::] = [] (empty the list)

# In [40]: fav_candies
# Out[40]: []







                            # # ***Built in List Methods*** # #


    # --APPEND...
    #Adds an element to the end of a list. Only takes one argument at a time.

# In [45]: fav_candies
# Out[45]: ['snickers', 'skittles', 'candy corn']

# In [46]: fav_candies.append('starburst') (Adds the element to the end of the list. Only takes one argument at a time)

# In [47]: fav_candies
# Out[47]: ['snickers', 'skittles', 'candy corn', 'starburst']



    # -- COPY ...
    #Creates a shallow copy of the list that can be changed without changing the original list

# In [47]: fav_candies
# Out[47]: ['snickers', 'skittles', 'candy corn', 'starburst']

# In [48]: candy_wishlist = fav_candies (Refers to the same reference of the array. If you do an assigment like this, if you change one, the other will change as well.)
# In [54]: fav_candies is candy_wishlist (*Using IS to check identity*)
# Out[54]: True

# In [49]: candy_wishlist
# Out[49]: ['snickers', 'skittles', 'candy corn', 'starburst']

# In [50]: copy_candies = fav_candies.copy() (Use this to create a copy)

# In [51]: copy_candies.append('reeses')

# In [52]: fav_candies
# Out[52]: ['snickers', 'skittles', 'candy corn', 'starburst']

# In [53]: copy_candies
# Out[53]: ['snickers', 'skittles', 'candy corn', 'starburst', 'reeses'] (Now this can be manipulated with no changes to the original array)



    # -- COUNT ...
    # (Counts how many times an item appears in a list.)

# In [55]: fav_candies.append('wildberry skittles')

# In [56]: fav_candies.count('skittles') 
# Out[56]: 1

# In [57]: fav_candies.append('snickers')

# In [58]: fav_candies.count('snickers')
# Out[58]: 2

# In [59]: fav_candies.count('licorice')
# Out[59]: 0

# In [60]: fav_candies
# Out[60]:
# ['snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'snickers']



    # -- EXTEND --
    #Takes one list and adds the contents of the second list to the end.

# In [61]: naughty_foods = ['chicken sandwich', 'burger']

# In [62]: naughty_foods.extend(fav_candies)

# In [63]: fav_candies
# Out[63]:
# ['snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'snickers']

# In [64]: naughty_foods
# Out[64]:
# ['chicken sandwich',
#  'burger',
#  'snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'snickers']



    # -- INDEX --
    # Gives you the first index of the specified element in the list

# In [64]: naughty_foods
# Out[64]:
# ['chicken sandwich',
#  'burger',
#  'snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'snickers']

# In [65]: 'candy corn' in naughty_foods
# Out[65]: True

# In [66]: naughty_foods.index('candy corn')
# Out[66]: 4

# In [67]: naughty_foods.index('snickers') (Gives you the index of the first occurence of the item in the list)
# Out[67]: 2

# In [68]: naughty_foods.index('fish') (WIll give and error if item is not in list)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-68-7b6c0eadd9b6> in <module>
# ----> 1 naughty_foods.index('fish')

# ValueError: 'fish' is not in list



    # -- INSERT --
    # Adds the element at the specified index 
    # syntax = list.insert(index, element)

# In [70]: fav_candies
# Out[70]:
# ['snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'snickers']

# In [71]: fav_candies.insert(5, 'airheads') (does not replaces the item already at 5, only shifts things down.)

# In [72]: fav_candies
# Out[72]:
# ['snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'airheads',
#  'snickers']



    # -- POP --
    # Removes and RETURNS the item at the specified index. If no index is specified, it will default to the last item "Pops it off"

# In [72]: fav_candies
# Out[72]:
# ['snickers',
#  'skittles',
#  'candy corn',
#  'starburst',
#  'wildberry skittles',
#  'airheads',
#  'snickers']

# In [73]: fav_candies.pop()
# Out[73]: 'snickers'

# In [74]: dont_want = fav_candies.pop(1)

# In [75]:

# In [75]: print(f'I dont want {dont_want}')
# I dont want skittles

# In [76]: fav_candies
# Out[76]: ['snickers', 'candy corn', 'starburst', 'wildberry skittles', 'airheads']



    # -- REVERSE --
    # Reverses the list

# In [76]: fav_candies
# Out[76]: ['snickers', 'candy corn', 'starburst', 'wildberry skittles', 'airheads']

# In [77]: fav_candies.reverse()

# In [78]: fav_candies
# Out[78]: ['airheads', 'wildberry skittles', 'starburst', 'candy corn', 'snickers']



    # -- SORT --
    # Sorts a list based on type, strings = alpha, numbers = little to large. Also must be a homogenous list

# In [78]: fav_candies
# Out[78]: ['airheads', 'wildberry skittles', 'starburst', 'candy corn', 'snickers']

# In [79]: fav_candies.sort()

# In [80]: fav_candies
# Out[80]: ['airheads', 'candy corn', 'snickers', 'starburst', 'wildberry skittles']

# In [81]: numbers = [99, 18, 45, -6, -24, 0, 16600]

# In [82]: numbers.sort()

# In [83]: numbers
# Out[83]: [-24, -6, 0, 18, 45, 99, 16600]

# In [84]: numbers.sort(reverse=True)

# In [85]: numbers
# Out[85]: [16600, 99, 45, 18, 0, -6, -24]


