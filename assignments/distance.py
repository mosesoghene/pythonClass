from math import radians, sin, cos, acos

latitude_one = float(input("Enter latitude 1: "))
latitude_two = float(input("Enter latitude 2: "))
longitude_one = float(input("Enter longitude 1: "))
longitude_two = float(input("Enter longitude 2: "))

EARTH_RADIUS = 6371.01
distance = EARTH_RADIUS * acos(sin(radians(latitude_one)) * sin(radians(longitude_one)) + cos(radians(latitude_one)) * cos(radians(longitude_one)) * cos(radians(longitude_one) - radians(longitude_two)))

print(distance)

