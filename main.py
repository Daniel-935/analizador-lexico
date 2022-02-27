import xlrd
from io import open
from lexico import analizador
from stack import stack
from sintactico import sintactico

analizador = sintactico()

file = open("compilador.lr","r")
fullString = file.readlines()

firstLine = fullString[1]
firstLine = firstLine[:-1].split("\t")

print(firstLine)



