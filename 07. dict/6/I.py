d1 = {'fname': 'ali', 'lname': 'moradi', 'age': 30, 'city': 'tehran', 'phone': '09377000000', 'country': 'iran', 1:11, 2:22, 3:33, 4:44, 5:55}
d2 = {'fname': 'ali', 'lname': 'moradi', 'age': 20, 'city': 'Shahrerey', 'phone': '09377000001', 'country': 'iran'}
res = {}
for k1, v1 in d1.items():
	for k2, v2 in d2.items():
		if k1 == k2 and v1 == v2:
			res[k1] = v1

print(res)
