def product(*args):
    total = 1
    for number in args:
        total *= number
    
    return total

print(product(1,2,3,4,5,6))
