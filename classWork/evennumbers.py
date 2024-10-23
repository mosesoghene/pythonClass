for i in range(1, 100):
    if i % 2 == 0:
        print(i, end=" - ")
print("\n===========================")

even = [i for i in range(1, 100) if i % 2 == 0]
print(even)
