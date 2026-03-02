size = 7
matrix = [[1 for _ in range(size)] for _ in range(size)]

for i in range(size):
    # Визначаємо кількість нулів для кожного рядка за шаблоном варіанту 19
    if i <= size // 2:
        count = i + 1
    else:
        count = size - i
    
    for j in range(count):
        matrix[i][j] = 0

for row in matrix:
    print(*(row))