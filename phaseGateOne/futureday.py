"""
prompt user to enter today day
prompt user to enter future_day
check if input is a valid number from 0 - 6
determine future day: (today + future day) % 7
print corresponding today and future day
"""


today = input("Enter today's day(0 - 6): ")
days_elapsed = input("Enter the number of days elapsed since today: ")
WEEKDAYS = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

if today.isdigit() and days_elapsed.isdigit():
    if int(today) >= 0 and int(today) <= 6:
        future_day = (int(today) + int(days_elapsed)) % 7
        print(f"Today is {WEEKDAYS[int(today)]} and the future day is {WEEKDAYS[int(future_day)]}")
    else:
        print("invalid day entered. ")
else:
    print("Invalid input, input not a valid digit!!!")
            



