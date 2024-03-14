year = int(input('Year: '))

if 1244 <= year <= 1342:
    if year % 33 in [1, 5, 9, 13, 17, 21, 26, 30]:
        print('yes')
    else:
        print('no')
elif 1343 <= year <= 1472:
    if year % 33 in [1, 5, 9, 13, 17, 22, 26, 30]:
        print('yes')
    else:
        print('no')
else:
    print('no')