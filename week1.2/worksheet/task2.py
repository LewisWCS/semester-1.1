try:
    def read_number():
        line = input("enter a number: ")
        number = float(line)
        return number

    num1 = read_number()
    num2 = read_number()
    num3 = read_number()
    num4 = read_number()
    num5 = read_number()
    set = [num1, num2, num3, num4, num5]
    set_mean = sum(set) / len(set)
    set_median = sorted(set)[len(set) // 2]

    print(f"minimum = {min(set)}")
    print(f"maximum = {max(set)}")
    print(f"mean = {set_mean:.1f}")
    print(f"median = {set_median}")

except ValueError:
    import sys
    sys.exit("Error: no numbers provided")
