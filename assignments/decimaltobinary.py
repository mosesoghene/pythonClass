user_input = input("Input a Decimal Number: ")


result = ""
whole_number = 0
BINARY_CONST = 2
if user_input.isdigit():
    whole_number = int(user_input)
    while whole_number > 0:
        remainder = whole_number % BINARY_CONST
        whole_number //= BINARY_CONST
        
        result = str(remainder) + result
    else:
        print(f"Binary number is: {result}")
else:
    print("Invalid input")
