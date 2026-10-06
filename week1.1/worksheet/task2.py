"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
print("We will calculate how much you will save in a year")
try:
    num1 = int(input("Please enter the amount you want to save every month:"))
except:
    print("please enter a number only")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
save = num1 * 12 
print(save, "will be saved for the year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
interest = save * 0.008
total = interest + save
print(f"This is the amount you will have after interest,£{total:.0f}")