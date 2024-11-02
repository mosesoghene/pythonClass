number = int(input("Enter a number"))
numbers = []
if number < 100000 and number > 9999:
    for i in range(5):
        numbers.insert (0, number % 10)
        number //= 10
    
    for num in numbers:
        print(num, end = " ")
    print()
else:
    print("input is not a 5 digit integer")
