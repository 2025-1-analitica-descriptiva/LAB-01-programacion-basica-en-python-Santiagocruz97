"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_11(ruta):
    asociaciones = {}
    with open(ruta, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            # Valor de la columna 2 (entero)
            valor_col2 = int(row[1])
            
            # Letras de la columna 4
            letras_col4 = row[3].split(",")
            
            # Sumar los valores de la columna 2 para cada letra
            for letra in letras_col4:
                if letra in asociaciones:
                    asociaciones[letra] += valor_col2
                else:
                    asociaciones[letra] = valor_col2
    
    # Ordenar el diccionario por clave
    resultado = dict(sorted(asociaciones.items()))
    return resultado

ruta = "files/input/data.csv"
print(pregunta_11(ruta))


"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
