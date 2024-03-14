numbers = [102, 110, 100, 120, 20, 8, 18]

for num in numbers:
    num_yekan = num_dahgan = num_sadgan = None

    # اگر عدد یک رقمی باشد
    if 0 <= num <= 9:
        # استخراج یکان
        num_yekan = num
    # اگر عدد دو رقمی باشد
    elif 10 <= num <= 99:
        # استخراج یکان
        num_yekan = num % 10
        # استخراج دهگان
        num_dahgan = num // 10 % 10
    # اگر عدد سه رقمی باشد
    elif 100 <= num <= 999:
        # استخراج یکان
        num_yekan = num % 10
        # استخراج دهگان
        num_dahgan = num // 10 % 10
        # استخراج صدگان
        num_sadgan = num // 100

    # چیزی که قراره عددمون رو به رشته درونش ذخیره کنم
    res = ''

    if num_sadgan == 1:
        res += 'sad va '
    elif num_sadgan == 2:
        res += 'devist va '
    elif num_sadgan == 3:
        res += 'sisad va '
    elif num_sadgan == 4:
        res += 'chaharsad va '
    elif num_sadgan == 5:
        res += 'pansad va '
    elif num_sadgan == 6:
        res += 'sheshsad va '
    elif num_sadgan == 7:
        res += 'haftsad va '
    elif num_sadgan == 8:
        res += 'hashtsad va '
    elif num_sadgan == 9:
        res += 'nohsad va '

    if num_dahgan == 1:
        if num_yekan == 1:
            res += 'yazdah'
        elif num_yekan == 2:
            res += 'davazdah'
        elif num_yekan == 3:
            res += 'sizdah'
        elif num_yekan == 4:
            res += 'chahardah'
        elif num_yekan == 5:
            res += 'panzdah'
        elif num_yekan == 6:
            res += 'shanzdah'
        elif num_yekan == 7:
            res += 'hefdah'
        elif num_yekan == 8:
            res += 'hejdah'
        elif num_yekan == 9:
            res += 'noozdah'
    elif num_dahgan == 2:
        res += 'bist va '
    elif num_dahgan == 3:
        res += 'si va '
    elif num_dahgan == 4:
        res += 'chehel va '
    elif num_dahgan == 5:
        res += 'panjah va '
    elif num_dahgan == 6:
        res += 'shast va '
    elif num_dahgan == 7:
        res += 'haftad va '
    elif num_dahgan == 8:
        res += 'hashtad va '
    elif num_dahgan == 9:
        res += 'navad va '

    if num_dahgan != 1:
        if num_yekan == 1:
            res += 'yek'
        elif num_yekan == 2:
            res += 'do'
        elif num_yekan == 3:
            res += 'se'
        elif num_yekan == 4:
            res += 'chahar'
        elif num_yekan == 5:
            res += 'panj'
        elif num_yekan == 6:
            res += 'shesh'
        elif num_yekan == 7:
            res += 'haft'
        elif num_yekan == 8:
            res += 'hasht'
        elif num_yekan == 9:
            res += 'noh'

    print(res)