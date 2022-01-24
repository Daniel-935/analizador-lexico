
import re


class analizador:

    def __init__(self, e):
        
        self.entrada = str(e)
        #Separa la entrada por espacios en una lista
        self.splitEntrada = self.entrada.split(" ")

    def printCase(self, num):

        if(num==0):

            return "Identificador"
        elif(num==1):

            return "Entero"
        elif(num==2):

            return "Real"
        elif(num==3):

            return "Cadena"
        elif(num==5):

            return "OpSuma"
        elif(num==6):

            return "OpMul"
        elif(num==7):

            return "OpRelac"
        elif(num==8):

            return "OpOR"
        elif(num==9):

            return "OpAND"
        elif(num==10):

            return "OpNOT"
        elif(num==11):

            return "OpIgualdad"
        elif(num==12):

            return ";"
        elif(num==13):

            return ","
        elif(num==14):

            return "("
        elif(num==15):

            return ")"
        elif(num==16):

            return "{"
        elif(num==17):

            return "}"
        elif(num==18):

            return "="
        elif(num==19):

            return "Palabra Reservada 'if'"
        elif(num==20):

            return "Palabra Reservada 'while'"
        elif(num==21):

            return "Palabra Reservada 'return'"
        elif(num==22):

            return "Palabra Reservdada 'else'"

        elif(num==23):

            return "$"
        elif(num==24):

            return "Palabra Reservada 'int'"
        elif(num==25):

            return "Palabra Reservada 'float'"
        elif(num==26):

            return "Palabra Reservada 'void'"

    def isString(self, e):

        number = False
        letter = False

        for i in e:

            if(i.isnumeric()):

                number = True
            else:

                letter = True
        
        if(number == letter):

            return False
        
        return True
        

    def returnCase(self, entrada):

        if(self.isString(entrada)==False):

            return 0
        elif(entrada.isnumeric()):

            return 1
        elif(entrada.find(".")!=-1):

            return 2
        elif(entrada == "+" or entrada=="-"):

            return 5
        elif(entrada=="*" or entrada=="/"):

            return 6
        elif(entrada=="<" or entrada==">" or entrada=="<=" or entrada==">="):

            return 7
        elif(entrada=="||"):

            return 8
        elif(entrada=="&&"):

            return 9
        elif(entrada=="!"):

            return 10
        elif(entrada=="==" or entrada=="!="):

            return 11
        elif(entrada==";"):

            return 12
        elif(entrada==","):

            return 13
        elif(entrada=="("):

            return 14
        elif(entrada==")"):

            return 15
        elif(entrada=="{"):

            return 16
        elif(entrada=="}"):

            return 17
        elif(entrada=="="):

            return 18
        elif(entrada=="if"):

            return 19
        elif(entrada=="while"):

            return 20
        elif(entrada=="return"):

            return 21
        elif(entrada=="else"):

            return 22
        elif(entrada=="$"):

            return 23
        elif(entrada=="int"):

            return 24
        elif(entrada=="float"):

            return 25
        elif(entrada=="void"):

            return 26
        else:

            return 3

    def iniciarAnalizador(self):
   
        for i in self.splitEntrada:

            print(i + "   " + self.printCase(self.returnCase(i))) 
    