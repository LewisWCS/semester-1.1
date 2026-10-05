# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
shopping.remove("bananas")
# shopping.insert([4], "grapes") # fix later # remove the []
shopping.append("grapes")
print(shopping)

# Add yoghurt, just after milk
shopping.insert(1, "yogurt") # the first starts with 0 and then position 2 is 1
print(shopping)