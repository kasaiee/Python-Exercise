f = open('../words.txt')
lines = f.readlines()
res = []
for line in lines:
    if len(line) == 5:
        res += [line]
new_f = open('../5-letter-words.txt', 'w')
new_f.write(''.join(res))
