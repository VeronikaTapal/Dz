sequence =  input("Введите последовательность чисел, разделенных пробелом: ").split()
item = input("Введите номер для поиска: ")

def binary_search(sequence, item):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        d = (low + high) // 2
        g = sequence[d]
        if g == item:
            while d>0 and sequence[d-1] == item:
                d -= 1
            return d
        elif g > item:
            high = d - 1
        else:
            low = d + 1
    return None

print(binary_search(sequence, item))


