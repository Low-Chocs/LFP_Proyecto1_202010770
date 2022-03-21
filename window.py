from tkinter import *
from tkinter import N, filedialog
from lexical import lexicalAnalyzer as lexical
from web import reports
from web import Errors
import os
analizeButtonState="DISABLED"

lexic=lexical()
tokenList=[]
errorList=[]
semanticList=[]



#To do list, this function needs to show only the .format files
def loadFile():                                                     
	global route
	route = filedialog.askopenfilename(title="Select A file")  

	with open(route,"r") as file:
		selectedFile=file.read()

	entryBox.insert(INSERT, selectedFile)    		
    	
def deleteTextfromBox():
	entryBox.delete("1.0","end")

def analyzer():
    if entryBox.get("1.0",'end-1c')!= "":
        global tokenList 
        global errorList
        global semanticList
        tokenList=[]
        errorList=[]
        semanticList=[]
        lexic.analyzer(entryBox.get("1.0",'end-1c'))
        lexic.semanticAnalyzer()
        tokenList=lexic.returnTokenList()
        errorList=lexic.returnErrorList()
        semanticList=lexic.returnSemanticError()

def tokenTable():
        web=reports()
        global tokenList
        if len(tokenList)>1:
        	web.table(tokenList)

def errorTable():
        theError=Errors()
        global errorList
        global semanticList
        if len(errorList)>=1 or len(semanticList)>=1:
            theError.table(errorList,semanticList)

def tecnico():
    os.startfile('ManualTécnico.pdf')

def usuario():
    os.startfile('ManualUsuario.pdf')

		

    
#We create the window
root=Tk()
myMenu=Menu(root)
root.config(menu=myMenu)
root.geometry("850x500")

#Here comes the buttons
selectFileButton = Button(root, text="Seleccionar Archivo", padx=15, pady=15, command=loadFile)
selectFileButton.place(x=10, y=10)
deleteButton = Button(root, text="Remover todo el texto", padx=15, pady=15, command=deleteTextfromBox)
deleteButton.place(x=375, y=10)


analyzeBotton= Button(root, text="Analizar Archivo",padx=15, pady=15, command=analyzer)
analyzeBotton.place(x=200, y=10)

#Here comes the entry box
entryBox=Text(root,width=103, height=24)
entryBox.place(x=10, y=100)

#Cascade Menu ->Reports
cascadeMenu= Menu(myMenu)
myMenu.add_cascade(label="Reportes", menu=cascadeMenu)
cascadeMenu.add_command(label="Reporte de tokens", command=tokenTable)
cascadeMenu.add_command(label="Reporte de errores", command=errorTable)
cascadeMenu.add_command(label="Manual tecnico ", command=tecnico)
cascadeMenu.add_command(label="Manual de usuario", command=usuario)




root.mainloop()