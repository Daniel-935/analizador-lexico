
class analizador:

    def __init__(self, e):
        
        self.entrada = str(e)
        #Separa la entrada por espacios en una lista
        self.splitEntrada = self.entrada.split(" ")
        #Declara el estado inicial en 0
        self.estado = 0

    def returnTipo(self):

        if self.estado == 0:

            return "Error"

        elif self.estado == 1:

            return "Entero"

        elif self.estado == 2:

            return "Error"

        elif self.estado == 3:

            return "Real"

        elif self.estado == 4:

            return "Identificador"

    def evaluaElemento(self, cadena):

        for i in cadena:

            #Se mantiene en estado 1 es ENTERO
            if i.isnumeric() and self.estado==0:

                self.estado = 1
            elif i.isnumeric() and self.estado==1:
                
                self.estado=1

            #Si tiene un punto y esta en el estado 1 pasa al segundo estado
            elif i == "." and self.estado==1:

                self.estado = 2

            #Si esta en el estado 2 y tiene numero es REAL
            elif self.estado==2 and i.isnumeric:

                    self.estado = 3
                
            #Si empieza con letra y esta en el estado 0 es IDENTIFICADOR
            elif i.isnumeric()==False and self.estado==0:

                    self.estado = 4

    def iniciarAnalizador(self):
   
        for i in self.splitEntrada:

            #Reinicia el automata
            self.estado=0

            self.evaluaElemento(i)

            print(i + "\t" + self.returnTipo())    
