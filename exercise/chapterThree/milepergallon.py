miles_driven = 0
gallons = 0
ultimate_miles = 0
miles_per_galon = 0

cut_off = 0

while cut_off != -1:
    miles_driven = float(input("\nenter miles driven \n>  "))
    gallons = float(input("enter gallons: \n>  "))
    miles_per_galon = miles_driven / gallons
    ultimate_miles += miles_per_galon
    print(miles_per_galon)
    cut_off = int(input("\nenter -1 to quit or 0 to continue: \n>  "))
else:
    print(ultimate_miles)
