"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Lewis White
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
maxtime = int(input("Enter an integer: "))  # read an integer number of steps (>0)

state_order = ["red", "red_amber", "green", "amber"]  # the order of the states

systime = -1
state_index = 0 
state = state_order[state_index]
time_in_state = 0  # how long we have been in the current state

for i in range(maxtime + 1):
    systime += 1
    print(f"Time {systime:03} State {state}")
    time_in_state += 1
    if time_in_state >= states[state]:
        state_index = (state_index + 1) % len(state_order)
        state = state_order[state_index]
        time_in_state = 0

    

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14