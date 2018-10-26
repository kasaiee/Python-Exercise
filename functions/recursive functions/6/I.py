# without error handling
def r_sum_num(num):
	if num < 10:
		return num
	return num % 10 + r_sum_num(num//10)

# with error handling
def r_sum_num(num):
	assert type(num) == int, 'Must be integer!'
	if num < 0:
		num *= -1
	if num < 10:
		return num
	return num % 10 + r_sum_num(num//10)
