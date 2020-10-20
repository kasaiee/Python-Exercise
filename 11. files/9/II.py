content = open('../words.txt').read().replace('\n', ' ').split(' ')
dotted_words = [word for word in content if 'i' in word or 'j' in word]
print(dotted_words)
