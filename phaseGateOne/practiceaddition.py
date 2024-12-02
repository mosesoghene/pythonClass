from random import randint

first_number = randint(0, 100)
second_number = randint(0, 100)

user_input = input(f"What is {first_number} + {second_number} \n> ")

def check_answer(user_input, first_number, second_number):
    return True if user_input.isdigit() and int(user_input) == first_number + second_number else False 

print(check_answer(user_input, first_number, second_number))
