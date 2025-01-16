"""
prompt user to enter first, second, and third number
declare a function with n-args
loop over each data and add them to a list using list comprehension
use the sorted() function to sort the list, 
print results
"""

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
third_number = input("Enter third number: ")

def sort_numbers(*numbers):
    return sorted([number for number in numbers])

print(*sort_numbers(first_number, second_number, third_number), sep=",")

