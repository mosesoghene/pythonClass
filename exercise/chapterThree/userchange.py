user_change = int(input("enter the change: "))

quarter = change // 25
remain = change % 25
dimes = remain // 10
pennies = remain % 10

print(f"> quarter: {quarter}\n> dimes: {dimes}\n> pennies: {pennies}")
