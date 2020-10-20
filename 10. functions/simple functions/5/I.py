def get_divs(num):
	res = []
	for i in range(1, num//2+1):
		if num % i == 0:
			res += [i]
	return res

def is_perfect(num):
	total = 0
	for i in get_divs(num):
		total += i
	if num == total:
		return True
	else:
		return False
