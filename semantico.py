from io import open

class Simbolo:

    def __init__(self):

        self.identificador = ""
        self.tipo = ""
        self.tipoDato = ""
        self.ambito = ""

    def printSimbolo(self):

        print(f"Identificador: {self.identificador}\t Tipo: {self.tipo}\t Tipo de Dato: {self.tipoDato}\t Ambito: {self.ambito}")

class Funcion(Simbolo):

    def __init__(self):

        self.identificador = ""
        self.tipo = ""
        self.tipoDato = ""
        self.ambito = ""
        '''Numero de parametros se usa para verificar al momento que la funcion sea llamada'''
        self.numParametros = 0

class Semantico:

    def __init__(self):

        self.tablaSimbolos = []
        self.listaErrores = []
        self.ambito = "Global"
        self.sangriaActual = 0
        '''Para saber si se agrega un return al final de una funcion en el archivo'''
        self.regresa = False
        self.asignacion = False
        self.variableAsignacion = ""

    def createFile(self):

        file = open("traduccion.asm","a+")

        '''Agrega las instrucciones principales al inicio del archivo ASM'''
        file.write('.386\n')
        file.write('.model flat, stdcall\n')
        file.write('option casemap:none\n\n')
        file.write('include c:\masm32\include\masm32rt.inc\n\n')
        file.write('.code\n\n')

        file.close()

    '''ABRE EL ARCHIVO'''

    def analiza(self, n, archivo):
        
        contador = 0
        siguiente = -1
        if len(n.elementosEliminados) > 0:

            for i in reversed(n.elementosEliminados):

                if i.nodo.regla == "DefFunc" and i.id == 2 :
                    
                    '''CREA EL SIMBOLO FUNCION'''
                    funcion = Funcion()
                    funcion.tipo = "Funcion"
                    funcion.tipoDato = i.nodo.elementosEliminados[-1].valor
                    funcion.ambito = "Global"

                    '''Comprueba si la funcion existe'''
                    if self.buscaFuncion(funcion.identificador,funcion.ambito,funcion.tipoDato) == False:

                        '''Establece el nuevo ambito'''
                        self.ambito = i.nodo.elementosEliminados[-2].valor

                        '''Agrega el simbolo a la tabla de simbolos'''
                        self.tablaSimbolos.append(funcion)
                        funcion.identificador = i.nodo.elementosEliminados[-2].valor
                        '''AGREGA LA FUNCION AL ARCHIVO ASM, NO AGREGA SALTO DE LINEA POR SI EXISTEN PARAMETROS'''
                        stringAux = f'{funcion.identificador} proc'
                        archivo.write(stringAux)
                    else:

                        error = f"ERROR: funcion '{funcion.identificador}' redefinida"
                        self.listaErrores.append(error)

                '''DETERMINA SI ES EL FIN DE LA FUNCION PARA ESCRIBIRLO EN EL ARCHIVO'''
                if i.id == 1 and i.valor == "}":

                    '''En caso de ser la funcion principal, al final se agrega el end main para finalizar el codigo'''
                    if self.ambito == "main":

                        if self.regresa == True:
                            archivo.write("ret\n")
                            self.regresa = False
                        archivo.write("invoke ExitProcess, 0\n\nmain endp\nend main")
                    else:

                        if self.regresa == True:
                            archivo.write("ret\n")
                            self.regresa = False
                        archivo.write(f"{self.ambito} endp\n\n")
                
                if i.id == 2 and i.nodo.regla == "Parametros" and len(i.nodo.elementosEliminados) > 0:

                    '''Crea simbolo de parametros'''

                    nodoAux = i.nodo

                    parametro = Simbolo()
                    parametro.tipo = "Parametro"
                    parametro.tipoDato = nodoAux.elementosEliminados[-1].valor
                    parametro.identificador = nodoAux.elementosEliminados[-2].valor
                    parametro.ambito = self.ambito

                    '''Comprueba si la variable existe'''
                    if self.buscaParametro(parametro.identificador,parametro.ambito,parametro.tipoDato) == False:

                        self.tablaSimbolos.append(parametro)
                        self.aumentaNumParametros(self.ambito,"Global")
                        '''AGREGA EL PARAMETRO AL ARCHIVO ASM'''
                        stringAux = f' {parametro.identificador}:DWORD'
                        archivo.write(stringAux)

                        listaParam = nodoAux.elementosEliminados[0].nodo

                        '''COMPRUEBA SI HAY MAS DE 1 PARAMETRO'''
                        if listaParam.regla == "ListaParam" and len(listaParam.elementosEliminados)>0:

                            '''LA FUNCION ES RECURSIVA EN EL CASO DE QUE EXISTAN MULTIPLES DELCARACIONES'''
                            self.agregaListaParam(listaParam,archivo)
                            archivo.write('\n')
                    
                    else:

                        error = f"ERROR: parametro '{parametro.identificador}' definido dos veces"
                        self.listaErrores.append(error)

                if i.id == 2 and i.nodo.regla == "Parametros" and len(i.nodo.elementosEliminados) == 0:

                    '''Esta verificacion es para acomodar el archivo asm, si no hay parametros agrega un salto de linea'''
                    archivo.write('\n')

                if i.id == 2 and i.nodo.regla == "DefVar":

                    '''Crea simbolo de variable'''
                    nodoAux = i.nodo

                    variable = Simbolo()
                    variable.tipo = "Variable"
                    variable.tipoDato = nodoAux.elementosEliminados[-1].valor
                    variable.identificador = nodoAux.elementosEliminados[-2].valor
                    variable.ambito = self.ambito

                    if self.buscaIdentificador(variable.identificador,variable.ambito,variable.tipoDato) == False:

                        self.tablaSimbolos.append(variable)
                        '''AGREGA LA VARIABLE AL ARCHIVO ASM'''
                        stringAux = f'local {variable.identificador}:DWORD\n'
                        archivo.write(stringAux)

                        listVar = nodoAux.elementosEliminados[1].nodo

                        '''Comprueba si hay otra variable declarada'''
                        if listVar.regla == "ListaVar" and len(listVar.elementosEliminados) > 0:

                            '''LA FUNCION ES RECURSIVA EN EL CASO DE QUE EXISTAN MULTIPLES DELCARACIONES'''
                            self.agregaListaVar(nodoAux.elementosEliminados[-1].valor,listVar,archivo)


                    else:

                        error = f"ERROR: variable '{variable.identificador}' redefinida"
                        self.listaErrores.append(error)

                if i.id == 2 and i.nodo.regla == "Termino" and i.valor == "36":

                    '''Comprueba si la variable existe'''
                    terminalAux = i.nodo.elementosEliminados[0]

                    if not self.existeIdentificador(terminalAux.valor,self.ambito) and not self.existeParametro(terminalAux.valor,self.ambito):

                        error = f"ERROR: variable '{terminalAux.valor}' no definida"
                        self.listaErrores.append(error)

                if i.id == 2 and i.nodo.regla == "Sentencia" and i.valor == "21":

                    '''Comprueba si la variable se declaro y se puede asignar'''
                    terminalAux = i.nodo.elementosEliminados[-1]
                    
                    if not self.existeIdentificador(terminalAux.valor,self.ambito) and not self.existeParametro(terminalAux.valor,self.ambito):

                        error = f"ERROR: variable '{terminalAux.valor}' no definida"
                        self.listaErrores.append(error)

                    else:
 
                        '''En el caso de que todo este bien, agrega la asignacion al archivo e imprime el valor'''
                        '''Debido a que no existe una funcion print en el lenguaje, cada que se realice una asignacion se realiza un print en lenguaje ensamblador para comprobar el funcionamiento del programa'''
                        '''Se marca como que hubo una asignacion y cuando se llegue a la expresion despues de la sentencia, se escribe en el archivo'''
                        self.asignacion = True
                        self.variableAsignacion = terminalAux.valor
                        

                if i.id == 2 and i.nodo.regla == "LlamadaFunc" and i.valor == "40":

                    '''Comprueba si la funcion que se llama existe'''
                    terminalAux = i.nodo.elementosEliminados[-1]

                    if not self.existeFuncion(terminalAux.valor,"Global"):

                        error = f"ERROR: variable '{terminalAux.valor}' no definida"
                        self.listaErrores.append(error)
                    else:

                        '''Toma los argumentos si es que existen y los escribe en el archivo'''
                        arg = i.nodo.elementosEliminados[1]
                        if len(arg.nodo.elementosEliminados)>0:

                            termino = arg.nodo.elementosEliminados[-1].nodo.elementosEliminados[0].nodo.elementosEliminados[0].valor
                            '''Mueve el valor al registro y le hace push a la pila del ensamblador'''
                            archivo.write(f"mov eax, {termino}\n")
                            archivo.write("push eax\n")

                            '''Comprueba si hay mas de un argumento'''
                            if len(arg.nodo.elementosEliminados[0].nodo.elementosEliminados)>0:

                                self.agregaArgumentos(arg.nodo.elementosEliminados[0],archivo)
                    
                    '''Consigue la funcion y comprueba si tienen el mismo numero de parametros'''
                    funcionAux = self.regresaFuncion(terminalAux.valor,"Global")
                    argumentos = i.nodo.elementosEliminados[1]
                    
                    if len(argumentos.nodo.elementosEliminados) < funcionAux.numParametros:

                        error = f"ERROR: numero de argumentos no coincide"
                        self.listaErrores.append(error)

                    '''Al final agrega la llamada de la funcion al archivo ASM'''
                    archivo.write(f"call {terminalAux.valor}\n")

                    '''Comprueba si hubo una asignacion previa, para realizar un print'''
                    if self.asignacion == True:

                        archivo.write(f"mov {self.variableAsignacion}, eax\n")
                        archivo.write(f"mov eax, {self.variableAsignacion}\n")
                        archivo.write("print str$(eax)\n")
                        self.asignacion = False
                        self.variableAsignacion = ""

                '''Si hay un return al final de la funcion se marca para agregarlo al final de la funcion'''
                if i.id == 2 and i.nodo.regla == "ValorRegresa":

                    self.regresa = True

                '''COMPRUEBA SI HAY ALGUNA OPERACION PARA ESCRIBIRLA EN EL ARCHIVO'''
                if i.id == 2 and i.nodo.regla == "Expresion":

                    '''Suma'''
                    if i.valor == "47" and i.nodo.elementosEliminados[1].valor == "+":

                        '''Obtiene el primer y segundo termino para la suma'''
                        termino_1 = i.nodo.elementosEliminados[-1].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor
                        termino_2 = i.nodo.elementosEliminados[0].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor

                        archivo.write(f"mov eax, {termino_1}\n")
                        archivo.write(f"add eax, {termino_2}\n")

                        '''Comprueba si hubo asignacion para imprimir el valor'''
                        if self.asignacion == True:

                            archivo.write(f"mov {self.variableAsignacion}, eax\n")
                            archivo.write(f"mov eax, {self.variableAsignacion}\n")
                            archivo.write("print str$(eax)\n")
                            self.asignacion = False
                            self.variableAsignacion = ""

                    '''Resta'''
                    if i.valor == "47" and i.nodo.elementosEliminados[1].valor == "-":

                        termino_1 = i.nodo.elementosEliminados[-1].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor
                        termino_2 = i.nodo.elementosEliminados[0].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor

                        archivo.write(f"mov eax, {termino_1}\n")
                        archivo.write(f"sub eax, {termino_2}\n")
                        '''Comprueba si hubo asignacion para imprimir el valor'''
                        if self.asignacion == True:

                            archivo.write(f"mov {self.variableAsignacion}, eax\n")
                            archivo.write(f"mov eax, {self.variableAsignacion}\n")
                            archivo.write("print str$(eax)\n")
                            self.asignacion = False
                            self.variableAsignacion = ""

                if i.id == 2 :

                    i.nodo.sangria = self.sangriaActual
                    i.nodo.printRegla()
                    self.analiza(i.nodo,archivo)

                contador+=1

            '''Continua el recorrido del arbol'''
            self.sangriaActual = self.sangriaActual + round(len(n.elementosEliminados[siguiente].nodo.regla)/2)
            #self.analiza(n.elementosEliminados[siguiente].nodo)

        

    def buscaIdentificador(self,nombre,ambito,tipo):

        for i in self.tablaSimbolos:

            if i.tipo == "Variable" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:

                return True

        return False
    
    def existeIdentificador(self,nombre,ambito):

        for i in self.tablaSimbolos:

            if i.tipo == "Variable" and i.identificador == nombre and i.ambito == ambito:

                return True

        return False
 
    def buscaFuncion(self,nombre,ambito,tipo):

        for i in self.tablaSimbolos:

            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:

                return True

        return False

    def existeFuncion(self,nombre,ambito):

        for i in self.tablaSimbolos:

            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito:

                return True

        return False

    def buscaParametro(self,nombre,ambito,tipo):

        for i in self.tablaSimbolos:

            if i.tipo == "Parametro" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:

                return True

        return False

    def existeParametro(self,nombre,ambito):

        for i in self.tablaSimbolos:

            if i.tipo == "Parametro" and i.identificador == nombre and i.ambito == ambito:

                return True

        return False

    def agregaListaVar(self,tipo,nodo,archivo):

        segVariable = Simbolo()
        segVariable.tipo = "Variable"
        segVariable.tipoDato = tipo
        segVariable.identificador = nodo.elementosEliminados[-2].valor
        segVariable.ambito = self.ambito

        '''Comprueba si la variable ya existe'''
        if self.buscaIdentificador(segVariable.identificador,segVariable.ambito,segVariable.tipoDato) == False:

            self.tablaSimbolos.append(segVariable)
            '''AGREGA LAS VARIABLES AL ARCHIVO'''
            archivo.write(f'local {segVariable.identificador}:DWORD\n')

            listaVar = nodo.elementosEliminados[0].nodo
            if listaVar.regla == "ListaVar" and len(listaVar.elementosEliminados) > 0:

                self.agregaListaVar(tipo,listaVar)
        
        else:

            error = f"ERROR: variable '{segVariable.identificador}' redefinida"
            self.listaErrores.append(error)

    def agregaListaParam(self,nodo,archivo):

        segParametro  = Simbolo()
        segParametro.tipo = "Parametro"
        segParametro.tipoDato = nodo.elementosEliminados[-2].valor
        segParametro.identificador = nodo.elementosEliminados[-3].valor
        segParametro.ambito = self.ambito

        '''Comprueba si el parametro ya se declaro'''
        if self.buscaParametro(segParametro.identificador,segParametro.ambito,segParametro.tipoDato) == False:

            self.tablaSimbolos.append(segParametro)
            self.aumentaNumParametros(self.ambito,"Global")
            '''AGREGA EL SIGUIENTE PARAMETRO AL ARCHIVO ASM'''
            stringAux = f',{segParametro.identificador}:DWORD'
            archivo.write(stringAux)

            listaParam = nodo.elementosEliminados[0].nodo
            if listaParam.regla == "ListaParam" and len(listaParam.elementosEliminados) > 0:

                self.agregaListaParam(listaParam)

        else:

            error = f"ERROR: parametro '{segParametro.identificador}' definido dos veces"
            self.listaErrores.append(error)

    '''Metodo para agregar los argumentos al archivo ASM'''
    def agregaArgumentos(self,nodo,archivo):

        arg = nodo.nodo.elementosEliminados[1].nodo.elementosEliminados[0].nodo.elementosEliminados[0].valor
        archivo.write(f"mov eax, {arg}\n")
        archivo.write("push eax\n")

        if len(nodo.nodo.elementosEliminados[0].nodo.elementosEliminados)>0:

            self.agregaArgumentos(nodo.nodo.elementosEliminados[0].nodo.elementosEliminados,archivo)

    def aumentaNumParametros(self,nombre,ambito):

        for i in self.tablaSimbolos:

            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito:

                i.numParametros +=1

    def regresaFuncion(self,nombre,ambito):

        for i in self.tablaSimbolos:

            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito:

                return i

    def muestraSimbolos(self):

        print("************* TABLA DE SIMBOLOS *************\n")
        for i in self.tablaSimbolos:

            i.printSimbolo()

    def muestraErrores(self):

        print("************* ERRORES *************\n")
        for i in self.listaErrores:

            print(i)