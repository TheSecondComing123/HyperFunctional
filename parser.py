import sly

from lexer import HFLexer
from element_helpers import *


class HFParser(sly.Parser):
	tokens = HFLexer.tokens
	
	@_("expr SEP expr PLUS")
	def expr(self, p):
		return plus(p[0], p[2])
	
	@_("expr SEP expr MINUS")
	def expr(self, p):
		return minus(p[0], p[2])
	
	@_("expr SEP expr TIMES")
	def expr(self, p):
		return p[0] * p[2]
	
	@_("expr SEP expr EXPO")
	def expr(self, p):
		return p[0] ** p[2]
	
	@_("expr SEP expr DIVIDE")
	def expr(self, p):
		return divide(p[0], p[2])
	
	@_("NUMBER")
	def expr(self, p):
		return p[0]
	
	@_("STRING")
	def expr(self, p):
		return p.STRING


parser = HFParser()
parse = parser.parse
