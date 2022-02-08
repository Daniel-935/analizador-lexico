
class analizador:

    def __init__(self, e):
        
        self.entrada = str(e)
        #Separa la entrada por espacios en una lista
        self.splitEntrada = self.entrada.split(" ")
        #Declara el estado inicial en 0

    def returnTipo(self,estado):

        if estado == 0:

            return "Error"

        elif estado == 1:

            return "Entero"

        elif estado == 2:

            return "Error"

        elif estado == 3:

            return "Real"

        elif estado == 4:

            return "Identificador"

        elif estado == 5:

            return "+"

    def evaluaElemento(self, cadena):

        estado = 0

        for i in cadena:

            #Se mantiene en estado 1 es ENTERO
            if i.isnumeric() and estado==0:

                estado = 1
            elif i.isnumeric() and estado==1:
                
                estado=1

            #Si tiene un punto y esta en el estado 1 pasa al segundo estado
            elif i == "." and estado==1:

                estado = 2

            #Si esta en el estado 2 y tiene numero es REAL
            elif estado==2 and i.isnumeric:

                estado = 3

            #Reconoce el simbolo +
            elif i == "+" and estado==0:

                estado = 5
                
            #Si empieza con letra y esta en el estado 0 es IDENTIFICADOR
            elif i.isnumeric()==False and estado==0:

                estado = 4

        return estado

    def iniciarAnalizador(self):
   
        for i in self.splitEntrada:

            print(i + "\t" + self.returnTipo(self.evaluaElemento(i)))    
