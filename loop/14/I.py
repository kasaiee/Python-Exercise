num = int(input('num: '))
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print('not prime!')
        break
else:
    print('prime!')
