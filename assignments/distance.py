import math

latitude_one = float(input("input the latitude of coordinate 1: "))
longitude_one = float(input("input the longitude of coordinate 1: "))
latitude_two = float(input("input the latitude of coordinate 2: "))
longitude_two = float(input("input the longitude of coordinate 2: "))

latitude_one = math.radians(latitude_one)
longitude_one = math.radians(longitude_one)
latitude_two = math.radians(latitude_two)
longitude_two = math.radians(longitude_two)

EARTH_RADIUS = 6371.01
distance = EARTH_RADIUS * math.acos((math.sin(latitude_one) * math.sin(latitude_two)) + math.cos(latitude_one) * (math.cos(latitude_two) * math.cos(longitude_one - longitude_two)) )

print(f"the distance between those points is: {distance:.13f} km")
