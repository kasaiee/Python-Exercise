while True:
    try:
        c = float(input('celsius degree: '))
        if c < -273.15:
            print('celsius degree must be greather than', 273.15)
        else:
            print(c / 5 * 9 + 32)
            break
    except ValueError:
        print('Incorrect input!')