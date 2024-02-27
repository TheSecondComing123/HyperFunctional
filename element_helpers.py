def __match_types(a, b, x, y):
	return isinstance(a, x) and isinstance(b, y) or isinstance(b, x) and isinstance(a, y)


def plus(a, b):
	if isinstance(a, type(b)):
		return a + b
	
	if __match_types(a, b, str, int):
		if isinstance(a, str):
			if b >= 32:
				return a + chr(b)
			return a + a[b % len(a)]
		else:
			if a >= 32:
				return chr(a) + b
			return b[a % len(b)] + b
		

def minus(a, b):
	try:
		return a - b
	except TypeError:
		if __match_types(a, b, str, str):
			return a.replace(b, "")
		elif __match_types(a, b, str | list, int):
			if isinstance(b, str | list):
				a, b = b, a
				
			point = b % len(a)
			return a[:point] + a[point + 1:]
