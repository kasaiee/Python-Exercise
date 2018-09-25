choice = mymax = float('-inf')
while True:
    choice = input('number: ')
    if choice.lower() == 'exit':
        break
    try:
        choice = int(choice)
        if choice > mymax:
            mymax = choice
    except:
        pass
