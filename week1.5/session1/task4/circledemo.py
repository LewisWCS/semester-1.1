# Week 1.5, Session 1: Task 4
import math

class point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
class circle:
    def __init__(self, center_point, radius):
        self.center = center_point
        self.radius = radius

def area(self):
        return math.pi * (self.radius ** 2)

def perimeter(self):
        return 2 * math.pi * self.radius

center = point(3, 4)
circle = circle(center, 5)

print(f'Area of circle: {area(circle):.1f}')
print(f'Perimeter of circle: {perimeter(circle):.1f}')

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
