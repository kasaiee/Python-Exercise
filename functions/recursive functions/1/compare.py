from datetime import datetime


def r_mul1(a, b):
	if b == 1:
		return a
	return a + r_mul1(a, b-1)

def r_mul2(a, b):
	return a if b == 1 else a + r_mul2(a, b-1)

def mul(a, b):
	res = 0
	for i in range(b):
		res += 1
	return res



start = datetime.now()
print(r_mul1(1, 998))
print(datetime.now() - start)

start = datetime.now()
print(r_mul2(1, 998))
print(datetime.now() - start)

start = datetime.now()
print(mul(1, 998))
print(datetime.now() - start)
