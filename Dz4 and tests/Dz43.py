def is_unique(x):
    if isinstance(x, str):
        x = list(x.replace(" ", ""))
        unique_elements = set(x)
        if len(unique_elements) == len(x):
            return True
        else:
            return False
x = input('Введите последовательность: ')
print(is_unique(x))