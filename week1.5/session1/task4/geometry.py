# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math
class circle:
    def __init__(self, center_point, radius):
        self.center = center_point
        self.radius = radius

class point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

def area(self):
        return math.pi * (self.radius ** 2)

def perimeter(self):
        return 2 * math.pi * self.radius

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
