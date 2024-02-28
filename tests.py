import unittest

from lexer import tokenize
from parser import parse

from string import ascii_lowercase


def test(text):
	return parse(tokenize(text))


class HFTests(unittest.TestCase):
	def test_integers(self):
		self.assertEqual(test("0123"), 123)  # leading zeros are removed
		self.assertEqual(test("1 2+"), 3)
		self.assertEqual(test("2 2*"), 4)
		self.assertEqual(test("5 6-"), -1)
		self.assertEqual(test("5 2/"), 2.5)
		self.assertEqual(test("5 3/"), 1.67)  # division is rounded to 2 decimal places
		self.assertEqual(test("2 10×"), 1024)
	
	def test_strings(self):
		self.assertEqual(test("\"abc 1\n\""), "abc 1\n")
		self.assertEqual(test("\"abc\" \"abc\"+"), "abcabc")
		self.assertEqual(test("\"abc\" 02*"), "abcabc")
		self.assertEqual(test("\"abc\" 32+"), "abc ")
		self.assertEqual(test("02 \"abc\"+"), "cabc")
		self.assertEqual(test("\"abc\" 05+"), "abcc")
		self.assertEqual(test("\"abc\" \"ab\"-"), "c")
		self.assertEqual(test("\"abc\" 05-"), "ab")
		self.assertEqual(test("01 \"abc\"*"), "abc")
		self.assertEqual(test("2 \"12345\"/"), ["12", "34", "5"])
		self.assertEqual(test("\"123345\" \"33\"/"), ["12", "45"])
	
	def test_lists(self):
		self.assertEqual(test("[01,\"abc\",a]"), [1, "abc", ascii_lowercase])
		self.assertEqual(test("3 [1,2]+"), [3, 1, 2])
		self.assertEqual(test("[1,2,2,3] [2]-"), [1, 3])
		self.assertEqual(test("123 \"2\"-"), 13)
		self.assertEqual(test("[1,2,3] 2/"), [[1, 2], [3]])
	
	def test_constants(self):
		self.assertEqual(test("a"), ascii_lowercase)


if __name__ == '__main__':
	unittest.main()
