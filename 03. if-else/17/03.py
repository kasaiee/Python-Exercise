numbers = [102, 110, 100, 120, 20, 8, 18]

for num in numbers:
    num_yekan = num_dahgan = num_sadgan = None

    # تبدیل عدد ورودی به رشته
    num_str = str(num)
    if len(num_str) == 1:
        num_yekan = num
    elif len(num_str) == 2:
        num_yekan = int(num_str[1])
        num_dahgan = int(num_str[0])
    elif len(num_str) == 3:
        num_yekan = int(num_str[2])
        num_dahgan = int(num_str[1])
        num_sadgan = int(num_str[0])

    sadgan_00 = {
        0: '',
        1: 'sad',
        2: 'devist',
        3: 'sisad',
        4: 'chaharsad',
        5: 'pansad',
        6: 'sheshsad',
        7: 'haftsad',
        8: 'hashtsad',
        9: 'nohsad',
    }

    sadgan = {
        None: '',
        0: '',
        1: 'sad va ',
        2: 'devist va ',
        3: 'sisad va ',
        4: 'chaharsad va ',
        5: 'pansad va ',
        6: 'sheshsad va ',
        7: 'haftsad va ',
        8: 'hashtsad va ',
        9: 'nohsad va ',
    }

    dahgan_0 = {
        0: '',
        2: 'bist',
        3: 'si',
        4: 'chehel',
        5: 'panjah',
        6: 'shast',
        7: 'haftad',
        8: 'hashtad',
        9: 'navad',
    }

    dahgan = {
        None: '',
        0: '',
        2: 'bist va ',
        3: 'si va ',
        4: 'chehel va ',
        5: 'panjah va ',
        6: 'shast va ',
        7: 'haftad va ',
        8: 'hashtad va ',
        9: 'navad va ',
    }

    yekan = {
        0: '',
        1: 'yek',
        2: 'do',
        3: 'se',
        4: 'chahar',
        5: 'panj',
        6: 'shesh',
        7: 'haft',
        8: 'hasht',
        9: 'noh',
    }

    dahgan_yek = {
        0: 'dah',
        1: 'yazdah',
        2: 'davazdah',
        3: 'sizdah',
        4: 'chahardah',
        5: 'panzdah',
        6: 'shanzdah',
        7: 'hefdah',
        8: 'hejdah',
        9: 'noozdah',
    }

    # چیزی که قراره عددمون رو به رشته درونش ذخیره کنم
    res = ''
    print(num)
    if num_dahgan == 0 and num_yekan == 0:
        print(sadgan_00[num_sadgan])
    elif num_dahgan == 1:
        print(sadgan[num_sadgan] + dahgan_yek[num_yekan])
    else:
        if num_yekan == 0:
            print(sadgan[num_sadgan] + dahgan_0[num_dahgan])
        else:
            print(sadgan[num_sadgan] + dahgan[num_dahgan] + yekan[num_yekan])