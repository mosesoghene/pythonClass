rows = int(input("Enter a number: \n>  "))


for col in range(rows, 0, -1,):
    print(*list(range(col, 0, -1)), sep ="")



