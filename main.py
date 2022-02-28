import xlrd
from io import open
from lexico import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

analizador.compliador("int hola ;")
#analizador.readFile()