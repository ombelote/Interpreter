from lexer import Lexer

def run(fileName, text):
    lexer = Lexer(fileName, text)
    tokens, err = lexer.make_tokens()
    return tokens, err

while True:
    text = input('basic > ')
    fileName = 'basic'
    tokens, error = run( fileName, text)

    if error:
        print(error.as_string())
    else:
        print('Result:\n', tokens)
