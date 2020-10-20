f = open('../words.txt')
lines = f.readlines()
res_lst = []
for word in lines:
    if word[-4:].lower() == 'ing\n':
        res_lst += [word]
result = open('words-ended-with-ing.txt', 'w')
result.write(''.join(res_lst))
