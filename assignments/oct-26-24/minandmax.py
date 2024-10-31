import re


numbers = input("Enter all numbers separated by a space i.e 12 -3 67 \n> ").split(" ")


def is_number(value) -> bool:
    return bool(re.match(r'^-?\d+(\.\d+)?$', value))

def min_max_of(array):
    largest = 0;
    smallest = 0;
    
    for number in array:
        if is_number(number):
            if float(number) > largest:
                largest = float(number)
            elif float(number) < smallest:
                smallest = float(number)
        else:
            print(f"'{number}' is not a digit")
    else:
        print(f"\nLargest: {largest} \nSmallest: {smallest}")


min_max_of(numbers)
