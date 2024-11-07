rows = 7


for row in range(1, rows+1):    
    print(" " * (rows - row), *list(range(row, 0, -1)), *list(range(2, row+1)), sep="")

