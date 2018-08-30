content = open('../words-with-numbers.txt').read()
total = 0
for char in content:
    if char in '1234567890':
        total += int(char)
print(total)
