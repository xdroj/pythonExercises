# Polygon Area Calculator

A Python project that implements object-oriented programming concepts to create Rectangle and Square classes with various geometric calculations and visual representations.

## Project Overview

This project is part of the FreeCodeCamp Scientific Computing with Python certification. It demonstrates inheritance, method overriding, and object-oriented design principles by creating geometric shape classes.

## Features

### Rectangle Class
- Initialize with width and height
- Calculate area, perimeter, and diagonal
- Generate ASCII art representation
- Calculate how many shapes fit inside
- Set width and height independently

### Square Class
- Inherits from Rectangle class
- Initialize with a single side length
- Maintains square properties when dimensions change
- All Rectangle methods available
- Additional `set_side()` method

## File Structure

```
PolygonAreaCalculator/
├── polygon_calculator.py    # Main implementation
├── README.md               # This file
├── task.md                # Project requirements
└── test_polygon.py        # Test file (optional)
```

## Usage Examples

### Rectangle Operations
```python
from polygon_calculator import Rectangle

# Create a rectangle
rect = Rectangle(10, 5)

# Basic calculations
print(rect.get_area())        # Output: 50
print(rect.get_perimeter())   # Output: 30
print(rect.get_diagonal())    # Output: 11.180339887498949

# Modify dimensions
rect.set_width(8)
rect.set_height(3)

# String representation
print(rect)                   # Output: Rectangle(width=8, height=3)

# ASCII art picture
print(rect.get_picture())
# Output:
# ********
# ********
# ********
```

### Square Operations
```python
from polygon_calculator import Square

# Create a square
sq = Square(4)

# All Rectangle methods work
print(sq.get_area())          # Output: 16
print(sq.get_perimeter())     # Output: 16
print(sq.get_diagonal())      # Output: 5.656854249492381

# Square-specific method
sq.set_side(6)
print(sq)                     # Output: Square(side=6)

# Setting width or height maintains square shape
sq.set_width(5)
print(sq)                     # Output: Square(side=5)
```

### Shape Fitting Calculation
```python
# How many small shapes fit inside a larger shape
rect = Rectangle(15, 10)
sq = Square(5)

fits = rect.get_amount_inside(sq)
print(fits)                   # Output: 6
```

## Method Documentation

### Rectangle Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `__init__(width, height)` | Initialize rectangle | None |
| `set_width(width)` | Set rectangle width | None |
| `set_height(height)` | Set rectangle height | None |
| `get_area()` | Calculate area | int/float |
| `get_perimeter()` | Calculate perimeter | int/float |
| `get_diagonal()` | Calculate diagonal length | float |
| `get_picture()` | Generate ASCII art | string |
| `get_amount_inside(shape)` | Count shapes that fit inside | int |
| `__str__()` | String representation | string |

### Square Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `__init__(side)` | Initialize square | None |
| `set_side(side)` | Set all sides to same length | None |
| `set_width(width)` | Set width (height follows) | None |
| `set_height(height)` | Set height (width follows) | None |
| All Rectangle methods | Inherited functionality | Various |

## Key Features Explained

### 1. Inheritance
- Square class inherits from Rectangle class
- Demonstrates "is-a" relationship (Square is a Rectangle)
- Code reuse through inheritance

### 2. Method Overriding
- Square overrides `set_width()` and `set_height()` to maintain square properties
- Custom `__str__()` methods for different string representations

### 3. ASCII Art Generation
```python
# For a 3x4 rectangle:
print(Rectangle(3, 4).get_picture())
# Output:
# ***
# ***
# ***
# ***
```

### 4. Size Limitations
- Pictures larger than 50 in width or height return: "Too big for picture."

### 5. Shape Fitting Algorithm
```python
# Calculates how many shapes fit without rotation
width_fits = self.width // other_shape.width
height_fits = self.height // other_shape.height
total_fits = width_fits * height_fits
```

## Testing

The project should pass these key tests:

1. ✅ Square inherits from Rectangle
2. ✅ Correct string representations
3. ✅ Accurate mathematical calculations
4. ✅ Proper dimension setting behavior
5. ✅ ASCII art generation
6. ✅ Shape fitting calculations

## Running the Code

1. Save the code in `polygon_calculator.py`
2. Run in Python:

```bash
python polygon_calculator.py
```

Or import in another Python file:

```python
from polygon_calculator import Rectangle, Square

# Your code here
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Learning Objectives

This project teaches:
- Object-oriented programming concepts
- Class inheritance and method overriding
- String formatting and representation
- Mathematical calculations in programming
- ASCII art generation
- Algorithm implementation

## Author

Created as part of FreeCodeCamp Scientific Computing with Python certification.

## License

This project is for educational purposes.