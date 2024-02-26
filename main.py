from lexer import *
from parser import *


if __name__ == "__main__":
	print(parse(tokenize("'abc'_'abc'+")))  # not working
