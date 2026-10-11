try:
    grade = int(input("Please enter a value between 0-100: "))
    if grade <= 39:
        print(f"{grade} is a Fail")
    elif grade >= 40 and grade <=69:
        print(f"{grade} is a Pass")
    elif grade >= 70 and grade <= 100:
        print(f"{grade} is a Distinction")
    elif grade <0 or grade > 100:
        import sys
        sys.exit("Error: grade must be an integer between 0-100")
except ValueError:
    import sys
    sys.exit("Error: grade must be an integer between 0-100")

