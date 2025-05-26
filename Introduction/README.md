
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction to NumPy</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            background-color: #1a1a1a;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            font-family: 'Inter', sans-serif;
        }
        .beautiful-heading {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #3b82f6, #a855f7);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
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
<body>
    <h1 class="beautiful-heading">Machine Learning Notes</h1>
</body>
</html>

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
