def largest_number(n):
	n.sort(reverse=True)
	num = ''
	for i in n:
		num += str(i)
	return num

num = input('Введите числа: ').split()
num = [int(i) for i in num]

print(largest_number(num))
