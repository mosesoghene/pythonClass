first_number = int(input("Enter three numbers \n> "))
second_number = int(input("> "))
third_number = int(input("> "))

print("Ascending" if first_number < second_number < third_number else "Descending" if third_number < second_number < first_number else "Neither")

