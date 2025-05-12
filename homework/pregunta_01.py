import csv

def pregunta_01(ruta):
    suma_total = 0
    with open(ruta, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")  
        for row in reader:
            suma_total += int(row[1])
    return suma_total  
ruta = r"files/input/data.csv"
suma_total = pregunta_01(ruta)
print(suma_total)
