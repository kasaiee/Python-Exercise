year = int(input('Year: '))
if 1244 <= year and year <= 1472:
    if year % 33 == 1 or \
    year % 33 == 5 or \
    year % 33 == 9 or \
    year % 33 == 13 or \
    year % 33 == 17 or \
    year % 33 == 21 and year <= 1342 or \
    year % 33 == 22 and 1343 <= year or \
    year % 33 == 26 or \
    year % 33 == 30:
        print('yes')
    else:
        print('no')
else:
    print('no')