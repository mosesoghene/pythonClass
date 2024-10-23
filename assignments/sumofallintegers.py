# Exercise 2.6

user_number = int(input("Enter integer between 0 - 1000 >> "))

min_cut_off = 0
max_cut_off = 1000

if user_number > min_cut_off and user_number < max_cut_off:
    if user_number > 99:
        first_number = user_number // 10 % 10
        second_number = user_number // 10 % 10
        third_number = user_number % 10
        total = first_number + second_number + third_number
    else:
        first_number = user_number // 10
        second_number = user_number % 10
        
        total = first_number + second_number
else:
    print("Number out of range")
print(total)

