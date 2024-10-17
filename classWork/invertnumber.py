data = int(input("enter number between 100 - 999 >> "))

if data > 99 and data < 1000:
    last_num = data % 10
    temp_data = data // 10
    mid_num = temp_data % 10
    first_num = temp_data // 10
    print(f"{data} inverted is >> {last_num}, {mid_num}, {first_num}")
else:
    print(f"{data} is out of range!")
