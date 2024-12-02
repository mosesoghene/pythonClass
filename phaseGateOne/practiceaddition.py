"""
generate random number (1 - 100)
save to variable first_number
generate random number (1 - 100)
save to variable first_number

declare function check_answer with params: user_input, first_number, second_number
    check if user_input is a valid number
    check if user_input == first_number + second_number
    function should return True if above check is true else False
"""

from random import randint

first_number = randint(0, 100)
second_number = randint(0, 100)

user_input = input(f"What is {first_number} + {second_number} \n> ")

def check_answer(user_input, first_number, second_number):
    return True if user_input.isdigit() and int(user_input) == first_number + second_number else False 

print(check_answer(user_input, first_number, second_number))
