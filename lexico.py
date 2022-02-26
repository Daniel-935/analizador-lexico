
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

        elif estado == 6:

            return "-"

        elif estado == 7:

            return "*"
        elif estado == 8:

            return "/"
        elif estado == 9:

            return "OP. RELACIONAL"
        elif estado == 10:

            return "||"
        elif estado == 11:

            return "&&"
        elif estado == 12:

            return "!"
        elif estado == 13:

            return "OP. IGUALDAD"
        elif estado == 14:

            return ";"
        elif estado == 15:

            return "("
        elif estado == 16:

            return ")"
        elif estado == 17:

            return "{"
        elif estado == 18:

            return "}"
        elif estado == 19:

            return "="
        elif estado == 20:

            return "if"
        elif estado == 21:

            return "while"
        elif estado == 22:

            return "return"
        elif estado == 23:

            return "else"
        elif estado == 24:

            return "int"
        elif estado == 25:

            return "float"
        elif estado == 26:

            return "$"
        elif estado == 27:

            return "CADENA"

    def evaluaElemento(self, cadena):

        estado = 0

        #PALABRAS RESERVADAS

        if cadena == "if" and estado==0:

            estado = 20
        elif cadena == "while" and estado==0:

            estado = 21
        elif cadena == "return" and estado==0:

                estado = 22
        elif cadena == "else" and estado==0:

            estado = 23
        elif cadena == "int" and estado==0:

            estado = 24
        elif cadena == "float" and estado==0:

            estado = 25
        elif cadena == "==" and estado==0:

            estado = 13

        else:
            
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

                #Reconoce simbolos aritmeticos
                elif i == "+" and estado==0:

                    estado = 5

                elif i == "-" and estado==0:

                    estado = 6

                elif i == "*" and estado==0:

                    estado = 7

                elif i == "/" and estado==0:

                    estado = 8
                #Operadores Relacionales
                elif (i == "<" or i == ">") and estado==0:

                    estado = 9
                elif i == "=" and estado == 9:

                    estado = 9
                elif i == "|" and estado==0:

                    estado = 10
                elif i == "&" and estado==0:

                    estado = 11
                elif i == "!" and estado==0:

                    estado = 12
                elif i == "=" and estado==12:

                    estado = 12
                elif i == ";" and estado==0:

                    estado = 14
                elif i == "(" and estado==0:

                    estado = 15
                elif i == ")" and estado==0:

                    estado = 16
                elif i == "{" and estado==0:

                    estado = 17
                elif i == "}" and estado==0:

                    estado = 18
                elif i == "}" and estado==0:

                    estado = 18
                elif i == "=" and estado==0:

                    estado = 19
                elif i == "$" and estado==0:

                    estado = 26
                elif (i == '"' or i == "'") and estado == 0:

                    estado = 27
                elif (i.isnumeric()==False or i == '"' or i == "'") and estado == 27:

                    estado = 27
                    
                #Si empieza con letra y esta en el estado 0 es IDENTIFICADOR
                elif i.isnumeric()==False and estado==0:

                    estado = 4

        return estado

    def iniciarAnalizador(self):
   
        for i in self.splitEntrada:

            print(i + "\t" + self.returnTipo(self.evaluaElemento(i)))    
