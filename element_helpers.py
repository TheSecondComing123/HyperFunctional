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
		else:  # a is the int
			if a >= 32:
				return chr(a) + b
			return b[a % len(b)] + b
	elif isinstance(a, list):
		if isinstance(b, list):
			return a + b
		return a + [b]
	elif isinstance(b, list):
		if isinstance(a, list):
			return a + b
		return [a] + b
		

def minus(a, b):
	if __match_types(a, b, int, int):
		return a - b
	elif __match_types(a, b, str, str):
		return a.replace(b, "")
	elif __match_types(a, b, list, list):
		return [i for i in a if i not in b]
	elif isinstance(a, str | list) and isinstance(b, int):
		if isinstance(b, str | list):
			a, b = b, a
			
		point = b % len(a)
		return a[:point] + a[point + 1:]
	elif isinstance(a, int) and isinstance(b, str | list):
		return int("".join(i for i in str(a) if i not in b))


def divide(a, b):
	if __match_types(a, b, int, int):
		if a / b == (result := int(a / b)):
			return result
		return round(a / b, 2)
	elif __match_types(a, b, str | list, int | str):
		if __match_types(a, b, str, str):
			return a.split(b)
		
		if isinstance(a, str):
			b = str(b) if isinstance(b, int) else "".join(b)
		
		current = []
		for i in range(len(a)):
			if a[i] == b:
				current.append(a[:i])
				
				try:
					end = a.index(b, i + 1)
				except ValueError:
					end = len(a)
				current.append(a[i + 1:end])
		
		return current
	elif __match_types(a, b, list, list):
		return [a[i] for i in range(len(a)) if a[i:i+len(b)] != b]
