def maxof(a, b, c):

  

  # Используем тернарный оператор для краткости
  maximum = a if a > b else b
  maximum = maximum if maximum > c else c
  return maximum

# Пример использования функции
a = int(input("Введите a"))
b = int(input("Введите b"))
c = int(input("Введите c"))

max_value = maxof(a, b, c)

print(f"Наибольшее значение: {max_value}")
