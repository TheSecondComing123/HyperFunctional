import sly
from lexer import HFLexer


class HFParser(sly.Parser):
	tokens = HFLexer.tokens
	
	@_('expr SEP expr PLUS')
	def expr(self, p):
		return p[0] + p[2]
	
	@_('expr SEP expr MINUS')
	def expr(self, p):
		return p[0] - p[2]
	
	@_('expr SEP expr TIMES')
	def expr(self, p):
		return p[0] * p[2]
	
	@_('expr SEP expr DIVIDE')
	def expr(self, p):
		val = p[0] / p[2]
		if val == int(val):
			return int(val)
		return round(val, 2)
	
	@_('NUMBER')
	def expr(self, p):
		return p[0]


parser = HFParser()
parse = parser.parse
