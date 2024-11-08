N = int(input())

# Создаем массив A[N, N]
A = [[0 for _ in range(N)] for _ in range(N)]

# Заполняем массив
for i in range(N):
    for j in range(N):
        A[i][j] = i + j

# Выводим массив на экран
print("Массив A:")
for row in A:
    print(row)
