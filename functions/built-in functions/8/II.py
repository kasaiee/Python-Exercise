lst = ['ali', '12', '3.2', 'maryam', '10', 'reza']
res = [int(i) for i in lst if all([char in '0123456789' for char in i])]
print(res)
