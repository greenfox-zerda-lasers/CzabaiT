# Create a `Circle` class that takes it's radius as constructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area
import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return self.radius ** 2 * math.pi


circle = Circle(6)
print("Circumference is: %.3f" % (circle.get_circumference()))
print("Area is: %.3f" % (circle.get_area()))
