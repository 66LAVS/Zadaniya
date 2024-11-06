import random
n = int(input("Введите размер массива: "))

# Ввод элементов массива
array = []
print("Введите элементы массива:")
for i in range(n):
    array.append(random.randint(-10, 10))

# Поиск максимального элемента с четным индексом
max_even_index = 0
max_even_value = array[0]
print(array)
for i in range(0, len(array), 2):
    if array[i] > max_even_value:
        max_even_value = array[i]
        max_even_index = i

print(f"Максимальный элемент с четным индексом: {max_even_value} (индекс {max_even_index})")
