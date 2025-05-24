import numpy as np


# Arrays in Numpy can be created by multiple ways, with various number of Ranks, defining the size of the Arrays
# Arrays can also be created with the use of various data types such as lists, tuples, etc.
# The type of the resultant array is deduced from the type of the elements in the sequences

# Creating a rank 1 array
arr = np.array([1,2,3])
print(arr)

# Creating a rank 2 array
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

# Creating an array from tuple
arr = np.array((1,3,2))
print(arr)


# In a numpy array, indexing or accessing the array index can be done in multiple ways. 
# To print a range of an array, slicing is done
# Slicing of an array is defining a range in a new array which is used to print a range of elements from the original array.
# Since, sliced array holds a range of elements of the original array, modifying content with the help of sliced array modifies the original array content

arr = np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])

# Printing a range of array
# with the use of slicing method
arr2 = arr[:2, ::2]
print("First 2 rows and alternate columns ( 0 and 2 ):\n", arr2)

# Printing elements at
# specific indices
arr3 = arr[[1,1,0,3],[3,2,1,0]]
print("\nElements at indices (1,3), (1,2), (0,1), (3,0):\n", arr3)


# In NumPy, arrays allow a wide range of operations which can be performed on a particular array or a combination of Arrays
# These operation include some basic Mathematical operation as well as Unary and Binary operations

# Defining array 1
a = np.array([[1,2],[3,4]])

# Defining array 2
b = np.array([[4,3],[2,1]])

# Adding 1 to every element
print("Adding 1 to every element: ",a+1)

# Subtracting 2 from each element
print("Subtracting 2 from each element:", b-2)

# sum of array elements
# performing unary operations
print("\nSum of all array elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a+b)


# In NumPy, datatypes of arrays need not to be defined unless a specific datatype is required
# NumPy tries to guess the datatype for Arrays which are not predefined in the constructor function

# Integer datatype
x = np.array([1,2])
print(x.dtype)

# Float datatype
x = np.array([1.0,2.0])
print(x.dtype)

# Forced Datatype
x = np.array([1,2], dtype = np.int64)
print(x.dtype)


# In Numpy arrays, basic mathematical operations are performed element-wise on the array
# These operations are applied both as operator overloads and functions
# Many useful functions are provided in NumPy for performing computations on Arrays such as sum: for addition of Array elements, T: for Transpose of elements, etc.

# First array
arr1 = np.array([[4,7],[2,6]], dtype = np.float64)

# Second Array
arr2 = np.array([[3,6],[2,8]], dtype = np.float64)

# Addition of two arrays
Sum = np.add(arr1, arr2)
print(Sum)

# Addition of all array elements
Sum1 = np.sum(arr1)
print(Sum1)

# Square root of array
Sqrt = np.sqrt(arr1)
print(Sqrt)

# Transpose of Array
Trans_arr = arr1.T
print(Trans_arr)
