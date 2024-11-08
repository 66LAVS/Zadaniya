N  = int(input(" Количество столбцов"))

# Создаем массив для треугольника Паскаля
pascal_triangle = [[0 for _ in range(i + 1)] for i in range(N)]

# Заполняем массив
for i in range(N):
    pascal_triangle[i][0] = 1 # Крайние элементы всегда равны 1
    pascal_triangle[i][i] = 1 # Крайние элементы всегда равны 1
    for j in range(1, i):
        pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

# Выводим треугольник Паскаля
print("Треугольник Паскаля:")
for row in pascal_triangle:
    print(row)
