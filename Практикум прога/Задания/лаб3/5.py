A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B (B > A): "))

# Проверка условия A < B
if A >= B:
    print("Ошибка: A должно быть меньше B.")
else:
    # Цикл for для вывода чисел от A до B
    for i in range(A, B + 1):
        # Вывод числа i нужное количество раз
        for j in range(i - A + 1):
            print(i, end=" ")
