# there are several errors in this code
# run the code, read the error messages or look at the output, and fix the problems

# Find and fix the errors

#name = input("Enter your name: ")     # The word input was spelt wrong
#age = int(input("Enter your age: "))       # Int function was around the variable age and not next to input
#city = input("Enter your city: ")

#print(f"Hello {name}, you are {age} years old and live in {city}.")       #didnt use the f string function, inbetween the print and "Hello"

try:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a second number: "))
    answer = num1 + num2 
    print(f"{num1} + {num2} = {answer}")
except:
    print("Please enter numbers only.")