from numpy import *

v1 = array([1,3,6,8])
v2 = v1 * 2

print(v2)

v3 = v1 + 2
print(v3)

v4 = v1 * 2, v1 + 2
print(v4)

# When we add, subtract, multiply and divide arrays with each other, the default behaviour is element-wise
# operations

v5 = v1 ** 2
print(v5)

v6 = array([[1,2,3,4], [5,6,7,8]])

print(v1.shape)
print(v6.shape)
print(v1)
print(v6)
v7 = v1 * v6
# print(v7)

# dot multiplication
# help(dot)

v8 = dot(v6, v1) # 2*4 . 4*1 they must be compatible, resultant is 2*1
print(v8)