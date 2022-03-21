from Token import Token
from Token import Error
from Token import semanticError
from semantic import semantic
from web import web
import os

class lexicalAnalyzer:
    def __init__(self):
        self.tokensList=[]
        self.errrorsList=[]
        self.semanticErrors=[]
        self.textoEntrada=""
        

    def analyzer(self,text):
        self.tokensList=[]
        self.errrorsList=[]
        self.semanticErrors=[]
        self.textoEntrada=""
        self.textoEntrada=text
        counter=0
        newLetter=""
        wordIsComplete="#"
        state=0
        line=0
        column=0
        fFormulario=False
        oFormulario=False
        rFormulario=False
        mFormulario=False
        uFormulario=False
        lFormulario=False
        aFormulario=False
        rFormulario2=False
        iFormulario=False

        tTipo=False
        iTipo=False
        pTipo=False

        vValor=False
        aValor=False
        lValor=False
        oValor=False
        rValores=False
        eValores=False

        nFondo=False
        dFondo=False

        nNombre=False
        oNombre=False
        mNombre=False
        bNombre=False
        rNombre=False

        eEvento=False
        vEvento=False
        eEvento2=False
        nEvento=False
        tEvento=False

        iInfo=False
        nInfo=False
        fInfo=False

        nEntrada=False
        tEntrada=False
        rEntrada=False
        aEntrada=False
        dEntrada=False
        

        for char in range(len(text)):
            letter=text[char]

            if letter=="#":
                print("Se ha leído exitosamente")
                break
                
            if state==0:
                if letter==" ":
                    column+=1
                
                elif letter=="\n":
                    line+=1
                    column=0
                elif letter=="\"" or letter=="\'":
                    state=1
                    column+=1
                elif letter== 'f' or letter=='F':
                    newLetter+=letter
                    column+=1
                    state=2
                    fFormulario=True
                elif letter== 't' or letter=='T':
                    newLetter+=letter
                    column+=1
                    state=2
                    tTipo=True
                elif letter== 'v' or letter=='V':
                    newLetter+=letter
                    column+=1
                    state=2
                    vValor=True
                elif letter== 'n' or letter=='N':
                    newLetter+=letter
                    column+=1
                    state=2
                    nNombre=True
                
                elif letter== 'e' or letter=='E':
                    newLetter+=letter
                    column+=1
                    state=2
                    eEvento=True
                
                elif letter== 'i' or letter=='I':
                    newLetter+=letter
                    column+=1
                    state=2
                    iInfo=True
                

                elif letter=='>' or letter=='[' or letter=='<' or letter =='~' or letter=="]" or letter==':' or letter==',':
                    column+=1
                    newLetter+=letter
                    if letter=="~":
                        token=Token("Primera apertura",newLetter,line, column)
                    elif letter==">":
                        token=token=Token("Cierra",newLetter,line, column)
                    elif letter=="[":
                        token=Token("Apertura",newLetter,line, column)
                    elif letter=="<":
                        token=Token("Abre",newLetter,line, column)
                    elif letter==":":
                        token=Token("Asignacion",newLetter,line, column)
                    elif letter==",":
                        token=Token("Separador",newLetter,line, column)
                    elif letter=="]":
                        token=Token("Cerradura",newLetter,line, column)
                    self.tokensList.append(token)
                    newLetter=""
                    state=0
                
                elif letter=='\'':
                    newLetter+=letter
                    column+=1
                    state = 12
                
            #String State
            elif state==1:
                
                if letter=="\"":
                    column+=1
                    token=Token("Cadena",newLetter,line, column)
                    self.tokensList.append(token)
                    newLetter=""
                    state=0
                elif letter=="\'":
                    column+=1
                    token=Token("Cadena",newLetter,line, column)
                    self.tokensList.append(token)
                    newLetter=""
                    state=0
                else:
                    newLetter+=letter
                    column+=1

            elif letter==" ":
                column+=1
                continue
                
            elif letter=="\n":
                line+=1
                column=0
                continue

            #Reserved words
            elif state==2:
                

                #Fo ->Formulario|Fondo
                if fFormulario:
                    if letter=='o' or letter=='O':
                        oFormulario=True
                        newLetter+=letter
                        column+=1
                        state=3
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: O|o para formar: Formulario|Fondo",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Ti ->Tipo
                elif tTipo:
                    if letter=='i' or letter=='I':
                        iTipo=True
                        newLetter+=letter
                        column+=1
                        state=3
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        tTipo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: I|i para formar: Tipo",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Va ->Valor|Valores
                elif vValor:
                    if letter=='a' or letter=='A':
                        aValor=True
                        newLetter+=letter
                        column+=1
                        state=3
                    else:
                        column+=1
                        state=0
                        vValor=False
                        newLetter+=letter
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: A|a para formar: Valor|Valores",line,column)
                        self.errrorsList.append(error)
                #No -> Nombre
                elif nNombre:
                    if letter=='o' or letter=='O':
                        oNombre=True
                        newLetter+=letter
                        column+=1
                        state=3
                    else:
                        column+=1
                        state=0
                        nNombre=False
                        newLetter+=letter
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: O|o para formar: Nombre",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Ev ->Evento
                elif eEvento:
                    if letter=='v' or letter=='V':
                        vEvento=True
                        newLetter+=letter
                        column+=1
                        state=3
                    #En -> Entrada
                    elif letter=='n' or letter=='N':
                        eEvento=False
                        nEntrada=True
                        newLetter+=letter
                        column+=1
                        state=3
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        eEvento=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: V|v para formar : Evento o N|n para formar Entrada",line,column)
                        self.errrorsList.append(error)
                        newLetter=""

                #In -> Info
                elif iInfo:
                    if letter=='n' or letter=='N':
                        nInfo=True
                        newLetter+=letter
                        column+=1
                        state=3
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        iInfo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: N|n para formar: Info",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
            
            elif state==3:
                #For -> Formulario | Fon->Fondo
                if oFormulario:
                    if letter=='r' or letter=='R':
                        rFormulario=True
                        newLetter+=letter
                        column+=1
                        state=4
                    elif letter=='n'or letter=='N':
                        oFormulario=False
                        fFormulario=False
                        nFondo=True
                        newLetter+=letter
                        column+=1
                        state=4
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),
                        "Se esperaba: R|r para formar: Formulario Se esperaba: N|n para formar: Fondo",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Tip -> Tipo   
                elif iTipo:
                    if letter=='p' or letter=='P':
                        pTipo=True
                        newLetter+=letter
                        column+=1
                        state=4
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        tTipo=False
                        iTipo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: P|p para formar: Tipo",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Val -> Valor| Valores
                elif aValor:
                    if letter=='l' or letter=='L':
                        lValor=True
                        newLetter+=letter
                        column+=1
                        state=4
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        vValor=False
                        aValor=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: L|l para formar: Valor|Valores",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Eve -> Evento 
                elif vEvento:
                    if letter=='e' or letter=='E':
                        eEvento2=True
                        newLetter+=letter
                        column+=1
                        state=4
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        eEvento=False
                        vEvento=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: E|e para formar: Evento",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #En -> Entrada
                elif nEntrada:
                    if letter=='t' or letter=='T':
                        tEntrada=True
                        newLetter+=letter
                        column+=1
                        state=4
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nEntrada=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: T|t para formar: Entrada",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Nom -> Nombre 
                elif oNombre:
                    if letter=='m' or letter=='M':
                        mNombre=True
                        newLetter+=letter
                        column+=1
                        state=4
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nNombre=False
                        oNombre=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: M|m para formar: Nombre",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                
                #In -> Info
                elif iInfo:
                    if letter=='f' or letter=='F':
                        fInfo=True
                        newLetter+=letter
                        column+=1
                        state=4
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        iInfo=False
                        fInfo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: F|f para formar: Info",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
            
            elif state==4:

                #Form -> Formulario
                if rFormulario:
                    if letter=='m' or letter=='M':
                        mFormulario=True
                        newLetter+=letter
                        column+=1
                        state=5
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: M|m para formar: Formulario",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Fond -> Fondo
                elif nFondo:
                    if letter=='d' or letter=='D':
                        dFondo=True
                        newLetter+=letter
                        column+=1
                        state=5
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nFondo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: D|d para formar: Fondo",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Even -> Evento
                elif eEvento2:
                    if letter=='n' or letter=='N':
                        nEvento=True
                        newLetter+=letter
                        column+=1
                        state=5
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        eEvento=False
                        vEvento=False
                        eEvento2=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: N|n para formar: Evento",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Entr -> Entrada
                elif tEntrada:
                    if letter=='r' or letter=='R':
                        rEntrada=True
                        newLetter+=letter
                        column+=1
                        state=5
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nEntrada=False
                        tEntrada=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: R|r para formar: Entrada",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Valo -> Valor|Valores
                elif lValor:
                    if letter=='o' or letter=='O':
                        oValor=True
                        newLetter+=letter
                        column+=1
                        state=5
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        vValor=False
                        aValor=False
                        lValor=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: O|o para formar: Valor|Valores",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Nomb -> Nombre
                elif mNombre:
                    if letter=='b' or letter=='B':
                        bNombre=True
                        newLetter+=letter
                        column+=1
                        state=5
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nNombre=False
                        oNombre=False
                        mNombre=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: B|b para formar: Nombre",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Tipo -> Tipo
                elif pTipo:
                    if letter=='o' or letter=='O':
                        column+=1
                        newLetter+=letter
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        newLetter=""
                        tTipo=False
                        iTipo=False
                        pTipo=False
                        state=0
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        tTipo=False
                        iTipo=False
                        pTipo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: O|o para formar: Tipo",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Info -> Info
                elif fInfo:
                    if letter=='o' or letter=='O':
                        newLetter+=letter
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        newLetter=""
                        iInfo=False
                        nInfo=False
                        fInfo=False
                        newLetter=""
                        column+=1
                        state=0
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        iInfo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: N|n para formar: Info",line,column)
                        self.errrorsList.append(error)
                        newLetter=""

            elif state==5:
                #Formu->Formulario
                if mFormulario:
                    if letter=='u' or letter=='U':
                        uFormulario=True
                        newLetter+=letter
                        column+=1
                        state=6
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        mFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: U|u para formar: Formulario",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Even->Evento        
                elif nEvento:
                    if letter=='t' or letter=='T':
                        tEvento=True
                        newLetter+=letter
                        column+=1
                        state=6
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        eEvento=False
                        vEvento=False
                        eEvento2=False
                        nEvento=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: T|t para formar: Evento",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Entra -> Entrada
                elif rEntrada:
                    if letter=='a' or letter=='A':
                        aEntrada=True
                        newLetter+=letter
                        column+=1
                        state=6
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nEntrada=False
                        tEntrada=False
                        rEntrada=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: A|a para formar: Entrada",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Fondo->Fondo
                elif dFondo:
                    if letter=='o' or letter=='O':
                        column+=1
                        newLetter+=letter
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        newLetter=""
                        nFondo=False
                        dFondo=False
                        state=0
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nFondo=False
                        dFondo=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: O|o para formar: Fondo",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Nombr->Nombre
                elif bNombre:
                    if letter=='r' or letter=='R':
                        rNombre=True
                        newLetter+=letter
                        column+=1
                        state=6
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nNombre=False
                        oNombre=False
                        mNombre=False
                        bNombre=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: R|r para formar: Nombre",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Valor->Valor|Valores
                elif oValor:
                    if letter=='r' or letter=='R':
                        if self.whoIsNext(char,text,1):
                            rValores=True
                            newLetter+=letter
                            column+=1
                            state=6
                            vValor=False
                            aValor=False
                            lValor=False
                            oValor=False
                            rValores=True
                        else:
                            column+=1
                            newLetter+=letter
                            token=Token("Palabra Reservada",newLetter,line, column)
                            self.tokensList.append(token)
                            newLetter=""
                            state=0
                            vValor=False
                            aValor=False
                            lValor=False
                            oValor=False
                            rValores=False
                            eValores=False

                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        vValor=False
                        aValor=False
                        lValor=False
                        oValor=False
                        rValores=False
                        eValores=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: E|e|  para formar: Valor|Valores",line,column)
                        self.errrorsList.append(error)
                        newLetter="" 

            elif state==6:
                #Formul->Formulario
                if uFormulario:
                    if letter=='l' or letter=='L':
                        lFormulario=True
                        newLetter+=letter
                        column+=1
                        state=7
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        mFormulario=False
                        uFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: L|l  para formar: Formulario",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Evento->Evento
                elif tEvento:
                    if letter=='o' or letter=='O':
                        newLetter+=letter
                        column+=1
                        state=0
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        newLetter=""
                        eEvento=False
                        vEvento=False
                        eEvento2=False
                        nEvento=False
                        tEvento=False
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        eEvento=False
                        vEvento=False
                        eEvento2=False
                        nEvento=False
                        tEvento=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: O|o  para formar: Evento",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Entrad -> Entrada
                elif aEntrada:
                    if letter=='d' or letter=='D':
                        dEntrada=True
                        newLetter+=letter
                        column+=1
                        state=7
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nEntrada=False
                        tEntrada=False
                        rEntrada=False
                        aEntrada=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: D|d para formar: Entrada",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Valore->Valores
                elif rValores:
                    if letter=='e' or letter=='E':
                        eValores=True
                        newLetter+=letter
                        column+=1
                        state=7
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        vValor=False
                        aValor=False
                        lValor=False
                        oValor=False
                        rValores=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: E|e  para formar: Valores",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                elif letter==' ':
                        column+=1
                #Nombre->Nombre
                elif rNombre:
                    if letter=='e' or letter=='E':
                        newLetter+=letter
                        column+=1
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        state=0
                        nNombre=False
                        oNombre=False
                        mNombre=False
                        bNombre=False
                        rNombre=False
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nNombre=False
                        oNombre=False
                        mNombre=False
                        bNombre=False
                        rNombre=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: E|e  para formar: Nombre",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                 

            elif state==7:
                #Formul->Formulario
                if lFormulario:
                    if letter=='a' or letter=='A':
                        aFormulario=True
                        newLetter+=letter
                        column+=1
                        state=8
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        mFormulario=False
                        uFormulario=False
                        lFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: A|a  para formar: Formulario",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Valores->Valores
                elif eValores:
                    if letter=='s' or letter=='S':
                        column+=1
                        newLetter+=letter
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        newLetter=""
                        state=0
                        vValor=False
                        aValor=False
                        lValor=False
                        oValor=False
                        rValores=False
                        eValores=False
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        vValor=False
                        aValor=False
                        lValor=False
                        oValor=False
                        rValores=False
                        eValores=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: S|s  para formar: Valores",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                #Entrada -> Entrada
                elif dEntrada:
                    if letter=='a' or letter=='A':
                        column+=1
                        newLetter+=letter
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        newLetter=""
                        state=0
                        nEntrada=False
                        tEntrada=False
                        rEntrada=False
                        aEntrada=False
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        nEntrada=False
                        tEntrada=False
                        rEntrada=False
                        aEntrada=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: A|a para formar: Entrada",line,column)
                        self.errrorsList.append(error)
                        newLetter=""

            elif state==8:
                #Formular->Formulario
                if aFormulario:
                    if letter=='r' or letter=='R':
                        rFormulario2=True
                        newLetter+=letter
                        column+=1
                        state=9
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        mFormulario=False
                        uFormulario=False
                        lFormulario=False
                        aFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: R|r  para formar: Formulario",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
                        

            elif state==9:
                #Formulari->Formulario
                if rFormulario2:
                    if letter=='i' or letter=='I':
                        iFormulario=True
                        newLetter+=letter
                        column+=1
                        state=10
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        mFormulario=False
                        uFormulario=False
                        lFormulario=False
                        aFormulario=False
                        rFormulario2=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: I|i  para formar: Formulario",line,column)
                        self.errrorsList.append(error)
                        newLetter=""

            elif state==10:
                #Formulario->Formulario
                if iFormulario:
                    if letter=='o' or letter=='O':
                        column+=1
                        newLetter+=letter
                        token=Token("Palabra Reservada",newLetter,line, column)
                        self.tokensList.append(token)
                        newLetter=""
                        state=0

                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        mFormulario=False
                        uFormulario=False
                        lFormulario=False
                        aFormulario=False
                        rFormulario2=False
                        iFormulario=False
                    else:
                        column+=1
                        state=0
                        newLetter+=letter
                        fFormulario=False
                        oFormulario=False
                        rFormulario=False
                        mFormulario=False
                        uFormulario=False
                        lFormulario=False
                        aFormulario=False
                        rFormulario2=False
                        iFormulario=False
                        error=Error("Entrada incorrecta: {} -> {}".format(newLetter,letter),"Se esperaba: O|o  para formar: Formulario",line,column)
                        self.errrorsList.append(error)
                        newLetter=""
            elif state ==11:
                column+=1
                newLetter+=letter
                if letter=="~":
                    token=Token("Primera apertura",newLetter,line, column)
                elif letter==">":
                    token=token=Token("Cierra",newLetter,line, column)
                elif letter=="[":
                    token=Token("Apertura",newLetter,line, column)
                elif letter=="<":
                    token=Token("Abre",newLetter,line, column)
                elif letter==":":
                    token=Token("Asignacion",newLetter,line, column)
                elif letter==",":
                    token=Token("Separador",newLetter,line, column)
                elif letter=="]":
                    token=Token("Cerradura",newLetter,line, column)
                self.tokensList.append(token)
                newLetter=""
                state=0

    def whoIsNext(self, pos,text,letter):
        for x in range(pos+1, len(text)):
            if text[x]!=" " or text[x]!="\n":
                if text[x]=="e" or text[x]=="E":
                    return True
                else:
                    return False

    def returnTokenList(self):
        return self.tokensList
    
    def returnErrorList(self):
        return self.errrorsList

    def returnSemanticError(self):
        return self.semanticErrors
    
    def semanticAnalyzer(self):
        state=0
        state2=False
        word=""
        dictionary={}
        valoresList=[]
        htmlWriter=web()
        for i in range(len(self.tokensList)):
            token=self.spelling(self.tokensList[i].getLexeme())
            print(token)

            if state==0:
                if token=="formulario":
                    state=1
                    continue
                else:
                    error=semanticError("Error Sintactico, se esperaba la palabra formulario")
                    self.semanticErrors.append(error)
                    break
                
            if state==1:
                if token=="~":
                    state=2
                    continue
                else:
                    error=semanticError("Error Sintactico, se esperaba el simbolo ~")
                    self.semanticErrors.append(error)
                    break
            
            
            elif state==2:
                if token==">" and state2==False:
                    state2=True
                    continue
                elif state2:
                    if token==">":
                        state=3
                        continue
                    else:
                        error=semanticError("Error Sintactico, se esperaba el simboolo >")
                        self.semanticErrors.append(error)
                        break
                else:
                    error=semanticError("Error Sintactico, se esperaba el simbolo >")
                    self.semanticErrors.append(error)
                    break
            
            elif state==3:
                if token=="[":
                    state=4
                    continue
                else:
                    error=semanticError("Error Sintactico, se esperaba el simbolo de apertura [")
                    self.semanticErrors.append(error)
                    break
            
            elif state==4:
                if token=="]":
                    break
                if token=="<":
                    state=5
                    continue
                else:
                    error=semanticError("Error Sintactico, no se a encontrado un < o ]")
                    self.semanticErrors.append(error)
                    break
            
            elif state==5:
                word=""
                if token ==">":
                    state=6
                    continue
                elif token =="tipo" or token=="valor" or token=="fondo" or token=="nombre" or token=="valores" or token=="evento":
                    state=7
                    word=token
                    continue
        
            elif state==6:
                if token ==",":
                    state=4
                elif token=="]":
                    htmlWriter.end()
                    self.htmlWrite(htmlWriter.returnHtml())
                    os.startfile("form.html")
                    break
                else:
                    error=semanticError("Error Sintactico, se esperaba un separador \",\" o un finalizador \"]\" ")
                    self.semanticErrors.append(error)
                    break
            
            elif state==7:
                if token==":":
                    if word=="tipo":
                        state=8
                    elif word=="valor":
                        state=9
                    elif word=="valores":
                        state=10
                    elif word=="fondo":
                        state=11
                    elif word=="evento":
                        state=12
                    elif word=="nombre":
                        state=15

            
            elif state==8:
                
                if token.replace(" ","")=="etiqueta":
                    print("entreee")
                    state=13
                    dictionary["Tipo"]="etiqueta"
                    print(dictionary["Tipo"])
                elif token.replace(" ","")=="texto":
                    state=13
                    dictionary["Tipo"]="texto"
                elif token.replace(" ","")=="grupo-radio":
                    state=13
                    dictionary["Tipo"]="grupo-radio"
                elif token.replace(" ","")=="grupo-option":
                    state=13
                    dictionary["Tipo"]="grupo-option"
                elif token.replace(" ","")=="boton":
                    dictionary["Tipo"]="boton"
                    state=13
                else:
                    error=semanticError("No se reconoce el tipo:{}".format(token))
                    self.semanticErrors.append(error)
                    state=13
            
            elif state==9:
                dictionary["Etiqueta"]=token
                state=13
                continue
            
            elif state==10:
                if token=="[":
                    state=14
                    continue
                else:
                    error=semanticError("Se esperaba un [")
                    self.semanticErrors.append(error)

            elif state==11:
                dictionary["Fondo"]=token
                state=13
                continue   

            elif state==12:
                dictionary["Evento"]=token
                state=13
                continue                  
            
            elif state==13:
                if token==",":
                    state=5
                    continue
                elif token==">":
                    state=6
                    self.htmlActions(htmlWriter, dictionary)
                    continue
                else:
                    error=semanticError("Se esperaba que se continuara \",\" o que se cerrara \">\" ")
                    self.semanticErrors.append(error)
                    break
            
            elif state==14:
                if token!="]":
                    if token!=",":
                        valoresList.append(token)
                        continue
                else:
                    state=13
                    dictionary["Valores"]=valoresList
                    continue

            elif state==15:
                dictionary["Etiqueta2"]=token
                state=13
                continue
            

    def htmlActions(self,object,dictionary):
        
        if "Tipo" in dictionary:
            print("Holaaa"+dictionary["Tipo"])
            if dictionary["Tipo"]=="etiqueta":
                name=""
                print(dictionary["Etiqueta"] +"cdadjskhjfehasjdk")
                if "Etiqueta" in dictionary:
                    name=dictionary["Etiqueta"] 
                    print("Este es el name"+name)
                object.label(name)
                
            elif dictionary["Tipo"]=="texto":
                name=""
                background=""
                if "Etiqueta" in dictionary:
                    name=dictionary["Etiqueta"]
                if "Fondo" in dictionary:
                    background=dictionary["Fondo"]
                object.inputForm(name,background)

            elif dictionary["Tipo"]=="grupo-radio":
                if "Valores" in dictionary:
                    name=""
                    list=dictionary["Valores"]

                    if "Etiqueta2" in dictionary:
                        name=dictionary["Etiqueta2"]
                    if "Etiqueta" in dictionary:
                        name=dictionary["Etiqueta"]

                    object.radioButton(name,list)
                    list.clear()
                else:
                    error=semanticError("No se encontraron valores")
                    self.semanticErrors.append(error)

            elif dictionary["Tipo"]=="grupo-option":
                if "Valores" in dictionary:
                    name=""
                    list=dictionary["Valores"]

                    if "Etiqueta2" in dictionary:
                        name=dictionary["Etiqueta2"]
                    if "Etiqueta" in dictionary:
                        name=dictionary["Etiqueta"]
                        
                    object.selectForm(name,list)
                    list.clear()
                else:
                    error=semanticError("No se encontraron valores")
                    self.semanticErrors.append(error)

            elif dictionary["Tipo"]=="boton":
                if "Evento" in dictionary:
                    event=dictionary["Evento"]
                    name=""
                    if "Etiqueta" in dictionary:
                        name=dictionary["Etiqueta"]
                    object.button(name, event, self.textoEntrada)
        else:
            error=semanticError("No se encontro el \"Tipo\" ")
            self.semanticErrors.append(error)


    
    def spelling(self, word):
        correctWord=""
        for char in range(len(word)):
            correctWord += word[char].lower()
        return correctWord
    
    def htmlWrite(self, write):

        with open("form.html","w") as writer:
            writer.write(write)
            writer.close()
        
