number = int(input("Введите пятизначное число: "))
while number > 0:
    f = number % 10
    number = number // 10
    print(f)


