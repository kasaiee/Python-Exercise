name = input('Name: ')
subname = name[0:4]
cond1 = subname.lower() in 'amir'
cond2 = subname in 'امیر'
cond3 = subname in 'امير'
if cond1 or cond2 or cond3:
    print('Hi', name)