import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Creating objects of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

# List of shapes
shapes = [circle, rectangle, triangle]

# Demonstrating polymorphism
for shape in shapes:
    print(f"{shape} has an area of {shape.area()}")


