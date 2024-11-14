A = float(input("Введите цену конфет: "))
ct = 1.0

for i in range(1, 7): # 10 итераций цикла
 price = A * ct
 print(f"{price:.1f} цена за {ct:.1f} кг конфет") # Форматирование до десятых
 ct += 0.2
