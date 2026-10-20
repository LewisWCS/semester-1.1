"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Lewis White
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
maxtime = int(input("Please enter an integer bigger than one: "))  # read an integer number of steps (>0)

state_order = ["red", "red_amber", "green", "amber"]  # the order of the states

systime = 0
state_index = 0 
state = state_order[state_index]
time_in_state = 0  # how long we have been in the current state

for i in range(maxtime):
    systime += 1
    time_in_state += 1
    if time_in_state >= states[state]:
        state_index += 1
        if state_index >= len(state_order):
            state_index = 0

        state = state_order[state_index]
        time_in_state = 0
    print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14