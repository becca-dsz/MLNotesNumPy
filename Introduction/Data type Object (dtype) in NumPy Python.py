import numpy as np


# obj: Object to be converted to a data-type object
# align: bool, optional
# Add padding to the fields to match what a C compiler would outputt for a similar C-struct
# copy: bool, optional
# Make a new copy of the data-type object. If False, te result may just be e referece to a built-in data type object

# Python Program to create a data type object

# np.int16 is converted into a data type object
print(np.dtype(np.int16))


# Python program to create a data type object
# containing a 32 bit big-endian integer

# i4 represents integer of size 4 byte
# > represents ig-endian byte ordering and < represents little
# dt is a dtype object
dt = np.dtype('>i4')

print("Byte order is: ",dt.byteorder)

print("Size is: ", dt.itemsize)

print("Data type is: ",dt.name)


# dtype is different from type

# Python program to differentiate
# between type and dtype

a = np.array([1])

print("type is: ", type(a))
print("dtype is: ",a.dtype)


# A field is like specifying a name to the object
# In the case of structured arrays, the dtype object will also be structured

# Python program for demonstrating
# the use of fields

# A structured data type containing a 16-character string ( in field 'name')
# and a sub-array of two 64-bit floating-point number (in field 'grades')

dt = np.dtype([('name', np.str_, 16),('grades', np.float64, (2,))])

# Data type of object with field grades
print(dt['grades'])

# Data type of object with field name
print(dt['name'])


# Python program to demonstrate
# the use of data type object with structured array

dt = np.dtype([('name', np.str_, 16),('grades', np.float64, (2,))])

# x is a structured array with names and marks of students
# Data type of name of the student is np.str_ and 
# data type of marks is np.float(64)
x = np.array([('Sarah',(8.0,7.0)),('John',(6.0,7.0))], dtype = dt)

print(x[1])
print("Grades of John are: ",x[1]['grades'])
print("Names are: ",x['name'])