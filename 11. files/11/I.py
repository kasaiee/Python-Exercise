words = open('../words.txt').read().replace('\n', ' ').split()
pangram_words = [word for word in words if len(word) == len(set(word))]
print(pangram_words)
