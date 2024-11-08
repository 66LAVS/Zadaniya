#Найти номер минимального по модулю элемента массива.  

import random
import math

array = []

n = int(input("Введите размер массива: "))
for i in range(n):
    array.append(random.randint(-10, 10))


min = abs(array[0])
print(array)
for num in array:
    if abs(num) < min:
        min = abs(num)

    

print(f"{min}")








