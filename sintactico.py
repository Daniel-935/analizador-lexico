from analizador import analizador
from stack import stack
from elementoPila import elementoPila

class sintactico:

    def __init__(self):
        
        self.pila = stack()

    def ejercicio_1(self, entrada):

        self.pila.limpiar()
        #El analizador guarda la entrada
        lexico = analizador(entrada)
        #Divide la entrada por espacios
        entrada = entrada + " $"
        entradaDividida = entrada.split(" ")

        #Tabla LR para el primer ejercicio
        tabla_1 = [[2,0,0,4,0],[0,0,3,0,0],[0,-1,0,0,-2],[1,0,0,0,0]]

        self.pila.push("$")
        self.pila.push("0")

        valor = 0
        valida = False
        cont = 0
        
        while valida==False:

            if entradaDividida[cont] != "$":

                type = lexico.returnTipo(lexico.evaluaElemento(entradaDividida[cont]))

                if type == "Identificador": 

                    #Toma el valor de la tabla
                    valor = tabla_1[0][int(self.pila.top())]

                    #Si es 0 es un error
                    if valor == 0:

                        break

                    else:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        self.pila.push(entradaDividida[cont])
                        self.pila.push(str(valor))

                elif type == "+":

                    valor = tabla_1[1][int(self.pila.top())]

                    if valor == 0:

                        break

                    else:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        self.pila.push(entradaDividida[cont])
                        self.pila.push(str(valor))

                cont=cont+1
            
            if entradaDividida[cont] == "$":

                valor = tabla_1[2][int(self.pila.top())]

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
                    self.pila.push("E")
                    self.pila.push(str(abs(valor+1)))

    def ejercicio_2(self,entrada):

        self.pila.limpiar()
        tabla_2 = [[2,0,0,2,0],[0,0,3,0,0],[0,-1,-3,0,-2],[1,0,0,4,0]]

        #El analizador guarda la entrada
        lexico = analizador(entrada)
        #Divide la entrada por espacios
        entrada = entrada + " $"
        entradaDividida = entrada.split(" ")

        self.pila.push("$")
        self.pila.push("0")

        valor = 0
        valida = False
        cont = 0

        while valida == False:

            type = lexico.returnTipo(lexico.evaluaElemento(entradaDividida[cont]))

            if type != "$":

                if type == "Identificador":

                    #Toma el valor de la tabla
                    valor = tabla_2[0][int(self.pila.top())]

                elif type == "+":

                    valor = tabla_2[1][int(self.pila.top())]

                #Verifica si hace reduccion o apila

                if valor > 0:

                    print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                    self.pila.push(entradaDividida[cont])
                    self.pila.push(str(valor))
                    
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
                        valorE = tabla_2[3][int(self.pila.top())]

                        self.pila.push("E")
                        self.pila.push(str(valorE))
                            
                    #Regla 1
                    elif valor == -2:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        for i in range(6):
                            self.pila.pop()

                        #Toma el valor de la segunda regla
                        valorE = tabla_2[3][int(self.pila.top())]

                        self.pila.push("E")
                        self.pila.push(str(valorE))

                elif valor == 0:

                    print("Entrada No Valida")
                    break

            else:

                valor = tabla_2[2][int(self.pila.top())]   

                if valor > 0:

                    print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                    self.pila.push(entradaDividida[cont])
                    self.pila.push(str(valor))
                    
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
                        valorE = tabla_2[3][int(self.pila.top())]

                        self.pila.push("E")
                        self.pila.push(str(valorE))
                            
                    #Regla 1
                    elif valor == -2:

                        print("Entrada: "+entradaDividida[cont]+"  Accion: "+str(valor))
                        for i in range(6):
                            self.pila.pop()

                        #Toma el valor de la segunda regla
                        valorE = tabla_2[3][int(self.pila.top())]

                        self.pila.push("E")
                        self.pila.push(str(valorE))
                elif valor == 0:

                    print("Entrada No Valida")
                    break
                

