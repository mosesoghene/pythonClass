"""
prompt user to enter first, second, and third number
use the .sort() list method to sort the list, 
print results
"""

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
third_number = input("Enter third number: ")

def sort_numbers(*numbers):
    return sorted([number for number in map(lambda number: int(number), numbers)])

print(*sort_numbers(first_number, second_number, third_number), sep=",")

