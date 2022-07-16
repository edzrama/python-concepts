# Differenc between array and list
import numpy as np
list = [1,2,3]
array = np.array([1,2,3])

# for n in list:
#     print(n)
#
# for a in array:
#     print(a)

list.append(4)
print(list)
# Array is fixed and new record cannot be added
list = list + [5]
print(list)

# Broadcasting  - instead of adding new record [4], it adds 4 to all the existing values
# array = array + np.array([4])
# print(array)
#  vector addition - adds the numbe 4 to 1, 5 to 2, and 6 to 3
# array = array + np.array([4, 5, 6])
# print(array)

# vector multiplication
# array *= 2
# print(array)
#
# # in python list, it is simply repeated by 2
# list *= 2
# print(list)

# vector squared
# array **= 2
# print(array)

# square root of all numbers in arrays
print(np.sqrt(array))
# log
print(np.log(array))
# exponent
print(np.exp(array))
#  hyperbolic tangent
print(np.tanh(array))





