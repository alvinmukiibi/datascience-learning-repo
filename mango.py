print "Hello World"


import math
# from math import *
# from math import cos, pi
# x = cos(90)

# for md in dir(math):
#     print md
#
# help(math.ceil) # to describe what a function does

# my_age = 23
# #
# # print type(my_age)
# #
# # x = 1.0 - 2.0j
# #
# # print type(x)
# # print x

import types # modules contains a number of type name defns to test if variables are of a certain type


# r = 3.4
#
# is_it = type(r) is float
# is_it_2 = isinstance(r, str)
# print is_it_2
#
# my_complex = 2 + 3j
#
# print my_complex.imag, my_complex.real

# some new operators
# // for integer division, ** for power

print 2**5 # 2 power 5

print 3.0 // 2.0 # returns the dividend without the remaninder section

print 1/2 # is 0 in py2 but it is 0.5 in py3
print 1.0/2 # this returns 0.5 well

# Boolean operatiors

check = 2 > 3 and 3 > 2
print check
print not False
print True or False
print True and False