def r_mul1(a, b):
	if b == 1:
		return a
	return a + r_mul1(a, b-1)
