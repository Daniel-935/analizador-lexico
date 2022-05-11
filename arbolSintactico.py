
class arbolSintactico:

    def __init__(self):

        self.sangriaActual = 0
    
    def imprimirArbol(self, nodo):
        
        '''Recorre los elementos que elimino el no terminal'''
        for i in reversed(nodo.elementosEliminados):

            '''Si un elemento es un no terminal imprime la regla que elimino'''
            if i.id == 2:

                i.nodo.sangria = self.sangriaActual
                i.nodo.printRegla()
            else:

                i.printValor()

        '''Obtiene el indice del no terminal que elimino mas elementos para continuar con el recorrido del arbol'''
        lastIndex = self.ultimoNodo(nodo)
        '''Si no encuentra un no terminal con mas hijos eliminados el recorrido termina'''
        if type(lastIndex) == int:

            nodoAux = nodo.elementosEliminados[lastIndex].nodo
            self.sangriaActual = self.sangriaActual + len(nodoAux.regla)-2

            self.imprimirArbol(nodoAux)

    def ultimoNodo(self,nodo):

        lastIndex = 0

        if len(nodo.elementosEliminados) > 0:

            for i in range(len(nodo.elementosEliminados)):

                nodoAux = nodo.elementosEliminados[i]
                if nodoAux.id == 2 and len(nodoAux.nodo.elementosEliminados) > 0:

                    lastIndex = i

            return lastIndex

        return False        

class Nodo:

    def __init__(self):

        self.sangria = 0
        self.elementosEliminados = []
        self.regla = ""


    def printRegla(self):

        sangriaAux = ""
        for i in range(self.sangria):

            sangriaAux += " "
        print(sangriaAux + self.regla + "\n")

    