base = 1
exponent = 2

power_times = 1
power_total = 1

print(f"a\tb\tpow(a, b)")
loop_count = 1
while loop_count <= 5:
    while power_times <= exponent:
        power_total *= base
        power_times += 1

    print(f"{base}\t{exponent}\t{power_total}")
    
    base += 1
    exponent += 1

    power_times = 1
    power_total = 1
    
    loop_count += 1
