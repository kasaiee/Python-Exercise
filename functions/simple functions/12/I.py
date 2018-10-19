def upper_count(text):
	counter = 0
	for char in text:
		if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			counter += 1
	return counter
