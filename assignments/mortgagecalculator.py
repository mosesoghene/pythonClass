principal = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
year_duration = int(input("Enter the duration in years: "))

monthly_rate = (annual_interest_rate / 100) / 12
month_duration = year_duration * 12
 
monthly_payment = principal * monthly_rate * ((1 + monthly_rate) ** month_duration) / (((1 + monthly_rate) ** month_duration) - 1)

print(f"Your monthly payment is ${monthly_payment:.2f}")

