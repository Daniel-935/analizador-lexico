from lexico import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

print("Primer Ejercicio: ")
analizador.ejercicio_1("hola + mundo")
print("\nSegundo Ejercicio: ")
analizador.ejercicio_2("a + b + c + d + e + f")