year = int(input("Input the year >> "))
result = str(year) + " is a leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else str(year) + " is not a leap year"
print(result)
