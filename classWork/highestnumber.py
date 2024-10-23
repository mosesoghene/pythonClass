highest = 0

max_value = 100
min_value = 1
 
count_limit = 10
count = 1
while count <= count_limit:
    number = int(input("Enter next score >> "))
    if number >= min_value and number <= max_value:
        if number > highest:
            highest = number
        count += 1
    else:
        print("Number out of range")
        
print(highest)
        

