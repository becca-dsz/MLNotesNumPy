import numpy as np


# numpy.arange() function creates an array of evenly spaced values within a given interval
# It is similar to Python's built-in range() function but returns a NumPy array instead of a list

# create an array
arr = np.arange(5,10)
print(arr)


# Generate a sequence of integers

# Creating a sequence of numbers from 0 to 9
sequence = np.arange(10)
print("Basic sequence: ", sequence)


# Generate a sequence of floating-point numbers

# Creating a sequence of floating-point numbers from 0 to 1
# with a step size of 0.2 using np.arange()
sequence = np.arange(0,1,0.2)
print("Floating-Point Sequence: ", sequence)


# Generate a sequence and filter specific values

# Creating a sequence of numbers from 0 to 20
sequence = np.arange(0,20,3)

# Filtering the sequence to include only values greater than 10
filtered = sequence[sequence > 10]
print("Filtered sequence: ", filtered)


# numpy.zeros() function creates a new array of specified shapes and types, filled with zero
# It is beneficial when you need a placeholder array to initialize variables or store intermediate results
# We can create 1D array using numpy.zeros()

# Create 1D array
arr = np.zeros(5)
print(arr)


# By using NumPy, we an easily create a 2D array filled with zeros using the numpy.zeros() function

# Creating a 2D array with 3 rows and 4 columns
arr = np.zeros((3,4))
print(arr)


# dtype parameter in numpy.zeros() defines the type of data stored in the array

# Create an array of tuples with zeros
d = np.zeros((2,2), dtype = [('f','f4'),('i','i4')])
print(d)


# Choosing the right memory layout can significantly improve performance, depending on our specific operations
# If your operations are row-wise, use C-order
# If they are column-wise, use F-order

# Create a 2x3 array in C-order
e = np.zeros((2,3), order = 'C')
print("C-ordered array: ", e)

# Create a 2x3 array in F-order
f = np.zeros((2,3), order = 'F')
print("F-ordered array: ", f)