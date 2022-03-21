class Token:
    def __init__(self, type,lexeme, line,column):
        self.type=type
        self.lexeme=lexeme
        self.line=line
        self.column=column

    def printToken(self):
        print("\n 1. Tipo:{}\n 2. Lexema:{}\n 3. Línea:{}\n 4. Columna:{}".format(self.type,
        self.lexeme,self.line,self.column))
    
    def getType(self):
        return self.type

    def getLexeme(self):
        return self.lexeme
    
    def getLine(self):
        return self.line
    
    def getColumn(self):
        return self.column

class Error:
    def __init__(self, type,errorDescription, line,column):
        self.type=type
        self.errorDescription=errorDescription
        self.line=line
        self.column=column
    
    def getType(self):
        return self.type

    def getErrorDescription(self):
        return self.errorDescription
    
    def getLine(self):
        return self.line
    
    def getColumn(self):
        return self.column

    def printError(self):
        print("\n 1. Tipo:{}\n 2. Descripción:{}\n 3. Línea:{}\n 4. Columna:{}".format(self.type,
        self.errorDescription,self.line,self.column))

class semanticError:

    def __init__(self, description):
        self.description=description

    def getError(self):
        return self.description
