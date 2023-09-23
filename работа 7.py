x = int(input("Введите число X: "))
y = int(input("Введите число Y: "))

sum = 0

for i in range(x, y+1):
    if i % 5 == 0:
        sum += i

print("Сумма чисел кратных 5-ти:", sum)



