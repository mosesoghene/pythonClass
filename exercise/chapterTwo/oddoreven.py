data = input("Enter a number >> ")
if data.isdigit() or data.isdecimal():
    data = float(data)
    if data % 2 == 0:
        print(f"{data} is an even number")
    else:
        print(f"{data} is an odd number")
else:
    print(f"{data} is not a number")
