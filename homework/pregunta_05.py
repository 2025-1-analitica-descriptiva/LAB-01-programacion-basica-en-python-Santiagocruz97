"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
def pregunta_05(ruta)->tuple:
    amin=100
    bmin=100
    cmin=100
    dmin=100
    emin=100
    amax=0
    bmax=0
    cmax=0
    dmax=0
    emax=0
    with open(ruta, "r", encoding="utf-8") as file:
        reader=csv.reader(file, delimiter="\t")
        for row in reader:
            if row[0]=="A":
                if int(row[1])<=amin:
                    amin=int(row[1])
                if int(row[1])>=amax:
                    amax=int(row[1])
            elif row[0]=="B":
                if int(row[1])<=bmin:
                    bmin=int(row[1])
                if int(row[1])>=bmax:
                    bmax=int(row[1]) 
            elif row[0]=="C":
                if int(row[1])<=cmin:
                    cmin=int(row[1])
                if int(row[1])>=cmax:
                    cmax=int(row[1])
            elif row[0]=="D":
                if int(row[1])<=dmin:
                    dmin=int(row[1])
                if int(row[1])>=dmax:
                    dmax=int(row[1])
            else:
                if int(row[1])<=emin:
                    emin=int(row[1])
                if int(row[1])>=emax:
                    emax=int(row[1])
        variablea="A"
        variableb="B"
        variablec="C"
        variabled="D"
        variablee="E"
        lista=[(variablea,amax, amin),(variableb,bmax, bmin),(variablec,cmax, cmin),(variabled,dmax, dmin),(variablee,emax, emin)]
    return lista
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
ruta = r"files/input/data.csv"
list_tuple = pregunta_05(ruta)
print(list_tuple)