f = open('words.txt')
new_f = open('5-letter-words.txt', 'w')
content = [line for line in f.readlines() if len(line) == 5]
new_f.write(''.join())
