def get_max(*args):
	return max(args)

var_count = int(input('variables count: '))
choices = []
for i in range(var_count):
	choices += [int(input('num %s:' % (i+1)))]

print(get_max(*choices))
