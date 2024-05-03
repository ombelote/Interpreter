from constants import *
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndex = 1
        self.advance()

    def advance(self):
        self.tokenIndex += 1
        self.currentToken = self.tokens[self.tokenIndex] if self.tokenIndex < len(self.tokens) else None
        return self.currentToken

    def factor(self):
        token = self.currentToken
        if token.type in (TT_FLOAT, TT_INT):
            self.advance()
            return NumberNode(token)

    def term(self):
        return self.bin_op(self.factor(), (TT_MUL,TT_DIV))

    def expression(self):
        return self.bin_op(self.term(), (TT_PLUS,TT_MINUS))

    def bin_op(self, function, operands):
        left = self.factor()
        while self.currentToken in operands:
            operatorToken = self.currentToken
            right = function()
            left = BinOpNode(left, operatorToken, right)

        return left
    
    def parse(self):
        res = self.expression()
        return res