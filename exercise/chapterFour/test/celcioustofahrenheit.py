def celcious_to_fahrenheit(value):
    fahrenheit = (9 / 5) * value + 32
    return fahrenheit


def celcious_to_fahrenheit_table():
    result = f"Celcious to fahrenheit \n"
    for c in range(0, 101):
        result += f"{c:>3} : {round(((9 / 5) * c + 32), 1):>3}"        
    
        print(f"{c:>3} : {round(((9 / 5) * c + 32), 1):>3}")
    
    return result
        

