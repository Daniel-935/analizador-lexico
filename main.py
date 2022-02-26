import xlrd
from lexico import analizador
from stack import stack
from sintactico import sintactico

#analizador = sintactico()
anLexico = analizador("'cadena'")

anLexico.iniciarAnalizador()

"""loc = ("Prueba.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)"""

