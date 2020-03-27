print "Hello World"


import math
# from math import *
# from math import cos, pi
# x = cos(90)

# for md in dir(math):
#     print md
#
# help(math.ceil) # to describe what a function does

my_age = 23
#
# print type(my_age)
#
# x = 1.0 - 2.0j
#
# print type(x)
# print x

import types # modules contains a number of type name defns to test if variables are of a certain type


r = 3.4

is_it = type(r) is float
is_it_2 = isinstance(r, str)
print is_it_2

my_complex = 2 + 3j

print my_complex.imag, my_complex.real
