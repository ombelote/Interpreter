class NumberNode:
    def __init__(self, token):
        self.token = token
    
    def __repr__(self):
        return f'{self.token}'
    
class BinOpNode:
    def __init__(self, leftNode, operatorToken, rightNode):
        self.left = leftNode
        self.operatorToken = operatorToken
        self.right = rightNode

    def __repr__(self):
        return f'{self.left}, {self.operatorToken}, {self.right}'