max_line = ''
for line in open('../words.txt').readlines():
    if len(line) > len(max_line):
        max_line = line
print(max_line)
