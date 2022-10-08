class Shape:
    def __init__(self):
        print("Base class")

    def Area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        print("Circle class")

    def Area(self):
        cirle_area = 3.14 * self.radius * self.radius
        print("Area of circle: ", cirle_area)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        rect_area = self.length * self.breadth
        print("Area of Rectangle: ", rect_area)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def Area(self):
        sq_area = self.side * self.side
        print("Area of Square: ", sq_area)

obj = Rectangle(6, 8)
obj.Area()

obj1 = Circle(4)
obj1.Area()

obj2 = Square(7)
obj2.Area()