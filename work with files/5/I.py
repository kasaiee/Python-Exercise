f = open('../words.txt')
counter = 0
while f.readline():
    counter += 1
print(counter)
