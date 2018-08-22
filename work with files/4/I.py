f = open('../words.txt')
lines = f.readlines()
res_str = ''
for word in lines:
    if word[-4:].lower() == 'ing\n':
        res_str += word
result = open('words-ended-with-ing.txt', 'w')
result.write(res_str)
