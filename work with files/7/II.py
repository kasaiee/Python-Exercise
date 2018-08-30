r_content = open('../words.txt').readlines()[::-1]
open('r-words.txt', 'w').writelines(''.join(r_content))