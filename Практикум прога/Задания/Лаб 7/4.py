def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result



   
x = int(input("Введите х"))

num = power(x, 6) * power(x - 5, 3)  
num1 = power(2 * x + 1, 5)         
y = num / num1
print(f"Значение y при x = {x}: {y}")
