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


def divide(a, b):
	if __match_types(a, b, int, int):
		if a / b == (result := int(a / b)):
			return result
		return round(a / b, 2)
	if __match_types(a, b, str, int):
		if isinstance(b, str):
			a, b = b, a
		return [a[i:i + b] for i in range(0, len(a), b)]
	if __match_types(a, b, str, str):  # todo: work on lists too
		return a.split(b)
	
