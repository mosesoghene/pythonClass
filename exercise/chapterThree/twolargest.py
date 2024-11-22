import re

largest = 0
next_argest = 0
count = 10

def is_integer(number):
    return bool(re.match(r"^-?\d+$"))

def is_float(number):
    return bool(re.match("^-?\d+(\.\d+)$"))

while count > 0:
    number = input("Enter a number \n>  ")
    if is_integer(number):
        number = int(number)
    elif is_float(number):
        number = float(number)
    else:
        print(f"'{number}' is not a valid integer")
        
    if (number > largest):
        next_largest = largest;
        largest = number
        count -= 1
else:    
    print(f"Largest: {largest}, \nSecond Largest: {next_largest}")
