from random import randint
import os
import time

def get_numbers():
    return (randint(1,10), randint(1,10))

def get_question(numbers):
    os.system("clear")
    
    response = input(f"What is {numbers[0]} times {numbers[1]} ?\n> ")
    if response.isdigit():
        if int(response) == numbers[0] * numbers[1]:
            print("That's Correct")
        else:
            print("You can do better")
    else:
        print(f"{response} is not a valid integer")
        

while True:

    time.sleep(3)    
    os.system("clear")
    
    response = input("Get question? Y/N\n> ").lower()
    if response == "y":
        get_question(get_numbers())
    else:
        break
