new_content = open('../words.txt').read().replace('\n', ' ')
open('words-in-one-line.txt', 'w').write(new_content)
