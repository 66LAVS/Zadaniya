import random

M = int(input("Количество строк"))

N  = int(input(" Количество столбцов"))

# Создаем двумерный массив с рандомными числами
array = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

# Выводим массив на экран
print("Массив array:")
for row in array:
    print(row)

# Находим и выводим элементы, кратные 5, с их индексами
print("\nЭлементы, кратные 5:")
for i in range(M):
    for j in range(N):
        if array[i][j] % 5 == 0:
            print(f"array[{i}][{j}] = {array[i][j]}")
