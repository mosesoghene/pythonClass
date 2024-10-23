user_input = int(input("Enter a 3 digit integer >> "))
min_cut_off = 99
max_cut_off = 1000
if user_input > min_cut_off and user_input < max_cut_off:
    if (user_input % 10) == (user_input // 100):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
else:
    print("Number out of range")
