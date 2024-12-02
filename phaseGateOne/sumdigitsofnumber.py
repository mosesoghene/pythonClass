user_input = input("Enter a number between 0 and 1000 \n> ")

def sum_digits_of(number):
    if number.isdigit() and int(number) < 1000 and int(number) > 0:
        return sum(map(lambda x: int(x), number))
    raise ValueError


print(sum_digits_of(user_input))
        
