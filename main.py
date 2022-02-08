from cmath import pi
from analizador import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

analizador.ejercicio_1("hola + mundo")
