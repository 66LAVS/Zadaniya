import random


M = int(input("Количество строк"))
N  = int(input(" Количество столбцов"))

# Создаем двумерный массив с рандомными числами
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

# Выводим массив на экран
print("Массив A:")
for row in A:
    print(row)

# Вычисляем среднее арифметическое каждого столбца
for j in range(N):
    sum_column = 0
    for i in range(M):
        sum_column += A[i][j]
    average = sum_column / M
    print(f"Среднее арифметическое столбца {j}: {average:.2f}")
