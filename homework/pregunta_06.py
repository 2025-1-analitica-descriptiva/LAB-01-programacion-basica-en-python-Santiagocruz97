"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_06(ruta)->list:
    lista={}

    with open(ruta, "r", encoding="utf-8") as file:
        reader= csv.reader(file, delimiter= "\t")
        for row in reader:
            elementos = row[4].split(",")
            for elemento in elementos:
                clave, valor = elemento.split(":")
                valor = int(valor)
                if clave not in lista:
                    lista[clave]={"min":float("inf"),"max":float("-inf")}
                lista[clave]["min"]=min(lista[clave]["min"], valor)
                lista[clave]["max"]=max(lista[clave]["max"], valor)
    lista_tuplas=[(clave, datos["min"], datos["max"]) for clave, datos in sorted(lista.items())]
    return lista_tuplas

ruta = r"files/input/data.csv"
list_tuple = pregunta_06(ruta)
print(list_tuple)
"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
