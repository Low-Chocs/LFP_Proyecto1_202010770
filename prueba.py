from lexical import lexicalAnalyzer as analyzer

lexical=analyzer()

lexical.analyzer('''formulario~>>[   
   <
      tipo:"etiqueta",
      valor: "Nombre:",
    >,
    <
      tipo:"texto",
      valor: "Nombre",
      fondo: "Ingrese nombre"
    >,
    <
      tipo:"grupo-radio",
      valor: "sexo",
      valores:['Masculino','Femenino']
    >,
    <
      tipo:"grupo-option",
      valor: "pais",
      valores:['Guatemala','El Salvador','Honduras','Mexico']
    >, 

        <
      tipo:"grupo-radio",
      valor: "sexo",
      valores:['Masculino','Femenino']
    >,
    <
      tipo:"grupo-option",
      valor: "pais",
      valores:['Guatemala','El Salvador','Honduras','Mexico']
    >, 
        <
      tipo:"grupo-radio",
      valor: "sexo",
      valores:['Masculino','Femenino']
    >,
    <
      tipo:"grupo-option",
      valor: "pais",
      valores:['Guatemala','El Salvador','Honduras','Mexico']
    >, 
    <
       tipo:"boton",
       valor: "validar",
       evento: "entrada"
     >
]    '''  )

lexical.returnTokenList()
lexical.semanticAnalyzer()
lexical.returnErrorList()
lexical.returnSemanticError()
    
