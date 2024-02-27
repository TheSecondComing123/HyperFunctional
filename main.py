from lexer import *
from parser import *


if __name__ == "__main__":
	while True:
		data = input(">>> ")
		if not data or data.isspace():
			break
		
		print(parse(tokenize(data)))
