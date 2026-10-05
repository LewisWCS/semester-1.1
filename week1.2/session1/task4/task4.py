# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"} #{} is a set of unordered unique items
vegetables = {"leek", "tomato", "potato"}


# What do you think will be printed here?

both = fruit.intersection(vegetables) # finds the common variables and prints them
print(both)


# Why does the following code diplay five items?

food = fruit.union(vegetables) #combines the two sets into one ignoring duplicates
print(food)

# Add an item to fruit
fruit.add("strawberries")
print(fruit)
# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)

# Find and display symmetric difference of the two sets
fruit.symmetric_difference(vegetables)
print(fruit.symmetric_difference(vegetables)) #tells you the subset which doesnt have varibles in the other