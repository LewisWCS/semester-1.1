# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["computer"] = "science" # this adds new value
rivers["name"] = "lewis"
print(rivers)
# Display all the keys
print(rivers.keys()) # prints the keys and not the value

# Display all the values
print(rivers.values()) # prints all the values
# Display all the key:value pairs, as tuples
print(rivers.items())
# Delete an entry from the rivers database
rivers.pop("Leeds") # this got rid of the entry Leeds(this also mean the value)
print(rivers)
