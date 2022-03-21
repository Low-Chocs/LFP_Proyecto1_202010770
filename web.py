import os
class web:

    def __init__(self):
        self.writer="""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="style.css"/>
            <title>Form</title>
        </head>
        <body>
        <header>
            <h1>Universidad de San Carlos de Guatemala</h1>
                    <p>Luis Mariano Moreira García 202010770</p>
            <form>
        </header>
        <div>
        <form>
        """
        self.radioCounter=0
        self.Ids=0
        self.textoEntrada=""
    
    def button(self, name, event, textoEntrada):
        self.textoEntrada=""
        self.textoEntrada=textoEntrada
        if name=="":
            name="Pulsa aquí"
        if event=="entrada":   
            self.writer+="""
            <section class="Buttons">
                <button type="button" onclick="showDocument()">{}</button>
            </section>
            """.format(name.capitalize())
    
    def inputForm(self, name, background):
        self.Ids+=1

        if name=="" and background=="":
            self.writer+='''
            <section class="Inputs">
                <input type="text" id="{}" name="name"/>
            </section>
            '''.format(self.Ids)
        elif background=="" and name!="":
            self.writer+='''
            <section class="Inputs">
                <input id="{}" name="nombre" placeholder="{}"/>
            </section>
            '''.format(self.Ids, name.capitalize())
        elif background!="" and name=="":
            self.writer+='''
            <section class="Inputs">
                <label for="nombre">{}</label>
                <input id="{}" name="nombre"/>
            </section>
            '''.format(self.Ids,background.capitalize())
        else:
            self.writer+='''
            <section class="Inputs">
                <label for="nombre">{}</label>
                <input type="" id="{}" name="nombre" placeholder="{}"/>
            </section>
            '''.format(name.capitalize(),self.Ids,background.capitalize())

    def selectForm(self, name, list):
        self.Ids+=1
        if name=="":
            self.writer+='''
            <section class="Selector">
                <select name="select">
            '''
        else: 
            self.writer+='''
            <section class="Selector">
                <label for="select">{}</label>
                <select name="select" id={}>
            '''.format(name.capitalize(),self.Ids)
        counter=1

        for element in list:
            self.writer+='''
                    <option value="{}">{}</option>
            '''.format(counter, element.capitalize())
            counter+=1
        self.writer+="</select>"

        self.writer+='</section>'

    def radioButton(self, name, list):
        self.writer+="<section class=\"Radio\">"
        if name!="":
            self.writer+="<label for=\"{}\">{}</label>".format(self.radioCounter,name.capitalize())
            for element in list:
                self.writer+='''
                <input type="radio" id="{}" name="{}">{}
                '''.format(element, self.radioCounter,element.capitalize())
        else:
            for element in list:
                self.writer+='''
                <input type="radio" id="{}" name="{}">{}
                '''.format(element, self.radioCounter,element)
        self.writer+='</section>'
        self.radioCounter+=1
    
    def label(self, name):
        if name != "":
            self.writer+='''
            <section>
            <p>{}</p>
            </section>
            '''.format(name)

    def end(self):
        self.writer+="""

        <section>
            <textarea name="information" id="doc" cols="100" rows="40" hidden>"""+self.textoEntrada+"""</textarea>
        </section>

        <section>
            <textarea name="information" id="answers" cols="100" rows="40" hidden></textarea>
        </section>

        <script>
            function showDocument(){
                let formDocument= document.getElementById('doc');
                formDocument.removeAttribute('hidden');
            }
        </script>

        </form>
        </div>
        <footer>
        </footer>
        </body>
        <script> src="buttons.js" </script>
        </html>
        """
        

    def returnHtml(self):
        return self.writer

class reports:

    def __init__(self):
        self.writer="""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="style.css"/>
            <title>Token Report</title>
        </head>
        <body>
        <header>
            <h1>Universidad de San Carlos de Guatemala</h1>
                    <p>Luis Mariano Moreira García 202010770</p>
            <form>
        </header>
        <div>"""
    
    def table(self, list):
        self.writer+='''
        
        <table class="table table-dark">
    <thead>
    <tr>
    
      <th scope="col">#</th>
      <th scope="col">Tipo</th>
      <th scope="col">Lexema</th>
      <th scope="col">Línea</th>
      <th scope="col">Columna</th>
    </tr>
    </thead>
    <tbody>
    '''
        counter=0
        
        for i in list:
            counter+=1
            self.writer+='''   
        <tr>
            <th scope="row">{}</th>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        '''.format(counter,i.getType(),i.getLexeme(),i.getLine(),i.getColumn())

        self.writer+='''</tbody>

        </table> 
        </div>
        <footer>
        </footer>
        </body>
        </html>'''
        with open("token.html","w") as writer:
            writer.write(self.writer)
            writer.close()
        os.startfile("token.html")

class Errors:
    
    def __init__(self):
        self.writer="""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="style.css"/>
            <title>Error Report</title>
        </head>
        <body>
        <header>
            <h1>Universidad de San Carlos de Guatemala</h1>
                    <p>Luis Mariano Moreira García 202010770</p>
            <form>
        </header>
        <div>"""
    
    
    def table(self, list,list2):
        self.writer+='''
        
        <table class="table table-dark">
    <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Tipo</th>
      <th scope="col">Descripción del error</th>
      <th scope="col">Línea</th>
      <th scope="col">Columna</th>
    </tr>
    </thead>
    <tbody>
    '''
        counter=0
        
        for i in list:
            counter+=1
            self.writer+='''   
        <tr>
            <th scope="row">{}</th>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        '''.format(counter,i.getType(),i.getErrorDescription(),i.getLine(),i.getColumn())

        self.writer+='''</tbody>

        </table> 

                <table class="table table-dark">
    <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Error Semantico</th>
    </tr>
    </thead>
    <tbody>
    '''
        counter=0
        
        for i in list2:
            counter+=1
            self.writer+='''   
        <tr>
            <th scope="row">{}</th>
            <td>{}</td>

        </tr>
        '''.format(counter,i.getError())

        self.writer+='''</tbody>

        </table>
        </div>
        <footer>
        </footer>
        </body>
        </html>'''
        print(self.writer)
        with open("error.html","w") as writer:
            writer.write(self.writer)
            writer.close()
        os.startfile("error.html")

        