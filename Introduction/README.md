
<head>
    <style>
        .beautiful-heading {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #3b82f6, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            text-align: center;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        .beautiful-heading::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 3px;
            background: linear-gradient(45deg, #3b82f6, #a855f7);
            transition: width 0.3s ease;
        }
        .beautiful-heading:hover::after {
            width: 50%;
        }
    </style>
</head>
<body class="bg-gray-900 min-h-screen flex items-center justify-center">
    <h1 class="beautiful-heading">Introduction to NumPy</h1>
</body>


The array object is called ndarray.
NumPy arrays are created using the array() function.

<br>

NumPy provides convenient methods to create arrays initialized with specific values like zeros and ones

<br>

Basic indexing in NumPy allows you to access elements of an array using indices

<br>

Just like lists in Python, NumPy arrays can be sliced. As arrays can be multidimensional, you need to specify a slice for each dimsnion of the array

<br>

Advanced indexing in NumPy provides more powerful and flexible ways to access and manipulate array elements

<br>

We can perform arithmetic operations like addition, subtraction, multiplication, and division directly on NumPy arrays

<br>

Unary operations are applied to each individual element in the array, without the need for multiple arrays (as in binary operations)

<br>

NumPy Binary Operations apply to the array elementwise and a new array is created. We can use all basic arithmetic operators like +,-,/, etc. In the case of +=,-=,= operators, the existing array is modified

<br>

NumPy provides familiar mathematical functions such as sin, cos, exp, etc. These functions also operate elementwise on an array, producing a array as output

<br>

We can use simple np.sort() method for sorting Python NumPy arrays
