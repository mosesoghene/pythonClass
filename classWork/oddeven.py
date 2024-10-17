data = int(input("enter number between 100 - 999 >> "))

if data > 99 and data < 1000:
    last_num = data % 10
    temp_data = data // 10
    mid_num = temp_data % 10
    first_num = temp_data // 10
    
    odd = even = 0
    
    if first_num % 2 == 0:
        even += 1
    else:
        odd += 1
    
    if mid_num % 2 == 0:
        even += 1
    else:
        odd += 1
        
    if last_num % 2 == 0:
        even += 1
    else:
        odd += 1
        
    print(f"{odd} odd numbers \n{even} even numbers")
else:
    print(f"{data} is out of range!")
