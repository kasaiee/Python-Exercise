try:
    year = int(input('Year: '))
    dividers = [1, 5, 9, 13, 17, 26, 30]

    assert 0 <= year <= 1472
    if year in range(1244, 1343):
        print('yes' if year % 33 in dividers + [21] else 'no')
    elif year in range(1343, 1473):
        print('yes' if year % 33 in dividers + [22] else 'no')
    else:
        print('no')
except ValueError:
    print('Invalid Input!')
except AssertionError:
    print('Out of range!')