import sly


class HFLexer(sly.Lexer):
	tokens = {NUMBER, PLUS, MINUS, TIMES, DIVIDE, SEP}
	ignore = "\t\n"
	
	NUMBER = r"\d+"
	PLUS = r"\+"
	MINUS = r"-"
	TIMES = r"\*"
	DIVIDE = r"/"
	SEP = r"[ _]"
	
	@_(r'\d+')
	def NUMBER(self, token):
		token.value = int(token.value)
		return token


lexer = HFLexer()
tokenize = lexer.tokenize
