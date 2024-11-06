A = float(input("Введите A"))
N = int(input("Введите N"))
z = 0.0
for i in range (0,N + 1):
    z = z  + (A ** i)
print(z)