from polygon_calculator import Rectangle, Square

# Test the example usage from the task
print("=== Testing Rectangle ===")
rect = Rectangle(10, 5)          # Create rectangle with width=10, height=5
print(rect.get_area())           # Should print 50
rect.set_height(3)               # Change height to 3
print(rect.get_perimeter())      # Should print 26 (2*10 + 2*3)
print(rect)                      # Should print Rectangle(width=10, height=3)
print(rect.get_picture())        # Should print picture with asterisks

print("=== Testing Square ===")
sq = Square(9)                   # Create square with side=9
print(sq.get_area())             # Should print 81
sq.set_side(4)                   # Change side to 4
print(sq.get_diagonal())         # Should print 5.656854249492381
print(sq)                        # Should print Square(side=4)
print(sq.get_picture())          # Should print 4x4 square of asterisks

print("=== Testing get_amount_inside ===")
rect.set_height(8)               # Set rectangle to 16x8
rect.set_width(16)
print(rect.get_amount_inside(sq)) # Should print 8 (how many 4x4 squares fit in 16x8)