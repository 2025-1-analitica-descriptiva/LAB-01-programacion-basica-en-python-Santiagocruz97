"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv

def pregunta_12(ruta):
    asociaciones = {}
    with open(ruta, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            # Columna 1 (letra)
            letra = row[0]
            
            # Columna 5 (valores separados por coma)
            valores = row[4].split(",")
            suma = sum(int(valor.split(":")[1]) for valor in valores)
            
            # Acumular la suma en el diccionario
            if letra in asociaciones:
                asociaciones[letra] += suma
            else:
                asociaciones[letra] = suma
    
    # Ordenar el diccionario por clave
    resultado = dict(sorted(asociaciones.items()))
    return resultado

# Prueba rápida
ruta = "files/input/data.csv"
print(pregunta_12(ruta))
"""
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
