from numpy import *

# FILE I/O

data = genfromtxt('./files/stockholm.dat')
print(data.shape)

# store to files

arr = array([[1,2], [3,4]], dtype=int)
# savetxt("./files/random_data.csv", arr, fmt='%d')

# .npy is numpy's original file format, you can write to it by using "save" and read from it by using "load" functions

save("./files/random_data_2.npy", arr)

arr_2 = load('./files/random_data_2.npy')

print(arr_2)

print(arr.ndim) # ndim for number of dimensions e.g. 2D, 1D, 3D, etc

