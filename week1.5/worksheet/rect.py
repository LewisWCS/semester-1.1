# Worksheet 1.5: Rectangle Class

class Rectangle:
    '''represents a rectangle'''
    def __init__(self, width, height):
        '''creating the rectangle'''
        if not isinstance(width,(int,float)):
            raise TypeError('Width must be a number')
        if not isinstance(height,(int,float)):
            raise TypeError('Height must be a number')
        if width <= 0:
            raise ValueError('Width must be greater than one')
        if height <= 0:
                    raise ValueError('Height must be greater than one')
       
        self.width = width
        self.height = height
   
    def is_square(self):
        '''checking if the rectangle is a square'''
        return self.width == self.height
    def area(self):
        '''Checking the area of the rectangle'''
        return self.width * self.height
    def perimeter(self):
        '''Checking the perimeter of the rectangle'''
        return 2 * (self.width + self.height)

rec = Rectangle()
print(rec.is_square())
print(rec.perimeter())
print(rec.area())