import unittest

from lexer import tokenize
from parser import parse


# def test(text):
# 	return parse(tokenize(test))


class HFTests(unittest.TestCase):
	def test_integers(self):
		self.assertEqual(parse(tokenize("0123")), 123)  # leading zeros are removed
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
		self.assertEqual(parse(tokenize("\"abc\" 32+")), "abc ")
		self.assertEqual(parse(tokenize("02 \"abc\"+")), "cabc")
		self.assertEqual(parse(tokenize("\"abc\" 05+")), "abcc")
		self.assertEqual(parse(tokenize("\"abc\" \"ab\"-")), "c")
		self.assertEqual(parse(tokenize("05 \"abc\"-")), "ab")
		self.assertEqual(parse(tokenize("01 \"abc\"*")), "abc")
		self.assertEqual(parse(tokenize("2 \"12345\"/")), ["12", "34", "5"])


if __name__ == '__main__':
	unittest.main()
