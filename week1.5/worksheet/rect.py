# Worksheet 1.5: Rectangle Class

class Rectangle:
   
    def __init__(self, width, height):
# checking for value errors=================================================================       
        if not isinstance(width,(int,float)):
            raise TypeError('Width must be a number')
        if not isinstance(height,(int,float)):
            raise TypeError('Height must be a number')
        if width <= 0:
            raise ValueError('Width must be greater than one')
        if height <= 0:
                    raise ValueError('Height must be greater than one')
# The parameters===========================================================================       
        self.width = width
        self.height = height
# every function that will be used=========================================================   
    def is_square(self):
        return self.width == self.height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
#print out the values=======================================================================
rec = Rectangle(0,5)
print(rec.is_square())
print(rec.perimeter())
print(rec.area())