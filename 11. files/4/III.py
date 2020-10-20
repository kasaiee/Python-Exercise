f = open('../words.txt')
words_ended_with_ing = [word for word in f.readlines() if word[-4:].lower() == 'ing\n']
open('words-ended-with-ing.txt', 'w').write(''.join(words_ended_with_ing))
