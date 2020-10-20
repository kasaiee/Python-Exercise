def filter_odd(*args):
	return [num for num in args if num % 2]

print(filter_odd(1, 2, 3, 4))
