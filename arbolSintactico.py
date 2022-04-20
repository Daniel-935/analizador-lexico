from stack import stack

class arbolSintactico:

    def imprimirArbol(self, nodo):

        '''Recibe la pila con los elementos que elimino'''
        for i in reversed(nodo.elementosEliminados):

            '''Si en los elementos hay un noTerminal se imprime la regla'''
            if i.id == 2:

                i.printRegla()
                '''Despues se le pasa el nodo de ese noTerminal y entra en recursividad'''
                self.imprimirArbol(i.nodo)

class Nodo:

    def __init__(self):

        self.sangria = 0
        self.elementosEliminados = stack()
        self.regla = ""

    def printSangria(self):

        for i in range(self.sangria):

            print(" ")

    def printRegla(self):

        self.printSangria()
        print(self.regla)

    