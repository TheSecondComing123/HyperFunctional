def __match_types(a, b, x, y):
	return isinstance(a, x) and isinstance(b, y) or isinstance(b, x) and isinstance(a, y)


def __str_int(a, b):
	if isinstance(a, str):
		if b >= 32:
			return a + chr(b)
		return a + a[b % len(a)]
	else:
		if a >= 32:
			return chr(a) + b
		return b[a % len(b)] + b


def plus(a, b):
	if isinstance(a, int | str) and isinstance(b, type(a)):
		return a + b
	
	if __match_types(a, b, str, int):
		return __str_int(a, b)
		
