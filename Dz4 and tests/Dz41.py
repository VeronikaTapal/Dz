def rotate_list(elements, k):
    for j in range(k):
        element = elements.pop()
        elements.insert(0, element)
    return elements

elements = input("Введите элементы списка через пробел: ").split()
k = int(input("Введите число k: "))
result = rotate_list(elements, k)
print(result)
