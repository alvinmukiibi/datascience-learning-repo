# print "Hello World"


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

# print 2**5 # 2 power 5
#
# print 3.0 // 2.0 # returns the dividend without the remaninder section
#
# print 1/2 # is 0 in py2 but it is 0.5 in py3
# print 1.0/2 # this returns 0.5 well
#
# # Boolean operatiors
#
# check = 2 > 3 and 3 > 2
# print check
# print not False
# print True or False
# print True and False

# STRINGS
# s = "Mukiibi Kelly Alvin"
#
# print type(s) # returns str
#
# print len(s)
#
# s2 = s.replace("Kelly", "Jace")
#
# print s
# print s2
#
# # we can find a character in a str using [] as in index it as an array
#
# print s[5]
#
# print s[2:4] # extract a substring using indexes, returns 2,3 (4 is not returned)
# print s[:8]
# print s[4:]

# LISTS
# very similar to strings except that each element can be of any type

# my_list = [1,4.2,"John", True]
#
# print type(my_list) # list type
#
# print my_list[2]
#
# for item in my_list:
#     print item

# we can generate lists using the range function

# list_2 = range(4, 20, 2) # from 4 to 20, skipping 2, 20 is not returned
#
# print list_2
#
# # in py3 u have to covert it to a list
#
# print list(list(list_2))
#
# my_str = "Kabaka"

# get list from string

# print my_str
# print list(my_str)

# adding modifying and removing elements from lists

# lis = []
#
# lis.append(5)
# lis.append(3)
#
# print lis
#
# lis[1] = 4
#
# print lis
#
# lis.insert(0, True)
# lis.insert(1, "Jack")
#
# print lis
#
# lis.remove(4)
#
# print lis
#
# del lis[2]
#
# print lis


# lists are mutable, tuples are not

# TUPLES

# point = (12, 40)
# point2 = 10, 20
#
# print point
#
# x, y = point2 # assigning each value to a variable using CSV format assigning
#
# print x


# DICTIONARIES
params = { "p1" : 9.0, "p2" : 2, "p3" : 3}
#
# print params['p1']
#
# params['p4'] = 4
#
# print params
#
# print("p1 is equal to " + str(params['p1']))


# CONTROL FLOW if, elif, else

# check = True
#
# if check:
#     print "its true"
#
# LOOPS


# for x in [2,3,4,5]:
#     print x
#
# for key, value in params.items():
#     print key + " = " + str(value)

# creating lists using loops

# list1 = [x*2 for x in range(0,4)]
#
# print list1

# FUNCTIONS

# def my_func():
#     """ To print a string, this is called a docstring, it must follow directly after the function definition """
#     print "This is a function"
#
# my_func()
#
# help(my_func) # prints the doc string
#
# def powers(x):
#     """ return a few powers of a number x """
#     return x**2, x**3, x**4
#
# print(powers(4))
#
# x, y, z = powers(5)
#
# print y

# UNNAMED FUNCTIONS

# created using lambda keyword

# func_two = lambda y: y*7 # given an arg of y, return y by 7
#
# print func_two(8)



# class Point:
#     """ Sample class to represent a cartesian coordinate"""
#
#     def __init__(self, x, y):
#         """Create a new Point x, y"""
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "Point at [%d, %d]" % (self.x, self.y)
#
# p1 = Point(2,3)
# print p1

try:
    print "This is a test"
    print test
except:
    print "Caught an exception because variable is undeclared"



