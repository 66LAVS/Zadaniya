import random

M = int(input("Количество строк"))
N  = int(input(" Количество столбцов"))

# Создаем двумерный массив с рандомными числами
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

# Выводим массив на экран
print("Массив A:")
for row in A:
    print(row)

# Находим минимальный и максимальный элементы
min_value = A[0][0]
max_value = A[0][0]
min_i = 0
min_j = 0
max_i = 0
max_j = 0
for i in range(M):
    for j in range(N):
        if A[i][j] < min_value:
            min_value = A[i][j]
            min_i = i
            min_j = j
        if A[i][j] > max_value:
            max_value = A[i][j]
            max_i = i
            max_j = j

# Меняем местами минимальный и максимальный элементы
A[min_i][min_j], A[max_i][max_j] = A[max_i][max_j], A[min_i][min_j]
print(A[min_i][min_j])
print(A[max_i][max_j])
# Выводим измененный массив на экран
print("\nИзмененный массив A:")
for row in A:
    print(row)
