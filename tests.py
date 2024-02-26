import unittest

from lexer import tokenize
from parser import parse


# def test(text):
# 	return parse(tokenize(test))


class MyTestCase(unittest.TestCase):
	def test_integers(self):
		self.assertEqual(parse(tokenize("0123")), 123)
		self.assertEqual(parse(tokenize("1 2+")), 3)
		self.assertEqual(parse(tokenize("2 2*")), 4)
		self.assertEqual(parse(tokenize("5 6-")), -1)
		self.assertEqual(parse(tokenize("5 2/")), 2.5)
		self.assertEqual(parse(tokenize("5 3/")), 1.67)  # division is rounded to 2 decimal places
		self.assertEqual(parse(tokenize("2 10×")), 1024)
	
	def test_strings(self):
		self.assertEqual(parse(tokenize("\"abc 1\n\"")), "abc 1\n")
		self.assertEqual(parse(tokenize("\"abc\" \"abc\"+")), "abcabc")
		self.assertEqual(parse(tokenize("\"abc\" 02*")), "abcabc")


if __name__ == '__main__':
	unittest.main()
