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
    
    sorted_numbers = sorted(numbers)
    
    if len(sorted_numbers) % 2 == 1:
        number_median = sorted_numbers[len(sorted_numbers) // 2]
    else:
        middle1 = sorted_numbers[len(sorted_numbers) // 2 - 1]
        middle2 = sorted_numbers[len(sorted_numbers) // 2]
        number_median = (middle1 + middle2) / 2

    print(f"Minimum = {min(numbers)}" "\n" f"Maximum = {max(numbers)}" "\n" f"Mean = {number_mean:.1f}" "\n" f"Median = {number_median}")
except ValueError:
    import sys
    sys.exit("Error: no numbers provided")
