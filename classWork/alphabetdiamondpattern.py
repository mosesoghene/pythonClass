rows = int(input("Input the number (middle number of rows): "))

for i in range(1, rows + 1):
    
    print(" " * (rows - i), end="")
    
    
    for j in range(1, i + 1):
        print(chr(64 + j), end="")


    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()

    
    
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")


    for j in range(1, i + 1):
        print(chr(64 + j), end="")


    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()



    
