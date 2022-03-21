class semantic:
    def __init__(self) -> None:
        pass

    def semanticalAnalyzer(self,tokenList, semanticErrorList):
        var=0
        for counter in range(5,len(tokenList)):
            token=tokenList[counter].getLexeme()
            if token=="<":
                for i in range(counter,len(tokenList)):
                    token2=tokenList[i].getLexeme()
                    if token2==">":
                        var=i
                        break
            else:
                print("No he entrado")

    def inside(self, tokenList, semanticErrorList, begin, end):
        tipo=False
        valor=False
        fondo=False
        nombre=False
        valores=False
        evento=False
        state=0

        for counter in range(begin, end+1):
            token=tokenList[counter]

            
                

        
