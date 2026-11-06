# Worksheet 1.5: Person class

from datetime import date

class Person:
    def __init__(self,first,last,date_birth):
        self.first = first
        self.last = last
        self.date_birth = date_birth
        self.name = first + last

    def initials(self):
        return self.first[0].upper() + self.last[0].upper()
    
    def is_birthday(self):
        today = date.today()
        return(today.day == self.date_birth.day and 
               today.month == self.date_birth.month)

emp_1 = Person('John','boy',date(2005, 11, 6))
print(emp_1.initials())
print(emp_1.date_birth)
print(emp_1.is_birthday())
    