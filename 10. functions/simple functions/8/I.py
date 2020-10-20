def is_pangram(text):
	d = {}
	for char in text:
		if char in d.keys():
			d[char] += 1
		else:
			d[char] = 1
	return len(d.values()) == sum(d.values())
