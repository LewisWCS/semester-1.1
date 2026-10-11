try:    
    def read_number():
        line = input("Enter a number: ")
        number = float(line)
        return number
    print(read_number())
except ValueError:
    print("Invalid input. Please enter a valid number.")