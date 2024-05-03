class Position:
    def __init__(self, idx, ln, col, fileName, fileText):
        self.idx = idx # index of the position in current line
        self.ln = ln # line number in file.
        self.col = col # column number in file.
        self.fileName = fileName # name of the file that contains this position.
        self.fileText = fileText  # text of the file that contains this position.

    def advance(self, current_char):
        self.idx += 1
        self.col += 1 if current_char != '\n' else 0

        return self
    
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fileName, self.fileText)
