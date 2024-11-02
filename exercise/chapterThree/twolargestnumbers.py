numbers = []

for i in range(1,11):
    num = int(input(f"Enter number {i} \n> "))
    numbers.append(num)

large1 = max(numbers)
numbers.pop(numbers.index(large1))
large2 = max(numbers)

print(large1, large2)
    
    
