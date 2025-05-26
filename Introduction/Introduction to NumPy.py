import numpy as np


# The array object is called ndarray.
# NumPy arrays are created using the array() function

# creating a 1D array
x =np.array([1,2,3])

# creating a 2D array
y=np.array([[1,2],[3,4]])

# creating a 3D array
z=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(x)
print(y)
print(z)


# NumPy provides convenient methods to create arrays initialized with specific values like zeros and ones

a1_zeros = np.zeros((3,3))
a2_ones = np.ones((2,2))
a3_range = np.arange(0,10,2)

print(a1_zeros)
print(a2_ones)
print(a3_range)


# Basic indexing in NumPy allows you to access elements of an array using indices

# Create a 1D array
arr1d = np.array([1,2,3,4,5])

# Single element access
print("Single element access: ",arr1d[2])

# Negative indexing
print("Negative indexing: ", arr1d[-1])

# Create a 2D array
arr2d = np.array([[1,2],[3,4]])

# Multidimensional array access
print("Mulidimensional array access: ",arr2d[1,0])


# Just like lists in Python, NumPy arrays can be sliced.
# As arrays can be multidimensional, you need to specify a slice for each dimsnion of the array

arr = np.array([[1,2,3],[4,5,6]])

# elements from index 1 to 3
print("Range of Elements: ",arr[1:4])

# all rows, second column
print("Multi-dimensional slicing: ",arr[:,1])


# Advanced indexing in NumPy provides more powerful and flexible ways to access and manipulate array elements

arr = np.array([10,20,30,40,50,60,70,80,90,100])

# Integer array indexing
indices = np.array([1,3,5])
print("Integer Array Indexing: ",arr[indices])

# Boolean array indexing
cond = arr>0
print("\nElements greater than 0: ",arr[cond])


# We can perform arithmetic operations like addition, subtraction, multiplication, and division directly on NumPy arrays

x = np.array([1,2,3])
y = np.array([4,5,6])

# Addition
add = x+y
print("Addition: ",add)

# Subtraction
subtract = x-y
print("Subtraction: ", subtract)

# Multiplication
multiply =x*y
print("Multiplication: ",multiply)

# Division
divide = x/y
print("Division: ",divide)


# Unary operations are applied to each individual element in the array, without the need for multiple arrays (as in binary operations)

# Example array with both positive and negative values
arr= np.array([-3,-1,0,1,3])

# Applying a unary operation: absolute value
result = np.absolute(arr)
print("Absolute values: ",result)


# NumPy Binary Operations apply to the array elementwise and a new array is created.
# We can use all basic arithmetic operators like +,-,/, etc.
# In the case of +=,-=,= operators, the existing array is modified

# Two example arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# Applying a binary operation: addition
result = np.add(arr1,arr2)

print("Array 1: ",arr1)
print("Array 2: ",arr2)
print("Addition Result: ", result)


# NumPy provides familiar mathematical functions such as sin, cos, exp, etc.
# These functions also operate elementwise on an array, producing a array as output

# Create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print("Sine values of array elements: ", np.sin(a))

# Exponential values
a = np.array([0,1,2,3])
print("Exponent of array elements: ", np.exp(a))

# Square root of array values
print("Square root of array elements: ",np.sqrt(a))


# We can use simple np.sort() method for sorting Python NumPy arrays

# Set alias names for dtypes
dtypes = [('name','S10'),('grad_year',int),('cgpa',float)]

# Values to be put in array
values = [('Hrithik',2009,8.5),('Ajay',2008,8.7),('Pankaj',2008,7.9),('Aakash',2009,9.0)]

# Creating array
arr = np.array(values, dtype = dtypes)
print("\nArray sorted by Names:\n", np.sort(arr, order='name'))

print("Array sorted by gradution year and then cgpa:\n", np.sort(arr, order=['grad_year','cgpa']))