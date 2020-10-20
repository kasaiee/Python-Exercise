num = int(input('num: '))
for i in range(2, int(num ** 0.5)):
    if num % i == 0:
        print('not prime!')
        break
else:
    print('prime!')
