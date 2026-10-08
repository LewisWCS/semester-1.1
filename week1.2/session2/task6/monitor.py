# Week 1.2, Session 2: Task 6
try:
    print("please tell me if your System is")
    print("1: Operating")
    print("0: Not operating")
    system = int(input("Please enter 1 or 0:"))
    if system == 0:
        print("Please turn the system on")
    elif system ==1:
        temp = int(input("What is the temperature of the system: "))
    else:
        print("Invalid information!")

except ValueError:
    print("Invalid information!")
# This section is gathering information about whether the system is operating or not, it also asks about the temperature(interger)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    if temp > 80:
        print("The operating machine is too high, please shut it down")
    elif temp > 50 and temp <80:
        print("The temperature is within safe limits!")
        psi = int(input("What is the PSI:"))
    elif temp < 50:
        print("The temperature is low, no action needed!")
        psi = int(input("What is the PSI:"))
    else:
        print("Invalid information!")

except ValueError:
    print("Invalid information!")
# This section talks about the temperature and also also asks about the psi(interger)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    if psi > 100:
        print("High pressure is detected, maintanence is required!")
    elif psi > 70 and psi < 100:
        print("The pressure is stable!")
    elif psi < 70:
        print("Pressure is low and the system is operating correctly!")
    else:
        print("Invalid information!")
except ValueError:
    print("Invalid information!")
#------------------------------------------------------------------------------------------------------------------------------------
if system == 1 and temp < 80 and psi < 100:
    print("The system is operating correctly!")




    












