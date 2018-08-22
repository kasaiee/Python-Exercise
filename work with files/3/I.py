f = open('../words.txt')
lines = f.readlines()
res_str = ''
for word in lines:
    if word[:3].lower() == 'sub':
        res_str += word
result = open('words-started-with-sub.txt', 'w')
result.write(res_str)
