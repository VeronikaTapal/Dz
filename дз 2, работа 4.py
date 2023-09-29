def check_brackets(s):
    opening = '('
    closing = ')'

    count_opening = 0  # количество открывающих скобок
    count_closing = 0  # количество закрывающих скобок

    for i in s:
        if i == opening:
            count_opening += 1  # увеличиваем счётчик открывающих скобок
        elif i == closing:
            count_closing += 1  # увеличиваем счётчик закрывающих скобок

    result = "Все скобки соответствуют!" if count_opening == count_closing else f"{count_closing - count_opening} {closing} не хватает!"

    return result


s = input("Введите строку: ")
print(check_brackets(s))