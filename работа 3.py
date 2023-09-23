import math

x = float(input("Введите число X: "))
y = float(input("Введите число Y: "))
z = float(input("Введите число Z: "))

length = math.sqrt(x**2 + y**2 + z**2)
print("Длина вектора:", length)
