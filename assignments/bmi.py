user_weight = float(input("Enter weight in pounds: "))
user_height = float(input("Enter weight in inches: "))

weight = user_weight * 0.45359237
height = user_height * 0.0254

bmi = weight * (height ** 2)
print("BMI is", bmi)

