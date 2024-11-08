#В массиве случайных целых чисел поменять местами минимальный и 
#максимальный элементы. 

import random
import math

array = []

n = int(input("Введите размер массива: "))
for i in range(n):
    array.append(random.randint(-10, 10))


min = array[0]
max = array[0]
max_pos = -1
min_pos = -1
print(array)
for num in range(0,len(array)):
    if array[num] < min:
        min = array[num]
        min_pos = num
    if array[num] > max:
        max = array[num]
        max_pos = num

print(min_pos)
print(max_pos)
array[min_pos],array[max_pos] = array[max_pos] ,array[min_pos]
    
print(array)








