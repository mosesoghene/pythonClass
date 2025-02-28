def pascals_triangle(n):
    return [list(map(int, str(11 ** i ))) for i in range(n)]

print(pascals_triangle(5))
