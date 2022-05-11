
class Simbolo:

    def __init__(self):

        self.identificador = ""
        self.tipo = ""
        self.tipoDato = ""
        self.ambito = ""

    def printSimbolo(self):

        print(f"Identificador: {self.identificador}\t Tipo: {self.tipo}\t Tipo de Dato: {self.tipoDato}\t Ambito: {self.ambito}")


class Semantico:

    def __init__(self):

        self.tablaSimbolos = []
        self.listaErrores = []
        self.ambito = "Global"

    def analiza(self, n):

        contador = 0
        siguiente = -1
        if len(n.elementosEliminados) > 0:

            for i in reversed(n.elementosEliminados):

                '''Toma el primer NT el cual es el que continua el recorrido del arbol'''
                if i.id == 2 :

                    if len(i.nodo.elementosEliminados) > 0:

                        siguiente = contador
                        siguiente = -abs(siguiente+1)
                if i.nodo.regla == "DefFunc" and i.id == 2 :
                    
                    '''CREA EL SIMBOLO FUNCION'''
                    funcion = Simbolo()
                    funcion.tipo = "Funcion"
                    funcion.tipoDato = i.nodo.elementosEliminados[-1].valor
                    funcion.identificador = i.nodo.elementosEliminados[-2].valor
                    funcion.ambito = self.ambito

                    '''Comprueba si la funcion existe'''
                    if self.buscaFuncion(funcion.identificador,funcion.ambito,funcion.tipoDato) == False:

                        '''Establece el nuevo ambito'''
                        self.ambito = i.nodo.elementosEliminados[-2].valor

                        '''Agrega el simbolo a la tabla de simbolos'''
                        self.tablaSimbolos.append(funcion)
                    else:

                        error = f"ERROR: funcion '{funcion.identificador}' redefinida"
                        self.listaErrores.append(error)
                
                elif i.id == 2 and i.nodo.regla == "Parametros" and len(i.nodo.elementosEliminados) > 0:

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

                        listaParam = nodoAux.elementosEliminados[0].nodo

                        '''COMPRUEBA SI HAY MAS DE 1 PARAMETRO'''
                        if listaParam.regla == "ListaParam" and len(listaParam.elementosEliminados)>0:

                            '''LA FUNCION ES RECURSIVA EN EL CASO DE QUE EXISTAN MULTIPLES DELCARACIONES'''
                            self.agregaListaParam(listaParam)
                    
                    else:

                        error = f"ERROR: parametro '{parametro.identificador}' definido dos veces"
                        self.listaErrores.append(error)

                elif i.id == 2 and i.nodo.regla == "DefVar":

                    '''Crea simbolo de variable'''
                    nodoAux = i.nodo

                    variable = Simbolo()
                    variable.tipo = "Variable"
                    variable.tipoDato = nodoAux.elementosEliminados[-1].valor
                    variable.identificador = nodoAux.elementosEliminados[-2].valor
                    variable.ambito = self.ambito

                    if self.buscaIdentificador(variable.identificador,variable.ambito,variable.tipoDato) == False:

                        self.tablaSimbolos.append(variable)

                        listVar = nodoAux.elementosEliminados[1].nodo

                        '''Comprueba si hay otra variable declarada'''
                        if listVar.regla == "ListaVar" and len(listVar.elementosEliminados) > 0:

                            '''LA FUNCION ES RECURSIVA EN EL CASO DE QUE EXISTAN MULTIPLES DELCARACIONES'''
                            self.agregaListaVar(nodoAux.elementosEliminados[-1].valor,listVar)

                    else:

                        error = f"ERROR: variable '{variable.identificador}' redefinida"
                        self.listaErrores.append(error)

                contador+=1

            '''Continua el recorrido del arbol'''
            self.analiza(n.elementosEliminados[siguiente].nodo)

    def buscaIdentificador(self,nombre,ambito,tipo):

        for i in self.tablaSimbolos:

            if i.tipo == "Variable" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:

                return True

        return False
 
    def buscaFuncion(self,nombre,ambito,tipo):

        for i in self.tablaSimbolos:

            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:

                return True

        return False

    def buscaParametro(self,nombre,ambito,tipo):

        for i in self.tablaSimbolos:

            if i.tipo == "Parametro" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:

                return True

        return False

    def agregaListaVar(self,tipo,nodo):

        segVariable = Simbolo()
        segVariable.tipo = "Variable"
        segVariable.tipoDato = tipo
        segVariable.identificador = nodo.elementosEliminados[-2].valor
        segVariable.ambito = self.ambito

        '''Comprueba si la variable ya existe'''
        if self.buscaIdentificador(segVariable.identificador,segVariable.ambito,segVariable.tipoDato) == False:

            self.tablaSimbolos.append(segVariable)

            listaVar = nodo.elementosEliminados[0].nodo
            if listaVar.regla == "ListaVar" and len(listaVar.elementosEliminados) > 0:

                self.agregaListaVar(tipo,listaVar)
        
        else:

            error = f"ERROR: variable '{segVariable.identificador}' redefinida"
            self.listaErrores.append(error)

    def agregaListaParam(self,nodo):

        segParametro  = Simbolo()
        segParametro.tipo = "Parametro"
        segParametro.tipoDato = nodo.elementosEliminados[-2].valor
        segParametro.identificador = nodo.elementosEliminados[-3].valor
        segParametro.ambito = self.ambito

        '''Comprueba si el parametro ya se declaro'''
        if self.buscaParametro(segParametro.identificador,segParametro.ambito,segParametro.tipoDato) == False:

            self.tablaSimbolos.append(segParametro)

            listaParam = nodo.elementosEliminados[0].nodo
            if listaParam.regla == "ListaParam" and len(listaParam.elementosEliminados) > 0:

                self.agregaListaParam(listaParam)

        else:

            error = f"ERROR: parametro '{segParametro.identificador}' definido dos veces"
            self.listaErrores.append(error)

    def muestraSimbolos(self):

        print("************* TABLA DE SIMBOLOS *************\n")
        for i in self.tablaSimbolos:

            i.printSimbolo()

    def muestraErrores(self):

        print("************* ERRORES *************\n")
        for i in self.listaErrores:

            print(i)