import re

def isint(data):
    return bool(re.match(r'^-?\d+$', data))

def isfloat(data):
    return bool(re.match(r"^-?\d+(\.\d+)$", data))

number = input("enter a number \n>  ")

if isint(number):
    number = int(number)
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")
elif isfloat(number):
    number = float(number)
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")
else:
    print("Invalid input")



    



