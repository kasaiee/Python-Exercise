choice = mymax = float('-inf')
while True:
    choice = input('number: ')
    if choice.lower() == 'exit':
        break
    elif choice[0] == '-' and all([number in '0123456789' for number in choice[1:]]):
        choice = int(choice)
        if choice > mymax:
            mymax = choice
    elif all([number in '0123456789' for number in choice]):
        choice = int(choice)
        if choice > mymax:
            mymax = choice
