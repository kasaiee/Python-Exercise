lines = open('words.txt').readlines()

max_lengh = 1
while True:
	res = [line for line in lines if len(line) == max_lengh]
	if res:
		break
	else:
		max_lengh += 1
print(res)



min_lengh = max([len(line) for line in lines])
while True:
	res = [line for line in lines if len(line) == min_lengh]
	if res:
		break
	else:
		max_lengh -= 1
print(res)
