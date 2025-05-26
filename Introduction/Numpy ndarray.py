import numpy as np


# ndarray is a short form for N-dimensional array which is an important compoent of NumPy.
# It allows us to store and manipulate large amounts of data efficiently
# All elements in an ndarray must be of the same type making it a homogeneous array
# This structure supports multiple datasets like those used in scientific computing or data analysis
# With this we ca perform fast and memory-efficient operations on data.

arr1 = np.array([1,2,3,4,5])

arr2 = np.array([[1,2,3],[4,5,6]])

arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr1)
print(arr2)
print(arr3)


# ndarray.shape: Returns a tuple representing the shape (dimensions) of the array
# ndarray.ndim: Returns the number of dimensions (axes) of the array
# ndarray.size: Returns the total number of elements in the array
# ndarray.dtype: Provides the data type of the array elements
# ndarray.itemsize: Returns the size in bytes of each element

arr = np.array([[1,2,3],[4,5,6]])

print("Shape: ",arr.shape)
print("Dimensions: ", arr.ndim)
print("Size: ", arr.size)
print("Data Type: ", arr.dtype)
print("Item size: ", arr.itemsize)


# We can access individual elements in an array using square brackets just like Python lists
# The indexing starts at 0

arr = np.array([10,20,30,40,50])
print(arr[2])


# Slicing allows us to extract sub-arrays using a range of indices
# The syntax is [start:stop] where start is inclusive and stop is exclusive

arr = np.array([10,20,30,40,50])
print(arr[1:4])


# We can index and slice each dimension separately in multi-dimensional arrays
# This allows us to access specific rows, columns, or deeper dimensions of the array

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr_2d[1,2])

print(arr_2d[0:2, 1:3])


# Element-wise operations are straightforward and allow us to perform arithmetic operations on each element of the array directly

arr = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr + arr2)
print(arr * arr2)
print(arr - arr2)
print(arr / arr2)


# Dot product allows us to multiply two arrays or matrices to get a single value or another matrix

matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])

print(np.dot(matrix1, matrix2))


# Broadcasting enables us to perform operationson arrays of different shapes
# NumPy automatically adjusts smaller array to atch the shape of the larger array to match the shape of the larger one for the operation

arr = np.array([[1,2],[3,4]])

print(arr + 10)


# Reshaping: Changing the shape of the array while keeping the data same

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)


# Flattening: Convert multi-dimensional arrays into one-dimensional arrays

arr = np.array([[1,2,3],[4,5,6]])
flattened_arr = arr.flatten()
print(flattened_arr)