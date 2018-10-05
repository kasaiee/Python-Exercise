d1 = {'fname': 'ali', 'lname': 'moradi', 'age': 30, 'city': 'tehran', 'phone': '09377000000', 'country': 'iran', 1:11, 2:22, 3:33, 4:44, 5:55}
d2 = {'fname': 'ali', 'lname': 'moradi', 'age': 20, 'city': 'Shahrerey', 'phone': '09377000001', 'country': 'iran'}
res = {k: v for k, v in d2.items() if k in d1.keys() and d1[k] == d2[k]}
print(res)
