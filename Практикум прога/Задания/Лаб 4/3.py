#Дано целое число N (N > 0). Используя операции деления нацело и взятия 
#остатка от деления, найти количество и сумму его цифр. 

N = int(input("Введите число н"))
k = 0
sum = 0
while (N):
    sum = sum + N % 10
    N = N // 10
    k += 1
    
print(k)   
print(sum)  