def is_prime(num):
	for i in range(2, num//2+1):
		if num % i == 0:
			return False
	else:
		return True


print(is_prime(15))
