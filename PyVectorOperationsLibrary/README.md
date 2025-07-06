Python Vector Operations Library
A Python project implementing 2D (R2Vector) and 3D (R3Vector) vector classes with various mathematical operations overloaded using Python's special methods (dunder methods). This library allows for intuitive and expressive vector arithmetic.

Table of Contents
Features

Classes

Installation

Usage

Instantiation

Vector Addition (+)

Vector Subtraction (-)

Scalar Multiplication (*)

Dot Product (Vector Multiplication *)

Cross Product (.cross())

Vector Norm / Magnitude (.norm())

Equality (==) and Inequality (!=)

Magnitude Comparisons (<, >, <=, >=)

Contributing

License

Author

Features
This library provides the following functionalities for vector objects:

Initialization: Create 2D and 3D vectors with named components (e.g., x, y, z).

Vector Addition: Add two vectors of the same dimension.

Vector Subtraction: Subtract one vector from another of the same dimension.

Scalar Multiplication: Multiply a vector by an integer or float.

Dot Product: Compute the scalar product (dot product) of two vectors of the same dimension.

Cross Product: Compute the vector product (cross product) of two 3D vectors.

Norm (Magnitude): Calculate the Euclidean norm (magnitude) of a vector.

String Representation: Human-readable and unambiguous string representations for vectors.

Comparison Operators:

Equality (==): Check if two vectors are identical (component-wise).

Inequality (!=): Check if two vectors are not identical.

Magnitude Less Than (<): Compare vectors based on their norm.

Magnitude Greater Than (>): Compare vectors based on their norm.

Magnitude Less Than or Equal (<=): Compare vectors based on their norm.

Magnitude Greater Than or Equal (>=): Compare vectors based on their norm.

Classes
R2Vector: Represents a 2-dimensional vector with x and y components.

R3Vector: Inherits from R2Vector and adds a z component, representing a 3-dimensional vector. It also implements the cross() product specific to 3D vectors.

Installation
This project is a single Python file. No special installation is required. Simply save the provided code as a .py file (e.g., vectors.py) and import it into your Python scripts or run it directly.

Bash

# Save the code as vectors.py
# python vectors.py
Usage
Here are examples demonstrating how to use the vector classes and their operations.

Instantiation
Python

from vectors import R2Vector, R3Vector

v2d_a = R2Vector(x=1, y=2)
v2d_b = R2Vector(x=3, y=4)

v3d_a = R3Vector(x=1, y=2, z=3)
v3d_b = R3Vector(x=4, y=5, z=6)

print(f"2D Vector A: {v2d_a}") # Output: 2D Vector A: (1, 2)
print(f"3D Vector A: {v3d_a}") # Output: 3D Vector A: (1, 2, 3)
Vector Addition (+)
Python

v2d_sum = v2d_a + v2d_b
print(f"{v2d_a} + {v2d_b} = {v2d_sum}") # Output: (1, 2) + (3, 4) = (4, 6)

v3d_sum = v3d_a + v3d_b
print(f"{v3d_a} + {v3d_b} = {v3d_sum}") # Output: (1, 2, 3) + (4, 5, 6) = (5, 7, 9)
Vector Subtraction (-)
Python

v2d_diff = v2d_a - v2d_b
print(f"{v2d_a} - {v2d_b} = {v2d_diff}") # Output: (1, 2) - (3, 4) = (-2, -2)

v3d_diff = v3d_a - v3d_b
print(f"{v3d_a} - {v3d_b} = {v3d_diff}") # Output: (1, 2, 3) - (4, 5, 6) = (-3, -3, -3)
Scalar Multiplication (*)
Python

v2d_scaled = v2d_a * 5
print(f"{v2d_a} * 5 = {v2d_scaled}") # Output: (1, 2) * 5 = (5, 10)

v3d_scaled = v3d_a * 2.5
print(f"{v3d_a} * 2.5 = {v3d_scaled}") # Output: (1, 2, 3) * 2.5 = (2.5, 5.0, 7.5)
Dot Product (Vector Multiplication *)
Python

# R2Vector dot product
v2d_dot = v2d_a * v2d_b
print(f"{v2d_a} . {v2d_b} = {v2d_dot}") # Output: (1, 2) . (3, 4) = 1*3 + 2*4 = 11

# R3Vector dot product
v3d_dot = v3d_a * v3d_b
print(f"{v3d_a} . {v3d_b} = {v3d_dot}") # Output: (1, 2, 3) . (4, 5, 6) = 1*4 + 2*5 + 3*6 = 32
Cross Product (.cross())
Available only for R3Vector instances.

Python

v3d_cross = v3d_a.cross(v3d_b)
print(f"{v3d_a} x {v3d_b} = {v3d_cross}")
# Output: (1, 2, 3) x (4, 5, 6) = R3Vector(x=-3, y=6, z=-3)
# (2*6 - 3*5) = -3
# (3*4 - 1*6) = 6
# (1*5 - 2*4) = -3
Vector Norm / Magnitude (.norm())
Python

norm_v2d_a = v2d_a.norm()
print(f"Norm of {v2d_a}: {norm_v2d_a:.2f}") # Output: Norm of (1, 2): 2.24

norm_v3d_a = v3d_a.norm()
print(f"Norm of {v3d_a}: {norm_v3d_a:.2f}") # Output: Norm of (1, 2, 3): 3.74
Equality (==) and Inequality (!=)
Python

v_equal = R2Vector(x=10, y=20)
v_same_equal = R2Vector(x=10, y=20)
v_diff_equal = R2Vector(x=10, y=21)

print(f"{v_equal} == {v_same_equal}: {v_equal == v_same_equal}") # Output: True
print(f"{v_equal} == {v_diff_equal}: {v_equal == v_diff_equal}") # Output: False
print(f"{v_equal} != {v_diff_equal}: {v_equal != v_diff_equal}") # Output: True
print(f"{v_equal} != {v_same_equal}: {v_equal != v_same_equal}") # Output: False
Magnitude Comparisons (<, >, <=, >=)
Python

v_small = R2Vector(x=1, y=0) # norm = 1
v_medium = R2Vector(x=1, y=1) # norm = sqrt(2) ≈ 1.41
v_large = R2Vector(x=2, y=0) # norm = 2

print(f"{v_small} < {v_medium}: {v_small < v_medium}")   # Output: True
print(f"{v_large} > {v_medium}: {v_large > v_medium}")   # Output: True
print(f"{v_medium} <= {v_medium}: {v_medium <= v_medium}") # Output: True
print(f"{v_medium} >= {v_large}: {v_medium >= v_large}")   # Output: False
Contributing
Feel free to fork this repository, open issues, or submit pull requests.

License
This project is open source and available under the MIT License.