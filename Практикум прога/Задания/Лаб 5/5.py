#Определить, какое число в массиве встречается чаще всего.

import random
import math

array = []

n = int(input("Введите размер массива: "))
for i in range(n):
    array.append(random.randint(-10, 10))

count = 0
max_count = 0
ib = 90
print(array)
for i in range(0,len(array)): 
    for num in range(0,len(array)):
        if array[num] == array[i]:
            count += 1
    if count >  max_count:
        max_count = count
        ib = array[i]
    count = 0


print(max_count) 
print(ib)
