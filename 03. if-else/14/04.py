# years = [2012, 2016, 2020, 2024, 2028, 2032]
base_leap_year = 2012
try:
    year = int(input('Year: '))
    if year < 0:
        raise ValueError
    if (year - base_leap_year) % 4 == 0:
        print('yes')
    else:
        print('no')
except ValueError:
    print('Invalid Input!')