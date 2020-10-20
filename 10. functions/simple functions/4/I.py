def is_prime(num):
	for i in range(2, num//2+1):
		if num % i == 0:
			return False
	else:
		return True


def get_prims(num):
	res = []
	for i in range(2, num):
		if is_prime(i):
			res.append(i)
	return res

print(get_prims(20))
print(get_prims(30))
