f = open('../words.txt')
lines = f.readlines()
res_lst = []
for word in lines:
    if word[:3].lower() == 'sub':
        res_lst += [word]
result = open('words-started-with-sub.txt', 'w')
result.write(''.join(res_lst))
