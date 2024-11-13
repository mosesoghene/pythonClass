def average(first_number, *args):
    total = first_number
    divisor = len(args) + 1
    
    for number in args:
        total += number
    
    return total / divisor
