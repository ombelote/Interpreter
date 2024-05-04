from lexer import Lexer
from parser_class import Parser

def run(fileName, text):
    lexer = Lexer(fileName, text)
    tokens, err = lexer.make_tokens()
    if err : return None, err
    parser = Parser(tokens)
    ast = parser.parse()
    return ast, None

while True:
    text = input('basic > ')
    fileName = 'basic'
    tokens, error = run( fileName, text)

    if error:
        print(error.as_string())
    else:
        print('Result:\n', tokens)
