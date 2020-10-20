from math import sqrt
num = int(input('num: '))
for i in range(2, int(sqrt(num))+1):
	if num % i == 0:
		print('not prime!')
		break
else:
	print('prime!')