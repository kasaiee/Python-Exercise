lst = ['ali', '12', '3.2', 'maryam', '10', 'reza']
res = []
for i in lst:
    if all([char in '0123456789' for char in i]):
        res.append(int(i))

print(res)
