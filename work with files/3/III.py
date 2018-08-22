f = open('../words.txt')
words_started_with_sub = [word for word in f.readlines() if word[:3].lower() == 'sub']
open('words-started-with-sub.txt', 'w').write(''.join(words_started_with_sub))
