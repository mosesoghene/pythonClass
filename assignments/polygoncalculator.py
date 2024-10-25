import math

number_of_sides = int(input("input the number of sides on the polygon: "))
length_of_sides = int(input("input the length of one of the sides: "))

PI = 22/7

numerator = number_of_sides * length_of_sides ** 2
denominator =  4 * math.tan(PI / number_of_sides)

area = numerator / denominator

print(f"the area is: {area:.2f}")
