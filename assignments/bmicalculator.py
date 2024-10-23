weight_in_kilo = float(input("Enter weight in KG >> "))
height_in_meter = float(input("Enter height in meters >> "))

bmi = weight_in_kilo / (height_in_meter ** 2)

print(f"\nCurrent BMI: {bmi:.1f}")

if bmi < 18.5:
    print("You're Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You're Normal Weight")
elif bmi >= 25 and bmi <29.9:
    print("You're Overweight")
else:
    print("You're Obese")

