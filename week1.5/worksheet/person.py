# Worksheet 1.5: Person class

from datetime import date

class Person:
    '''Representing a person'''
    def __init__(self,name,date_birth):
        '''Creating a person'''
        self.name = name
        self.date_birth = date_birth
        if name =='':
            raise ValueError('The first and last name must be present')
        if not isinstance(name,(str)):
            raise TypeError('Please enter a valid name')
        if not isinstance(date_birth, date):
            raise TypeError('Please enter a valid birthday')
    
    def initials(self):
        """Return a persons initials"""
        parts = self.name.split()
        result = ""
        for part in parts:
            result += part[0].upper()
        return result
    
    def is_birthday(self):
        '''Checking if the persons birthday is today'''
        today = date.today()
        return(today.day == self.date_birth.day and 
               today.month == self.date_birth.month)


    