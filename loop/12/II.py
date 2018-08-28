nums = int(input('How many numbers? '))
all_num = []
counter = 1
while counter <= nums:
    msg = '%sth number: ' % (counter + 1)
    all_num.append(float(input(msg)))
    counter += 1
print(max(all_num))
