name = input('Name: ')
subname = name[0:4]
if subname.lower() in 'amir' or subname in 'امیر' or subname in 'امير':
    print('Hi', name)