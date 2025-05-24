import numpy as np


# NumPy array's objects allow us to work with arrays in Python
# The array object is called ndarray
# NumPy arrays are created using the array() function

# Creating a 1D array
x = np.array([1,2,3])

# Creating a 2D array
y = np.array([[1,2],[3,4]])

# Creating a 3D array
z = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])

print(x)
print(y)
print(z)


# NumPy arrays have attributes that provide information about the array:
# shape: returns the dimension of the array
# dtype: returns the data type of the elements
# ndim: Returns the number of dimensions

arr = np.array([[1,2,3],[4,5,6]])

print(arr.shape)
print(arr.dtype)
print(arr.ndim)


# Numpy supports element-wise and matrix operations, including addition, subtraction, multiplication, and division

# Element-wise addition
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
# Output: [5 7 9]

# Matrix Multiplication
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.dot(a,b))