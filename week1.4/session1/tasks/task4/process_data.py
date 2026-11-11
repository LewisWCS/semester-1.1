# Week 4, Session 1

# You are given function process_data with docstring. 
# Is the function returning the correct value corresponding to the docstring? 
# Which line of code contains the inconsistency?

# Your task is to identify the incorrect line of code and
# update the code to produce the correct output.


def process_data(data):
    total = 0
    for i in data:
        total = total + i
    if not data:
        return '0'
    return total

# What is output from the following line of code?
print(process_data([1, 2, 3, 4, 5]))  # 15?

# How about this one?
print(process_data([]))               # None?
