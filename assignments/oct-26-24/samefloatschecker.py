first_input = float(input("Enter a decimal digit >> "))
second_input = float(input("Enter another decimal digit >> "))

response = "They are same" if round(first_input, 3) == round(second_input, 3) else "They are different"

print(response)

