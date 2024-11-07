number = int(input("Enter a number: \n>  "))

for i in range(1, number +1): print(" " * (number - i) ,*list(range(i, 0, -1)), *list(range(2, i+1)), sep="")    

for i in range(number-1, 0,  -1):    print(" " * (number-i), *list(range(i, 0, -1)), *list(range(2, i+1)), sep="")

