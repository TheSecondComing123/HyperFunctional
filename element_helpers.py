def __match_types(a, b, x, y):
	return isinstance(a, x) and isinstance(b, y) or isinstance(b, x) and isinstance(a, y)


def __str_int(a, b):
	if isinstance(a, str):
		if b >= 32:
			return a + chr(b)
		if b <= len(a) - 1:
			return a + a[b]
		return a + str(b)
	else:
		if a >= 32:
			return chr(a) + b
		if a <= len(b) - 1:
			return b[a] + b
		return str(a) + b


def plus(a, b):
	if isinstance(a, int | str) and isinstance(b, type(a)):
		return a + b
	
	if __match_types(a, b, str, int):
		return __str_int(a, b)
		
