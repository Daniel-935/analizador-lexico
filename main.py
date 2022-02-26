import xlrd
from analizador import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

"""print("Primer Ejercicio: ")
analizador.ejercicio_1("hola + mundo")
print("\nSegundo Ejercicio: ")
analizador.ejercicio_2("a + b + c + d + e + f")"""

loc = ("Prueba.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

"""print(sheet.cell_value(0,0))
print(sheet.cell_value(1,0))
print(type(sheet.cell_value(0,0)))
print(type(sheet.cell_value(1,0)))
print(int(sheet.cell_value(2,0)))
print(type(sheet.cell_value(2,0)))"""

if sheet.cell_value(2,1) == "":

    print("Esta vacio")

else:

    print("No esta vacio")
    print(sheet.cell_value(2,1))

