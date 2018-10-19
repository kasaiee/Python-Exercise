def get_divs2(num):
	return [i for i in range(1, num//2+1) if num % i == 0]

def is_perfect2(num):
	return num == sum(get_divs2(num))
