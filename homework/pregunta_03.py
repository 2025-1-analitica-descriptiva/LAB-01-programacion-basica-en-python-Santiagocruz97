"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
def pregunta_03(ruta)->tuple:
    a=0
    b=0
    c=0
    d=0
    e=0
    with open(ruta, "r", encoding="utf-8") as file:
        reader=csv.reader(file, delimiter="\t")
        for row in reader:
            if row[0]=="A":
                a+=int(row[1])
            elif row[0]=="B":
                b+=int(row[1])
            elif row[0]=="C":
                c+=int(row[1])
            elif row[0]=="D":
                d+=int(row[1])
            else:
                e+=int(row[1])
        variablea="A"
        variableb="B"
        variablec="C"
        variabled="D"
        variablee="E"
        lista=[(variablea,a),(variableb,b),(variablec,c),(variabled,d),(variablee,e)]
    return lista
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
ruta = r"files/input/data.csv"
list_tuple = pregunta_03(ruta)
print(list_tuple)