from datetime import date

year = int(input("Enter Year > "))
month = int(input("Enter month > "))
day = int(input("Enter day > "))

for i in range(0, 12):
    this_month_date = date(year, month+i, day)
    ovulation_date = date(year, month+i, day+ 14)
    
    safe_period_before_ovulation_start = date(year, month+i, day+ 21)
    safe_period_before_ovulation_end = date(year, month+i, day+ 24)
    
    fertile_window_start = date(year, month+i, day+ 23)
    fertile_window_start = date(year, month+i, day+ 24)
    
