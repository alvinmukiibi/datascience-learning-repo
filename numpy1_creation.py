from numpy import *

# CREATING NUMPY ARRAYS FROM PYTHON LISTS
my_list = [1,2,3,4]
vector = array(my_list)
print(vector)

nested_list = [[1,2], [3,4]]
matrix = array(nested_list)
print(matrix)

type(matrix) # numpy.ndarray, the only diff btn matix and vector is shape i.e row * col

vector.shape # 4*1 (4,)
matrix.shape # 2*2 (2,2)

matrix.size # no of elements in the ndarray

datatype = matrix.dtype
# print(datatype) #integers, numpy arrays are statically typed

m = array(nested_list, dtype=complex) # can explicitly define array type at creation
# others are int, float, bool, object etc
# print(m)

# CREATING NUMPY ARRAYS USING FUNCTIONS

# arange

x = arange(0, 10, 1) # x is now of type ndarray
# print(x)

y = arange(-1,1,0.1) # y dtype is float, size is 20
# print(y)

# linspace and logspace

# help(linspace) #  Returns `num` evenly spaced samples, calculated over the interval specified

n = linspace(1, 2, 5) # 5 equal subintervals btn 1 and 2 ( 2-1 div 5-1)
print(n)

# help(logspace) #
l = logspace(0, 10, 10, base=e)
print(l)

#mgrid
# help(mgrid)

d, e =  mgrid[0:3, 0:4]

print(e)

# random data
w = random.rand(2,4) # generates a 2 by 4 matrix of random numbers
print(w)

#diagonal matrix

dg = diag([3,4,5]) # creates a matrix with the args in the main diagonal, left to right, rest are 0s
print(dg)
dg2 = diag([2,3,4], k=1)
print(dg2)

# zeroes and ones
z = zeros((4, 2)) # takes in a tuple for the shape of the matrix with all elements as zeros
print(z)
o = ones((1,3))
print(o)