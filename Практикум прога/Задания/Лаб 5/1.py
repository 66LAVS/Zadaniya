import random

array = []

n = int(input("Введите размер массива: "))
for i in range(n):
    array.append(random.randint(-10, 10))

# Вычисление суммы четных положительных элементов
sum = 0
print(array)
for num in array:
    if num > 0 and num % 2 == 0:
        sum += num

print(f"Сумма четных положительных элементов: {sum}")








