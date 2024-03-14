try:
    char = input('Char: ')
    assert len(char) == 1 and char.isalpha()
    if char.lower() in 'aioue':
        print('yes')
    else:
        print('no')
except AssertionError:
    print('Invalid Input!')