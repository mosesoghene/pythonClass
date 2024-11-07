def sum_of_multiples(x, n):
    total = 0
    for num in range(x, n+1):
        total = (total + num) if num % x == 0 else (total + 0)
    
    return total

print(sum_of_multiples(3, 10))

