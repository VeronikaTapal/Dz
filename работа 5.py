x = float(input("Введите число X: "))
y = float(input("Введите число Y: "))

if x > 0 and y > 0:
    print("Точка находится в первой четверти")
elif x < 0 and y > 0:
    print("Точка находится во второй четверти")
elif x < 0 and y < 0:
    print("Точка находится в третьей четверти")
elif x > 0 and y < 0:
    print("Точка находится в четвертой четверти")
elif x == 0 and y != 0:
    print("Точка лежит на оси Y")
elif x != 0 and y == 0:
    print("Точка лежит на оси X")
else:
    print("Точка лежит в начале координат")


