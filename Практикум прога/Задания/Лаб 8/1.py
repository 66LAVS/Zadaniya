import random 

def generate_num(length): 
    # Генерируем уникальное число заданной длины
    digits = random.sample(range(0, 10), length)   
    if digits[0] == 0:  
        # Если первая цифра 0, меняем её с первой ненулевой цифрой
        digits[0], digits[1] = digits[1], digits[0] 
    return ''.join(map(str, digits))  # Преобразуем список цифр в строку

def get_bulls_and_cows(guess, secret): 
    bulls = 0  # Счётчик для быков
    cows = 0   # Счётчик для коров
    for i in range(len(guess)): 
        if guess[i] == secret[i]:   
            # Увеличиваем количество быков, если цифры совпадают по месту
            bulls += 1 
    for digit in guess: 
        if digit in secret:   
            # Увеличиваем количество коров, если цифра есть в числе, но не на своем месте
            cows += 1 
    cows -= bulls  # Учитываем, что быки не являются коровами
    return bulls, cows  # Возвращаем количество быков и коров

length = int(input("Введите длину числа (от 1 до 10): "))  # Запрашиваем у пользователя длину числа

secret_number = generate_num(length)  # Генерируем загаданное число
print(secret_number)  # Выводим загаданное число (для отладки)

print(f"Загаданное число состоит из {length} уникальных цифр.") 

while True: 
    guess = input(f"Попробуйте угадать число (длина {length}): ")  # Запрашиваем ввод от пользователя
    
    bulls, cows = get_bulls_and_cows(guess, secret_number)  # Получаем количество быков и коров
    
    print(f"Быки: {bulls}, Коровы: {cows}")  # Выводим результат
    
    if bulls == length:   
        # Если все цифры угаданы, поздравляем пользователя
        print(f"Поздравляю! Вы угадали число {secret_number}") 
        break  # Выходим из цикла
