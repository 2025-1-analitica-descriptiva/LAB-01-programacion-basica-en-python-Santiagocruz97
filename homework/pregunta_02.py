"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_02(ruta)->tuple:
    a=0
    b=0
    c=0
    d=0
    e=0
    with open(ruta, "r", encoding="utf-8") as file:
        reader=csv.reader(file, delimiter="\t")
        for row in reader:
            if row[0]=="A":
                a+=1
            elif row[0]=="B":
                b+=1
            elif row[0]=="C":
                c+=1
            elif row[0]=="D":
                d+=1
            else:
                e+=1
        variablea="A"
        variableb="B"
        variablec="C"
        variabled="D"
        variablee="E"
        lista=[(variablea,a),(variableb,b),(variablec,c),(variabled,d),(variablee,e)]
    return lista
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """ 
ruta = r"files/input/data.csv"
list_tuple = pregunta_02(ruta)
print(list_tuple)
