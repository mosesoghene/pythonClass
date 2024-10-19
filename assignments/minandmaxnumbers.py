user_input = int(input("You are only allowed to enter positive integer numbers \nEnter 0 to stop and get results \nEnter number here >> "))

largest = user_input
smallest = user_input

while user_input != 0:
    if user_input > 0 and user_input > largest:
        largest = user_input
    
    if user_input < smallest :
        smallest = user_input
    
    user_input = int(input("\nYou are only allowed to enter positive integer numbers \nEnter 0 to stop and get results \nEnter number here >> "))
print(f"Smallest: {smallest} ==> Largest: {largest}")
