try:
    def read_number():
        line = input("Enter some numbers, separated by spaces: ")
        numbers = [float(item) for item in line.split()]
        return numbers
    
    set = read_number()
    set_mean = sum(set) / len(set)
    set_median = sorted(set)[len(set) // 2]

    print(f"minimum = {min(set)}" "\n" f"maximum = {max(set)}" "\n" f"mean = {set_mean:.1f}" "\n" f"median = {set_median}")
except ValueError:
    import sys
    sys.exit("Error: no numbers provided")
