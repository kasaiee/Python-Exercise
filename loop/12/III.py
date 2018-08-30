nums = int(input('How many numbers? '))
print(max([float(input('%sth number: ' % (index + 1))) for index, item in enumerate(range(nums))]))
