import xlrd
from io import open
from lexico import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

file = open("file.txt","r")
fullString = file.readlines()

for i in fullString:

    print(i)

"""loc = ("Prueba.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)"""

