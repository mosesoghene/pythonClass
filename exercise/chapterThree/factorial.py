number = int(input("Enter a number to find its factorial \n> "))
total = number
for num in range(number, 1, -1):
    total *=  num - 1

print(total)
