# Matrix
import numpy as np

py_list = [[1, 2], [3, 4]]
print(py_list)
print(py_list[0][1])

numpy_array = np.array([[1, 2], [3, 4]])
print(numpy_array)
print(numpy_array[0][1])
print(numpy_array[0, 1])

# select all rows
print(numpy_array[:, 0])
# transposed array
print(f"transpose: {numpy_array.T}")

print(np.exp(numpy_array))
# numpy recognizes python list as numpy array as well
print(np.exp(py_list))

array2 = np.array([[1, 2, 3], [4, 5, 6]])

print(numpy_array.dot(array2))

# invalid, dimension don't match'
# print(numpy_array.dot(array2.T))

print(np.linalg.inv(numpy_array))
