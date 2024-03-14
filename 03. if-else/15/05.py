year = int(input('Year: '))

dividers = [1, 5, 9, 13, 17, 26, 30]

if 1244 <= year <= 1342:
    if year % 33 in dividers + [21]:
        print('yes')
    else:
        print('no')
elif 1343 <= year <= 1472:
    if year % 33 in dividers + [22]:
        print('yes')
    else:
        print('no')
else:
    print('no')