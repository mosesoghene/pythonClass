range_start = input("Enter range start number: ")
range_stop = input("Enter range stop number: ")
divisor = input("Enter divisor number: ")

count = 0
if range_start.isdigit() and range_stop.isdigit() and divisor.isdigit():
    range_start = int(range_start)
    range_stop = int(range_stop)
    divisor = int(divisor)
    for number in range(range_start, range_stop):
        if number % divisor == 0:
            count += 1
    print(count)
else:
    print("Invalid input")
    

