
x = [3,5,1,0,6]

y = sorted(x, reverse=True) # leaves x unchanged
x.sort() # changes x
print y

# sort the words and counts from highest count to lowest
# wc = sorted(word_counts.items(), key=lambda (word, count): count, reverse=True)

# LIST COMPREHENSIONS

even_numbers = [x for x in range(10) if x % 2 == 0]

squares = [x * x for x in even_numbers]

print even_numbers
print squares

square_dict = { x: x**2 for x in range(10) if x % 2 == 0}

print square_dict

square_set = { x * x for x in [-1, 1]}

print square_set

# GENERATORS

"""A problem with lists is that they can easily grow very big. range(1000000) creates an
actual list of 1 million elements. If you only need to deal with them one at a time, this
can be a huge source of inefficiency (or of running out of memory). If you potentially
only need the first few values, then calculating them all is a waste."""

"""A generator is something that you can iterate over (for us, usually using for) but
whose values are produced only as needed (lazily)."""

def lazy_range(n):
    i = 0;
    while i < n:
        yield i
        i += 1

for i in lazy_range(1000):
    if i == 23:
        break
    # print i

# help(xrange)

# RANDOM NUMBERS

import random

"""If you dont need the value from the list, its conventional to use an underscore as the
variable:"""
rans = [random.random() for _ in range(4)]

print rans

print random.randrange(1990, 2000)
print random.randrange(10)

up_to_ten = range(10)

random.shuffle(up_to_ten)

print up_to_ten

users = ["Alice", "John", "Milly"]

random_choice =  random.choice(users)

print random_choice

lottery_numbers = range(60)

winning_numbers = random.sample(lottery_numbers, 5)

print winning_numbers

# Enumerating, using a list value and its index

for i, document in enumerate(users):
    print i, document

# zipping, make two lists into a single list of tuples

list1 = ['a','b','c', 'd']
list2 = [1,2,3]

list3 = zip(list1, list2)

print list3

letters, numbers = zip(*list3) # asterisk performs argument unpacking,

print letters


def add(a, b): return a + b
add(1, 2) # returns 3
# add([1, 2]) # TypeError!
add(*[1, 2]) # returns 3

def magic(*args, **kwargs):
    print "unnamed args:", args
    print "keyword args:", kwargs
"""args is a tuple of its unnamed arguments
and kwargs is a dict of its named arguments."""
magic(1, 2, key="word", key2="word2")

def other_way_magic(x, y, z):
    return x + y + z
x_y_list = [1, 2]
z_dict = { "z" : 3 }
print other_way_magic(*x_y_list, **z_dict) # 6

