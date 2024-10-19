base = float(input("Enter first number >> "))
exponent = float(input("Enter second number >> "))

power_times = 1
power = 1
while power_times <= exponent:
    power = power * base
    power_times += 1

print(f"{base} raised to the power of {exponent} => {power}")



