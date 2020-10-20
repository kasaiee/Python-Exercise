def list_sum(lst):
	total = 0
	for i in lst:
		if type(i) == int:
			total += i
		elif type(i) == list:
			total += list_sum(i)
	return total

print(list_sum([1, 1, 1, [2, 2, [1], [3]]]))
