rows = int(input("Enter a number: \n>  "))

for row in range(1, rows + 1):
    for _ in range(1, row + 1):
        print("*", end = "")
    print()

for row in range(1, rows + 1):
    print("*" * row)

