def r_mul2(a, b):
	return a if b == 1 else a + r_mul2(a, b-1)
