from random import randint
import os
import time

        
passes = 0
fails = 0
answers = []

counter = 1

def get_numbers(start, stop):
    return (randint(start, stop), randint(start, stop))


while counter <= 10:
    time.sleep(1) 
    os.system("clear") 
  
    
    numbers = get_numbers(1,1000)
    if counter <= 5:
        response = int(input(f"Question {counter}:\n  what is {numbers[0]} + {numbers[1]}\n  > "))
        if response == (numbers[0] + numbers[1]):
            passes += 1
        else:
            fails += 1
            answers.append(f"\tQuestion {counter}: {numbers[0]} + {numbers[1]} = {numbers[0] + numbers[1]}")
    elif counter <= 8:
        response = int(input(f"Question {counter}:\n  what is {numbers[0]} x {numbers[1]}\n  > "))
        if response == (numbers[0] * numbers[1]):
            passes += 1
        else:
            fails += 1
            answers.append(f"\tQuestion {counter}: {numbers[0]} x {numbers[1]} = {numbers[0] * numbers[1]}")
    else:
        response = int(input(f"Question {counter}:\n  what is {numbers[0]} - {numbers[1]}\n  > "))
        if response == (numbers[0] - numbers[1]):
            passes += 1
        else:
            fails += 1
            answers.append(f"\tQuestion {counter}: {numbers[0]} - {numbers[1]} = {numbers[0] - numbers[1]}")
    
    counter += 1
else:
    os.system("clear")
        
    

print(f"RESULTS: \n\tTotal Passes: {passes}\n\tTotal Fails: {fails}\n\nANSWERS:\n")

for answer in answers:
    print(answer)
