import numpy as np


# A one dimensional array is a type of linear array

list = [1,2,3,4]

sample_array = np.array(list)

print("List in Python: ",list)

print("Numpy array in python: ",sample_array)


# Check data type for list and array

print(type(list))

print(type(sample_array))


# A 2D array is like a table with rows and columns where each element is accessed by two indices: one for the row and one for the column
# Higher dimensions like 3D arrays involve adding additional layers

list_1=[1,2,3,4]
list_2=[5,6,7,8]
list_3=[9,10,11,12]

sample_array = np.array([list_1,list_2,list_3])
print("Numpy multi-dimensional array in python\n", sample_array)


# Shape: Number of elements along with each axis is returned as a tuple

sample_array = np.array([[0,4,2],[3,4,5],[23,4,5],[2,34,5],[5,6,7]])

print("Shape of the array: ", sample_array.shape)


# Data typeobkects (dtype) is an example of numpy.dtype class
# It describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted

sample_array_1 = np.array([[0,4,2]])

sample_array_2 = np.array([0.2,0.4,2.4])

print("Data type of the array 1: ", sample_array_1.dtype)

print("Data type of array 2: ", sample_array_2.dtype)


# numpy.array(): Numpy array object in NumPy ia called ndarray

arr = np.array([3,4,5,5])

print("Array: ",arr)


# the fromiter() function create a new one-dimensional array from an iterable object

var = "Geeksforgeeks"

arr = np.fromiter(var, dtype = 'U2')

print("fromiter() array:", arr)


# numpy.arange() is an inbuilt NumPy function that returns evenly spaced values within a given interval

np.arange(1,20,2, dtype = np.float32)


# numpy.linspace() function returns evenly spaced numbers over a specified limit

np.linspace(3.5, 10, 3, dtype=np.int32)


# numpy.empty() function creates a new array of given shapeand type without initializing value

np.empty([4,3], dtype = np.int32, order='F')


# numpy.ones() function is used to get a new array of given shape and type filled with ones (1)

np.ones([4,3], dtype = np.int32, order = 'F')


# numpy.zeros() used to get new array of given shape and type filled with zeros (0)

np.zeros([4,3], dtype = np.int32, order = 'F')