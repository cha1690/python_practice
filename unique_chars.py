def unique_chars(str1):
	chars = set()
	for let in str1:
		if let in chars:
			return False
		else:
			chars.add(let)