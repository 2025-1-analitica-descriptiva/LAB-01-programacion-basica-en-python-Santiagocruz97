"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_09(ruta):
    asociaciones = {}
    with open(ruta, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            elementos = row[4].split(",")
            for elemento in elementos:
                clave, valor = elemento.split(":")
                if clave in asociaciones:
                   asociaciones[clave]+=1
                else:
                   asociaciones[clave] = 1
    resultado = dict(sorted(asociaciones.items()))    
    return resultado

ruta = r"files/input/data.csv"
list_tuple = pregunta_09(ruta)
print(list_tuple)  



"""
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
