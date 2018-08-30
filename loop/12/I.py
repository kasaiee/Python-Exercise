nums = int(input('How many numbers? '))
all_num = []
for index, item in enumerate(range(nums)):
    msg = '%sth number: ' % (index + 1)
    all_num.append(float(input(msg)))
print(max(all_num))
