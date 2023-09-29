numbers = input("Введите список чисел через запятую: ").split(",")
numbers = [int(num) for num in numbers]
numbers.sort(reverse=True, key=lambda x: str(x))
result = "".join(str(num) for num in numbers)
print("Максимально возможное число:", result)
#числа сортируются в обратном порядке с помощью функции sort и ключа lambda, который преобразует числа в строки для сравнения. отсортированные числа объединяются в одну строку с помощью функции join и выводится результат.
