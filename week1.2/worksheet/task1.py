try:
    grade = int(input("Please enter a value between 0-100: "))
    if grade <= 39:
        print("Fail")
    elif grade >= 40 and grade <=69:
        print("Pass")
    elif grade >= 70 and grade <= 100:
        print("Distinction")
    else:
        import sys
        sys.exit("Error!")
except ValueError:
    import sys
    sys.exit("Error!")

