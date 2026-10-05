# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry") # A tuple variable cannotbe replaced, and has () not []

print(fruit)

# Find and display position of "banana"
print(fruit[1])

# Display how many times "cherry" occurs
fruit.count("cherry") # if you put this in a print function it will then tell you
print(fruit.count("cherry"))
# Display how many times "strawberry" occurs
print(fruit.count("strawberries")) # do an if statement
# Unpack tuple into variables
(apple, banana, cherry) = fruit
print(apple)

