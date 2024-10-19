first_number = input("Enter first number >> ")
second_number = input("Enter second number >> ")

first_number = float(first_number)
second_number = float(second_number)
sum_of_numbers = first_number + second_number

print(f"Sum of {first_number} + {second_number} => {sum_of_numbers}")


continue_program_prompt = input("Do you want to continue? (Yes(Y) or No(N) >> ").lower()

while (continue_program_prompt == "yes") or (continue_program_prompt == "y"):
    first_number = input("Enter first number >> ")
    second_number = input("Enter second number >> ")

    first_number = float(first_number)
    second_number = float(second_number)
    sum_of_numbers = first_number + second_number

    print(f"Sum of {first_number} + {second_number} => {sum_of_numbers}")
    

    continue_program_prompt = input("Do you want to continue? (Yes(Y) or No(N) >> ").lower()
