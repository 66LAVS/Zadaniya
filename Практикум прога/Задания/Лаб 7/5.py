def dvoi(n):
    
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def vosm(n):
   
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal


   
number = int(input("Введите десятичное число: "))
binary = dvoi(number)
vosmi = vosm(number)
    
print(f"Двоичное представление числа {number}: {binary}")
print(f"Восьмеричное представление числа {number}: {vosmi}")
