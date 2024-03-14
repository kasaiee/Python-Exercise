base_leap_year = 2012
try:
    year = int(input('Year: '))
    assert year >= 0
    if (year - base_leap_year) % 4 == 0:
        print('yes')
    else:
        print('no')
except (ValueError, AssertionError):
    print('Invalid Input!')