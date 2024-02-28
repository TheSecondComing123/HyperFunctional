import sly


class HFLexer(sly.Lexer):
	tokens = {NUMBER,
	          PLUS, MINUS, TIMES, DIVIDE, EXPO,
	          STRING,
	          LIST_BEGIN, LIST_END, LIST_SEP,
	          LOWERCASE_ALPHABET, SEP}
	ignore = "\t"
	
	NUMBER = r"\d+"
	PLUS = r"\+"
	MINUS = r"-"
	TIMES = r"\*"
	EXPO = r"×"
	DIVIDE = r"/"
	
	LIST_BEGIN = r"\["
	LIST_END = r"\]"
	LIST_SEP = r","
	
	SEP = r"[ _]"
	
	# (ACTUAL) CONSTANTS
	LOWERCASE_ALPHABET = r"a"
	
	@_(r"\d+")
	def NUMBER(self, token):
		token.value = int(token.value)
		return token
	
	@_(r"\"[^\"]*\"")
	def STRING(self, token):
		token.value = token.value[1:-1]
		return token
	
	@_(r'\[.*?\]')
	def LIST(self, token):
		token.value = token.value[1:-1].split(',')
		return token


lexer = HFLexer()
tokenize = lexer.tokenize
