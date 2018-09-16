from datetime import datetime


def r_fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	return r_fib(n-1) + r_fib(n-2)


def fib(n):
	a, b = 0, 1
	for i in range(n-1):
		a, b = b, a+b
	return a


start = datetime.now()
print(r_fib(33))
print('    recursive: ', datetime.now()-start)

start = datetime.now()
print(fib(33))
print('non recursive: ', datetime.now()-start)
