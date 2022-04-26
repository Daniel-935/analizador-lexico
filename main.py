import xlrd
from io import open
import elementoPila
from lexico import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

analizador.compliador("int main ( ) { int a ; }")