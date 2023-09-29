from random import randint

secret_number = randint(0, 100)
guess = None

while guess != secret_number:
    guess = int(input("Введите число: "))

    if guess < secret_number:
        print("Загаданное число больше!")
    elif guess > secret_number:
        print("Загаданное число меньше!")

print("Вы угадали число!")
