# Week 1.5, Session 2: Task 2

# Write code here to create and print a Point object,
# then create and print a Circle object
import math
class Point:
    '''Create a class to represent a point in 2D space.'''
    def __init__(self, x:float, y:float):
        if not isinstance(x,(float,int)):
            return ValueError('x is not a valid integer')
        if not isinstance(y,(float,int)):
                    return ValueError('y is not a valid integer')
        self.x = x 
        self.y = y      
    def distance_from_o(self):
          return(f'({self.x},{self.y})')  
    def distance_new_point(self,p):
          return(self.x - p.x , self.y - p.y)
    def __str__(self):
          return f'(The point in the cirlce is {self.x},{self.y})'
print(Point(5,6))
class cirlce:
        def __init__(self, centre:Point, radius:float):
            if not isinstance(centre,Point):
                  return TypeError('Centre must be a point')
            if not isinstance(radius, (int,float)):
                  return TypeError('Radius must be a integer')
            self.radius = radius
            self.centre = centre
        def area(self):
            return math.pi * self.radius * self.radius
        def perimeter(self):
              return 2 * math.pi * self.radius
        def __str__(self):
              return f'The centre is {self.centre}, the radius is {self.radius}'

print(cirlce(Point(5,6),7))

        
        
          
