import random

QUESTIONS = 10
QUESTION = 1
total_score = 0
total_fails = 0

while QUESTION <= QUESTIONS:
    left_operand = random.randint(1, 20)
    right_operand = random.randint(1, 20)
    operator = random.choice(["+", "-", "*", "/"])
    user_input = input(f"Questions {QUESTION}: {left_operand} {operator} {right_operand} = ")

    while user_input == "":
        user_input = input(f"Questions {QUESTION}: {left_operand} {operator} {right_operand} = ")
    else:
        response = float(user_input)

    if operator == "+":
        answer = left_operand + right_operand
    elif operator == "-":
        answer = left_operand - right_operand
    elif operator == "*":
        answer = left_operand * right_operand
    elif operator == "/":
        answer = left_operand / right_operand

    if response == answer:
        total_score += 1
        print("Correct!")
    else:
        total_fails += 1
        print(f"Incorrect! Answer is {answer}.")

    QUESTION += 1
else:
    print("*" * 17)
    print(f"Total score is {total_score}")
    print(f"Total fails is {total_fails}")
    print("*" * 17)