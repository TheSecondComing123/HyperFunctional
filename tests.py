import unittest

from lexer import tokenize
from parser import parse


# def test(text):
# 	return parse(tokenize(test))


class MyTestCase(unittest.TestCase):
	def test_integers(self):
		self.assertEqual(parse(tokenize("1 2+")), 3)
		self.assertEqual(parse(tokenize("2 2*")), 4)
		self.assertEqual(parse(tokenize("5 6-")), -1)
		self.assertEqual(parse(tokenize("5 2/")), 2.5)
		self.assertEqual(parse(tokenize("5 3/")), 1.67)  # division is rounded to 2 decimal places
		self.assertEqual(parse(tokenize("2 10×")), 1024)


if __name__ == '__main__':
	unittest.main()
