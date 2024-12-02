"""
prompt user to enter number between 0 and 1000
save input as user_input (type string type)
check if user_input is a valid digit and is less than 1000 and greater than 0
map of user_input and cast each character to int type, sum the numbers
"""
user_input = input("Enter a number between 0 and 1000 \n> ")

def sum_digits_of(number):
    if number.isdigit() and int(number) < 1000 and int(number) > 0:
        return sum(map(lambda x: int(x), number))
    raise ValueError


print(sum_digits_of(user_input))
        
