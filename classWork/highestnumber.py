highest = 0
count = 1
count_limit = 10
while count <= 10:
    number = int(input("Enter next score >> "))
    if number >= 1 and number <= 100:
        if number > highest:
            highest = number
        count += 1
    else:
        print("Number out of range")
print(highest)
        

