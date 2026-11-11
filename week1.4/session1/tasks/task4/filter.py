# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def filter_positive_numbers(*numbers):
    lst = []
    for i in numbers:
        if i % 2 == 0:
            continue
        else:
            lst.append(i)
   
    return lst

print(filter_positive_numbers(1,2,3,4,5,6,7,8,9,10))
