import numpy as np


# NumPy Arrays are grid-like structures similar to lists in Python but optimized for numerical operations
# The most straightforward way to create a NumPy array is by converting a regular Pytho list into an array using the np.array() function

# One-dimensional array
arr1 = np.array([1,2,3,4,5])
print(arr1)

# Two-dimensional array
arr2 = np.array([[1,2],[3,4]])
print(arr2)


# np.zeros() function creates an array filled with zeros
# It requires the shape of the array as a parameter

# 3x4 array filled with zeros
arr_zero = np.zeros((3,4))
print(arr_zero)


# np.ones() creates an array filled with ones
arr_one = np.ones((2,3))
print(arr_one)


# np.full() function allows you to create an array filled with a specific value

#2x2 array filled with 7
arr_full = np.full((2,2),7)
print(arr_full)


# np.random.rand() function generates an array of random values between 0 and 1

# 2x3 array of random floats
arr_rand = np.random.rand(2,3)
print(arr_rand)


# If we need random integers, we can use np.random.randint() to create arrays with integer values in a specified range

# 3x3 array of random integers from 1 to 9
arr_int = np.random.randint(1,10,size=(3,3))
print(arr_int)


# np.arange() creates arrays with values spaces according to a given interval.
# It's similar to python's built-in range() but returns a NumPy array

# Array from 0 to 10 with step 2
arr_arange = np.arange(0,10,2)
print(arr_arange)


# np.linspace() generates an array with a specified number of evenly spaced values over a specified range

# 5 values from 0 to 1
arr_linspace = np.linspace(0,1,5)
print(arr_linspace)


# np.eye() function creates an identity matrix, a square matrix with ones on the diagonal and zeros elsewhere

#3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)


# Use np.diag() to create a diagonal matrix, where the provided array elements form teh diagonal

# Diagonal matrix with [1,2,3] on te diagonal
diag_matrix = np.diag([1,2,3])
print(diag_matrix)