try:
    def read_number():
        line = input("Enter some numbers, separated by spaces: ")
        numbers = [float(item) for item in line.split()]
        return numbers
    
    numbers = read_number()

    if len(numbers) == 0:
        import sys
        sys.exit("Error: no numbers provided")
    
    number_mean = sum(numbers) / len(numbers)
    number_median = sorted(numbers)[len(numbers) // 2]

    print(f"Minimum = {min(numbers)}" "\n" f"Maximum = {max(numbers)}" "\n" f"Mean = {number_mean:.1f}" "\n" f"Median = {number_median}")
except ValueError:
    import sys
    sys.exit("Error: no numbers provided")
