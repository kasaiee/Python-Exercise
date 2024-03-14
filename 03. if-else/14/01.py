# years = [2012, 2016, 2020, 2024, 2028, 2032]
years = [2012, 2016, 2020, 2024, 2028, 2032]
year = 2012

if year % 4 == 0:
    if year % 100 == 0:
        print('no')    
    elif year % 400 == 0:
        print('yes')
    print('yes')
else:
    print('no')