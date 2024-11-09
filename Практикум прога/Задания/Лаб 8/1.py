import random

def generate_num(length):
    
    digits = random.sample(range(0, 10), length)  
    if digits[0] == 0: 
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits))

def get_bulls_and_cows(guess, secret):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:  
            bulls += 1
    for digit in guess:
        if digit in secret:  
            cows += 1

    cows -= bulls 

    return bulls, cows



length = int(input("Введите длину числа (от 1 до 10): "))

secret_number = generate_num(length)
print(secret_number)


print(f"Загаданное число состоит из {length} уникальных цифр.")
    
while True:
    guess = input(f"Попробуйте угадать число (длина {length}): ")
    
    bulls, cows = get_bulls_and_cows(guess, secret_number)
        
    print(f"Быки: {bulls}, Коровы: {cows}")
        
    if bulls == length:  
        print(f"Поздравляю! Вы угадали число {secret_number}")
        break


