user_input = input("Введите строку: ")
k = int(input("Введите число k: "))

digits = [char for char in user_input if char.isdigit()]

if k > len(digits):
    print("В строке нет", k, "цифры")
else:
    print(k, "-ая цифра в строке", digits[k-1])
