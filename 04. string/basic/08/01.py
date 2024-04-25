name = input('Name: ')
subname = name[0:4]
if subname.lower() in 'amir':
    print('Hi', name)
elif subname in 'امیر':
    print('Hi', name)
elif subname in 'امير':
    print('Hi', name)