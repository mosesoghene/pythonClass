negative_counter = 0
positive_counter = 0
zero_counter = 0

number_counter = 1

while number_counter <= 5:
    number = int(input("Enter an integer number >> "))
    
    if number < 0:
        negative_counter += 1
    elif number == 0:
        zero_counter += 1
    else:
        positive_number += 1
    
    number_counter += 1

