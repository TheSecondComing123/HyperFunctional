import sly

from lexer import HFLexer
from element_helpers import *

from string import ascii_lowercase


class HFParser(sly.Parser):
	tokens = HFLexer.tokens
	
	@_("expr SEP expr PLUS")
	def expr(self, p):
		return plus(p[0], p[2])
	
	@_("expr SEP expr MINUS")
	def expr(self, p):
		return minus(p[0], p[2])
	
	# todo: implement -int, -str, -list
	
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
	
	@_("LIST")
	def expr(self, p):
		return p.LIST
	
	@_("LIST_BEGIN list_items LIST_END")
	def LIST(self, p):
		return p.list_items
	
	@_("list_items LIST_SEP item")
	def list_items(self, p):
		p.list_items.append(p.item)
		return p.list_items
	
	@_("item")
	def list_items(self, p):
		return [p.item]
	
	@_("expr")
	def item(self, p):
		return p[0]
	
	@_("LOWERCASE_ALPHABET")
	def expr(self, p):
		return ascii_lowercase


parser = HFParser()
parse = parser.parse
