import random
import math

def find_maximum(arr):
   
    max_value = arr[0]  
    for num in arr:
        if num > max_value:  
            max_value = num
    return max_value

array = []

n = int(input("Введите размер массива: "))
for i in range(n):
    array.append(random.randint(-10, 10))

print(array)

max_value = find_maximum(array)
print(f"Максимальное значение в массиве: {max_value}")