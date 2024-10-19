first_number = float(input("Enter first number >> "))
second_number = float(input("Enter second number >> "))

sum_of_exponents = 0

while second_number > 0:
    sum_of_exponents = first_number * first_number
    second_number -= 1

print(f"{first_number} raised to the power of {second_number} => {sum_of_exponents}")
