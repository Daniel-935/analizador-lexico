import xlrd
from io import open
import elementoPila
from lexico import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

analizador.compliador("int a ; int suma ( int a , int b ) { return a + b ; } int main ( ) { float a ; int b ; int c ; c = a + b ; c = suma ( 8 , 9 ) ; }")
#MASM
#int main ( int b , int a ) { return a + b ; }
