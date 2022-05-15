from io import open
from lexico import analizador
from stack import stack
import arbolSintactico
import elementoPila
import semantico

class sintactico:

    def __init__(self):
        
        self.pila = stack()
        #Variables para guardar la gramatica del compilador
        self.gramatica = []
        self.popElements = []
        self.nombreRegla = []
        self.matrizGramatica = []

    def ejercicio_1(self, entrada):

        self.pila.limpiar()
        #El analizador guarda la entrada
        lexico = analizador(entrada)
        #Divide la entrada por espacios
        entrada = entrada + " $"
        entradaDividida = entrada.split(" ")

        #Tabla LR para el primer ejercicio
        tabla_1 = [[2,0,0,4,0],[0,0,3,0,0],[0,-1,0,0,-2],[1,0,0,0,0]]

        #Se crea el primer elementoPila
        primerNT = elementoPila.noTerminal("$")
        #Segundo elementoPila
        primerEstado = elementoPila.estado("0")
        #Push a los elementos creados
        self.pila.push(primerNT)
        self.pila.push(primerEstado)

        valor = 0
        valida = False
        cont = 0
        
        while valida==False:

            if entradaDividida[cont] != "$":

                type = lexico.returnTipo(lexico.evaluaElemento(entradaDividida[cont]))

                if type == "Identificador": 

                    #Toma el valor de la tabla
                    valor = tabla_1[0][int(self.pila.top().returnValor())]

                    #Si es 0 es un error
                    if valor == 0:

                        break

                    else:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))

                        #Se crea el terminal
                        terminal = elementoPila.terminal(entradaDividida[cont])
                        
                        #Se crea el estado
                        estado = elementoPila.estado(str(valor))

                        self.pila.push(terminal)
                        self.pila.push(estado)

                elif type == "+":

                    #Toma el valor de la tabla
                    valor = tabla_1[1][int(self.pila.top().returnValor())]

                    #Si es 0 es un error
                    if valor == 0:

                        break

                    else:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))

                        #Se crea el terminal
                        terminal = elementoPila.terminal(entradaDividida[cont])
                        
                        #Se crea el estado
                        estado = elementoPila.estado(str(valor))
                        
                        self.pila.push(terminal)
                        self.pila.push(estado)

                cont=cont+1
            
            if entradaDividida[cont] == "$":

                valor = tabla_1[2][int(self.pila.top().returnValor())]

                if valor == 0:

                    break
                elif valor == -1:
    
                    print("Entrada: "+entrada+ " Aceptada")
                    valida = True

                elif valor < 0:

                    #Hace reduccion y hace pop a los 6 elementos
                    for i in range(6):

                        self.pila.pop()

                    print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))

                    noTerminal = elementoPila.noTerminal("E")
                    
                    estado = elementoPila.estado(str(abs(valor+1)))
                    
                    self.pila.push(noTerminal)
                    self.pila.push(estado)

    def ejercicio_2(self,entrada):

        self.pila.limpiar()
        tabla_2 = [[2,0,0,2,0],[0,0,3,0,0],[0,-1,-3,0,-2],[1,0,0,4,0]]

        #El analizador guarda la entrada
        lexico = analizador(entrada)
        #Divide la entrada por espacios
        entrada = entrada + " $"
        entradaDividida = entrada.split(" ")

        primerNT = elementoPila.noTerminal("$")
        primerE = elementoPila.estado("0")
        self.pila.push(primerNT)
        self.pila.push(primerE)

        valor = 0
        valida = False
        cont = 0

        while valida == False:

            type = lexico.returnTipo(lexico.evaluaElemento(entradaDividida[cont]))

            if type != "$":

                if type == "Identificador":

                    #Toma el valor de la tabla
                    valor = tabla_2[0][int(self.pila.top().returnValor())]

                elif type == "+":

                    valor = tabla_2[1][int(self.pila.top().returnValor())]

                #Verifica si hace reduccion o apila

                if valor > 0:

                    print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))

                    terminal = elementoPila.terminal(entradaDividida[cont])
                    estado = elementoPila.estado(str(valor))

                    self.pila.push(terminal)
                    self.pila.push(estado)
                    
                    cont+=1

                elif valor < 0:

                    if valor == -1:

                        print("Entrada: "+entrada+ " Aceptada")
                        valida = True
                        
                    #Regla 2
                    elif valor == -3:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        for i in range(2):
                            self.pila.pop()

                        #Toma el valor de la primera regla
                        valorE = tabla_2[3][int(self.pila.top().returnValor())]

                        noTerminal = elementoPila.noTerminal("E")
                        estado = elementoPila.estado(str(valorE))
                        self.pila.push(noTerminal)
                        self.pila.push(estado)
                            
                    #Regla 1
                    elif valor == -2:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        for i in range(6):
                            self.pila.pop()

                        #Toma el valor de la segunda regla
                        valorE = tabla_2[3][int(self.pila.top())]

                        noTerminal = elementoPila.noTerminal("E")
                        estado = elementoPila.estado(str(valorE))

                        self.pila.push(noTerminal)
                        self.pila.push(estado)

                elif valor == 0:

                    print("Entrada No Valida")
                    break

            else:

                valor = tabla_2[2][int(self.pila.top().returnValor())]   

                if valor > 0:

                    print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))

                    terminal = elementoPila.terminal(entradaDividida[cont])
                    estado = elementoPila.estado(str(valor))

                    self.pila.push(terminal)
                    self.pila.push(estado)
                    
                    cont+=1

                elif valor < 0:

                    if valor == -1:

                        print("Entrada: "+entrada+ " Aceptada")
                        valida = True
                        
                    #Regla 2
                    elif valor == -3:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        for i in range(2):
                            self.pila.pop()

                        #Toma el valor de la primera regla
                        valorE = tabla_2[3][int(self.pila.top().returnValor())]

                        noTerminal = elementoPila.noTerminal("E")
                        estado = elementoPila.estado(str(valorE))

                        self.pila.push(noTerminal)
                        self.pila.push(estado)
                            
                    #Regla 1
                    elif valor == -2:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        for i in range(6):
                            self.pila.pop()

                        #Toma el valor de la segunda regla
                        valorE = tabla_2[3][int(self.pila.top().returnValor())]

                        noTerminal = elementoPila.noTerminal("E")
                        estado = elementoPila.estado(str(valorE))

                        self.pila.push(noTerminal)
                        self.pila.push(estado)
                elif valor == 0:

                    print("Entrada No Valida")
                    break
                
    def readFile(self):

        #Abre el archivo el modo lectura
        file = open("compilador.lr","r")
        #Guarda todos los datos en un string
        fullString = file.readlines()

        #CARGA LA PRIMERA LINEA QUE ES VACIA
        self.gramatica.append("52")
        self.popElements.append("0")
        self.nombreRegla.append(" ")


        #Comienza a cargar los datos
        for i in range(1,54):

            #Guarda la linea
            line = fullString[i]
            line = line[:-1].split("\t")

            if i != 53:

                #Guarda la regla gramatical
                self.gramatica.append(line[0])
                #Guarda los elementos que genera la regla
                self.popElements.append(line[1])
                #Guarda el nombre de la regla
                self.nombreRegla.append(line[2])

            elif i == 53:

                #Guarda la regla gramatical
                self.gramatica.append(line[0])
                #Guarda los elementos que genera la regla
                self.popElements.append(line[1])
                #Al no tener un nombre de regla, se agrega un espacio vacio
                self.nombreRegla.append(" ")


        for i in range(54,148):

            #Guarda la linea actual
            line = fullString[i]
            #Genera una lista con los elementos
            line = line[:-1].split("\t")

            #Guarda la lista dentro de la matriz
            self.matrizGramatica.append(line)

        file.close()


    def compliador(self,e):

        #Carga la gramatica del compilador
        self.readFile()
        
        self.pila.limpiar()

        lexico = analizador(e)
            
        e = e + " $"
        entradaDividida = e.split(" ")

        #Se crea el primer elementoPila
        primerNT = elementoPila.noTerminal("$","$",2)
        #Segundo elementoPila
        primerEstado = elementoPila.estado("0","",3)
        #Push a los elementos creados
        self.pila.push(primerNT)
        self.pila.push(primerEstado)

        valida = False
        cont = 0
        valorTabla = ""

        while valida == False:

            #Devuelve el tipo de token y su valor en tabla
            (tipo,valor) = lexico.returnTipo(lexico.evaluaElemento(entradaDividida[cont]))

            #COMPARA TOPE DE LA PILA CON EL VALOR DEL TOKEN Y GUARDA EL VALOR DE LA TABLA
            topePila = int(self.pila.top().returnValor())
            valorTabla = int(self.matrizGramatica[topePila][valor])
                
            if valorTabla == 0:

                print("Entrada no valida")
                break

            elif valorTabla > 0:

                terminal = elementoPila.terminal(entradaDividida[cont],"",1)
                estado = elementoPila.estado(str(valorTabla),"",3)

                self.pila.push(terminal)
                self.pila.push(estado)

                #print("Token: "+entradaDividida[cont]+" Accion: "+str(valorTabla))
                #self.pila.printStack()
                cont+=1

            elif valorTabla < 0:

                if valorTabla == -1:

                    print("Entrada Aceptada!")
                    valida = True
                    '''COMIENZA A IMPRIMIR EL ARBOL'''
                    arbolFinal = arbolSintactico.arbolSintactico()
                    analizadorSem = semantico.Semantico()
                    '''Hace pop al ultimo elemento que es un estado'''
                    self.pila.pop()
                    elemento = self.pila.pop()
                    '''Imprime la regla del Nodo'''
                    print(f"Entrada: {lexico.entrada}\n")
                    elemento.nodo.printRegla()
                    #arbolFinal.imprimirArbol(elemento.nodo)
                    analizadorSem.analiza(elemento.nodo)
                    analizadorSem.muestraSimbolos()
                    analizadorSem.muestraErrores()
                    break
                
                '''CREA EL NODO'''
                nodo = arbolSintactico.Nodo()

                valorTabla+=1
                numeroEliminar = int(self.popElements[abs(valorTabla)])
                '''Obtiene el nombre de la regla'''
                nomRegla = self.nombreRegla[abs(valorTabla)]
                '''EL NODO GUARDA EL NOMBRE DE LA REGLA'''
                nodo.regla = nomRegla

                if numeroEliminar > 0:

                    for i in range(int(numeroEliminar)*2):

                        elemento = self.pila.pop()
                        '''EL NODO SOLO GUARDA EL ELEMENTO IMPORTANTE'''
                        if i%2 == 1:

                            nodo.elementosEliminados.append(elemento)
                    
                #Compara tope de la pila con la regla
                topePila = int(self.pila.top().returnValor())
                regla = int(self.gramatica[abs(valorTabla)])
                valorTabla = self.matrizGramatica[topePila][regla]

                '''El noTerminal guarda el numero de la regla, el nombre, su ID y el nodo'''
                noTerminal = elementoPila.noTerminal(nomRegla,nomRegla,2)
                noTerminal.nodo = nodo
                estado = elementoPila.estado(str(valorTabla),"",3)

                #Hace push en la pila
                self.pila.push(noTerminal)
                self.pila.push(estado)

                #print("Token: "+entradaDividida[cont]+" Accion: "+str(valorTabla))
                #self.pila.printStack()
                
              
