from analizador import analizador
from stack import stack

class sintactico:

    def __init__(self):
        
        self.pila = stack()

    def ejercicio_1(self, entrada):

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
