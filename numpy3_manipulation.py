from numpy import *
from random import randint

# list = [randint(50, 100) for _ in range(5)]
list = [82, 78, 71, 59, 57];
vector = array(list)

matrix = diag([1,2,3])
#indexing, starts at 0, so in 3*3 array, the last item is of 2*2

print(vector[3])
print(matrix)
print(matrix[1,2])
print(matrix[2]) # if you omit an index of a multiD array, it returns the whole vector row
print(matrix[2:,]) # row 2 (index) same as statement above
# print(matrix[:1])

# assigning values to indexes
matrix[0,1] = -3
matrix[0,2] = 4
matrix[1,0] = 7
matrix[1,2] = 5
matrix[2,0] = -1

print(matrix)
print(matrix[:,0]) # print first column
print(matrix[:,1]) # print second column
print(matrix[1,:]) # print second row and so on and so forth

# index slicing, extracting a subsection of the array

print(vector)
# print(vector[a:b]) #from index a (included) to index (b - 1)
print(vector[2:4])
# array slices are mutable, assigning them new values alters the original array
vector[0:2] = [90, 32]

print(vector)

print(vector[-1]) # last value in the array
print(vector[-3]) # the 3rd last element
print(vector[-3:]) # the last 3 elements

# Functions for extracting data from arrays and creating arrays

vec = arange(0, 10, 0.5)
mask = (5 < vec) * (vec < 7.5)
print(mask)

indices = where(mask)
print(indices)

values = vec[indices]
print(values)

