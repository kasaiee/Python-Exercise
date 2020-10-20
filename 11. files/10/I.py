content = open('../words.txt').read().replace('\n', ' ').split()
res = [line for line in content if line == line[::-1]]
print(res)
