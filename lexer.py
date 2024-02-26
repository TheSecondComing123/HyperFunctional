import sly


class HFLexer(sly.Lexer):
	tokens = {NUMBER, PLUS, MINUS, TIMES, DIVIDE, EXPO, STRING, SEP}
	ignore = "\t"
	
	NUMBER = r"\d+"
	PLUS = r"\+"
	MINUS = r"-"
	TIMES = r"\*"
	EXPO = r"×"
	DIVIDE = r"/"
	
	SEP = r"[ _]"
	
	@_(r"\d+")
	def NUMBER(self, token):
		token.value = int(token.value)
		return token
	
	@_(r"\"[^\"]*\"")
	def STRING(self, token):
		token.value = token.value[1:-1]
		return token


lexer = HFLexer()
tokenize = lexer.tokenize
