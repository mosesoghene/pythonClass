numbers = input("Enter 3 decimal numbers separated by space(E.G. 1.3 16.45 36.21) >> ").split()
sorted_numbers = []

for number in numbers:
    for data in numbers:
        if float(number) > float(data):
            sorted_numbers.append(float(number))
        else:
            sorted_numbers.insert(0, number)
    

print(sorted_numbers)
