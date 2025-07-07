class Rectangle:
    def __init__(self, width, height):
        self.width = width #stores the width of the rectangle
        self.height = height #stores the height of the rectangle

    def set_width(self, width):
        self.width = width #update the width attr

    def set_height(self, height):
        self.height = height #update the height attr

    def get_area(self):
        return self.width * self.height #area formula: width*height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height #Perimeter Formula: 2(width +height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5 #diagonal = sqrt(widthsqrd + heightsqrd)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = "" #Initialize empty str to build the picture
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, other_shape):
        width_fits = self.width // other_shape.width
        height_fits = self.height // other_shape.height
        return width_fits * height_fits

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) #square must have equal width and height

    def set_side(self, side):
        self.width = side #sets the width of new side length
        self.height = side #sets the height of new side length

    def set_width(self, width):
        self.width = width #set width to new value
        self.height = width #set height to same value to maintain sqr shape

    def set_height(self, height):
        self.width = height #set width to new value to maintain sqr shape
        self.height = height #set height to same value

    def __str__(self):
        return f"Square(side={self.width})" #use width since width and height are of equal value.
        