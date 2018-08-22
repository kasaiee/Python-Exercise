lines = open('../words.txt').readlines()
min_len = 1
while True:
    shortest_words = [word for word in lines if len(word) == min_len]
    if shortest_words:
        result = open('shortest-words.txt', 'w')
        result.write(''.join(shortest_words))
        break
    else:
        min_len += 1
