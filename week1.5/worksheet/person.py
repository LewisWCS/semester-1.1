# Worksheet 1.5: Person class

from datetime import date

class Person:
    '''Representing a person'''
    def __init__(self,first,last,date_birth):
        '''Creating a person'''
        self.first = first
        self.last = last
        self.date_birth = date_birth
        self.name = first + last
        if first == "" or last == "":
            raise ValueError('The first and last name must be present')

    def initials(self):
        '''We are retuning the persons initials'''
        return self.first[0].upper() + self.last[0].upper()
    
    def is_birthday(self):
        '''Checking if the persons birthday is today'''
        today = date.today()
        return(today.day == self.date_birth.day and 
               today.month == self.date_birth.month)

emp_1 = Person()
print(emp_1.initials())
print(emp_1.date_birth)
print(emp_1.is_birthday())
    