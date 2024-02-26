from lexer import *
from parser import *


if __name__ == "__main__":
	print(parse(tokenize("10 5- 6+ 2×")))
