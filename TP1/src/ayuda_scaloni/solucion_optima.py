from enum import Enum
import time
import os

Opcion = Enum('Opcion', ['Tiempos', 'Soluciones', 'Ambas'])
script_dir = os.path.dirname(__file__)
rel_path = "/../utils/ejemplos/"
FILES = ["3_elementos.txt", "10_elementos.txt", "100_elementos.txt", "1000_elementos.txt"]
FILE_PATHS = list(map(lambda x: script_dir + rel_path + x, FILES))

PROGRESS = "####"

def comparar_tiempos(opcion):
    result = []
    start = 0
    for filename in FILE_PATHS:
        print(PROGRESS * (start + 1))
        start += 1
        result.append(ayuda_scaloni(leer_archivo(filename)))
    print()
    if(opcion == Opcion.Soluciones.value or opcion == Opcion.Ambas.value):
        print("Soluciones para ejemplos de 3, 10, 100 y 1000 elementos:")
        for e in result:
            print(e[0])
        print()
    if (opcion == Opcion.Tiempos.value or opcion == Opcion.Ambas.value):
        print("Tiempos de ejecucion para corridas con 3, 10, 100 y 1000 elementos:")
        for e in result:
            print(e[1])
        print()

def leer_archivo(ruta):
    res = []
    with open(ruta) as archivo:
        archivo.readline()
        for linea in archivo.readlines():            
            tupla = tuple(int(elemento) for elemento in linea.split(","))
            res.append(tupla)
    return res

def ayuda_scaloni(arreglo):
    inicio = time.time_ns()
    tiempo_scaloni= 0
    tiempo_total = 0
    arreglo_ordenado = sorted(arreglo, key=lambda x: x[1], reverse=True)
    for analisis in arreglo_ordenado:
        tiempo_scaloni += analisis[0]
        tiempo_ayudante = tiempo_scaloni + analisis[1]
        if tiempo_ayudante > tiempo_total:
            tiempo_total = tiempo_ayudante
    fin = time.time_ns()
    return (tiempo_total, fin - inicio)
