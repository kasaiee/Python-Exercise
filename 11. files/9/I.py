dotted_words = []
for word in open('../words.txt').read().replace('\n', ' ').split(' '):
    if 'i' in word or 'j' in word:
        dotted_words.append(word)
print(dotted_words)
