from pprint import pprint


result = {}
for char in open('../words.txt').read():
    if char not in result:
        result[char] = 1
    else:
        result[char] += 1
pprint(result)
