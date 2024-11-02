num1 = input("Enter an integer >> ")
num2 = input("Enter an integer >> ")
num3 = input("Enter an integer >> ")

if num1.isdigit() and num2.isdigit() and num3.isdigit():
    num1, num2, num3 = int(num1), int(num2), int(num3)
    total = num1 + num2 + num3
    average = total / 3
    product = num1 * num2 * num3
    
    smallest = 0
    largest = 0
    
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num3:
        largest = num2
    else:
        largest = num3
        
    
    if num1 < num2 and num1 < num3:
        smallest = num1
    elif num2 < num3:
        smallest = num2
    else:
        smallest = num3
        
    print(f"""
        Total: {total} 
        Avearge: {average}
        Product: {product}
        Smallest: {smallest}
        Largest: {largest}
""")
else:
    print(f"{num1} Or {num2} or {num3} is not an integer")



    
    
