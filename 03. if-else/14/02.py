years = [2012, 2016, 2020, 2024, 2028, 2032]
year = 2012

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('yes')
else:
    print('no')