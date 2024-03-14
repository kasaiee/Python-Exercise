num = 38

num_yekan = num_dahgan = num_sadgan = None

# تبدیل عدد ورودی به رشته
num_str = str(num)
if len(num_str) == 1:
    num_yekan = int(num_str[0])
elif len(num_str) == 2:
    num_yekan = int(num_str[0])
    num_dahgan = int(num_str[1])
elif len(num_str) == 3:
    num_yekan = int(num_str[0])
    num_dahgan = int(num_str[1])
    num_sadgan = int(num_str[2])


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