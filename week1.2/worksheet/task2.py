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

    print(min(set))
    print(max(set))
    print(f"{set_mean:.1f}")
    print(set_median)
          
except ValueError:
    import sys
    sys.exit("Error!")
