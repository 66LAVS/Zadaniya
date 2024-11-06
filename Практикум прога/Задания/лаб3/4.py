N = int(input("Введите целое число N (N > 1): "))

A1 = 1
A2 = 2

print(A1, end=" ")
print(A2, end=" ")

for k in range(3, N + 1):
    AK = (A1 + 2 * A2) / 3
    print(AK, end=" ")
    A1 = A2
    A2 = AK