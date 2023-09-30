elements = []
while True:
    user_input = input("Введите элемент: ")
    if user_input == "":
        break
    elements.append(user_input)
print("Итоговый список:", elements)
