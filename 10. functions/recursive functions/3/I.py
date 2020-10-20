def r_fact(num):
	assert num >= 0, 'Must not be negative!'
	if num == 1 or num == 0:
		return 1
	else:
		return num * r_fact(num - 1)

print(r_fact(4))
print(r_fact(-4))
