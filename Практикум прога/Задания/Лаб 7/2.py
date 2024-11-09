def nok(a, b):
    z = 2
    while (z <= a) and (z <=3):
        if (a % z == 0) and (b % z ==0):
            return z
            break 
        z += 1

            



# Пример использования функции
a = int(input("Введите a"))
b = int(input("Введите b"))

nok1 = nok(a,b)
print(f"НОК чисел {a} и {b}: {nok1}")
