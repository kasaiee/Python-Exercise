def filter_odd(*args):
	assert all([type(i) == int for i in args]), 'Only integers!'
	return [num for num in args if num % 2]

print(filter_odd(1, 2, 3, 4))
