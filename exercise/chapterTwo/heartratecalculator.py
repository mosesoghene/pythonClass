age = input("Enter age >> ")

if age.isdigit():
    age = int(age)
    heart_rate = 220 - age
    min_rate = heart_rate * 0.5
    max_rate = heart_rate * 0.85
    
    print(f"Minimum heart rate :{min_rate} <> Maximum heart rate : {max_rate}")
else:
    print(f"{age} Invalid. Not a valid integer.")
