user_input = input("enter a binary number: ")

decimal_number = 0

iteration = len(user_input) - 1

while iteration >= 0:
    digit = int(user_input[iteration])
    power = len(user_input) - iteration - 1
    decimal_number += digit * 2 ** power
    iteration -= 1
else:
    print(f"Decimal number: {decimal_number}")
