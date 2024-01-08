import os
from parser_1 import obtener_subconjuntos
from backtracking import hitting_set_problem_BT
from lineal import hitting_set_problem_pl
from lineal_aprox import hitting_set_problem_pl_relajado
from greedy import hitting_set_problem_greedy
from backtracking_nuevo import hitting_set_problem_BT_mejorado

SEP = "------------------------------------------------------------"
MESSAGE = "Indique el nombre del archivo de entrada, de la carpeta ejemplos (o q para salir): "
MESSAGE_ALGORITHM = "Indique el algoritmo a utilizar: \n 1. Backtracking \n 2. Backtracking reformulado \n 3. Programación lineal \n 4. Aproximación por programación lineal \n 5. Aproximación Greedy \n 6. Todos \n"
RETRY = "Respuesta invalida, intenta nuevamente"
SOLUCION_BACKTRACKING = "Solución por Backtracking: "
SOLUCION_BACKTRACKING_MEJORADO = "Solución por Backtracking mejorado: "
SOLUCION_PROGRAMACION_LINEAL = "Solución por Programación Lineal: "
SOLUCION_APROXIMACION_PROGRAMACION_LINEAL = "Solución por Aproximación por Programación Lineal: "
SOLUCION_APROXIMACION_GREEDY = "Solución por Aproximación Greedy: "
TIEMPO_EJECUCION = "Tiempo de ejecución: "
script_dir = os.path.dirname(__file__)
DIRECTORIO = script_dir + '/ejemplos'

def imprimir_todos(A, subconjuntos):
    res, tiempo = hitting_set_problem_BT(A, subconjuntos)
    print(f"{SOLUCION_BACKTRACKING}{res}")
    print(f"{TIEMPO_EJECUCION}{tiempo}")
    print(SEP)
    res, tiempo = hitting_set_problem_BT_mejorado(A, subconjuntos)
    print(f"{SOLUCION_BACKTRACKING_MEJORADO}{res}")
    print(f"{TIEMPO_EJECUCION}{tiempo}")
    print(SEP)
    res, tiempo = hitting_set_problem_pl(A, subconjuntos)
    print(f"{SOLUCION_PROGRAMACION_LINEAL}{res}")
    print(f"{TIEMPO_EJECUCION}{tiempo}")
    print(SEP)
    res, tiempo = hitting_set_problem_pl_relajado(A, subconjuntos)
    print(f"{SOLUCION_APROXIMACION_PROGRAMACION_LINEAL}{res}")
    print(f"{TIEMPO_EJECUCION}{tiempo}")
    print(SEP)
    res, tiempo = hitting_set_problem_greedy(A, subconjuntos)
    print(f"{SOLUCION_APROXIMACION_GREEDY}{res}")
    print(f"{TIEMPO_EJECUCION}{tiempo}")
        



def main():
    print(SEP)
    print(MESSAGE)
    path = ""
    while path != "q" and not os.path.isfile(path):
        path = input()
        if path == "q":
            return 0
        path = os.path.join(DIRECTORIO, path)
        if not os.path.isfile(path):
            print("El archivo no existe, intenta nuevamente")
    A, subconjuntos = obtener_subconjuntos(path)
    print(SEP)
    print(MESSAGE_ALGORITHM)
    respuesta = 0
    while respuesta not in [1, 2 , 3, 4, 5, 6]:
        respuesta = int(input())
        if respuesta not in [1, 2 , 3, 4, 5, 6]:
            print(RETRY)
    if respuesta == 1:
        res, tiempo = hitting_set_problem_BT(A, subconjuntos)
        print(f"{SOLUCION_BACKTRACKING}{res}")
        print(f"{TIEMPO_EJECUCION}{tiempo}")
    elif respuesta == 2:
        res, tiempo = hitting_set_problem_BT_mejorado(A, subconjuntos)
        print(f"{SOLUCION_BACKTRACKING_MEJORADO}{res}")
        print(f"{TIEMPO_EJECUCION}{tiempo}")
    elif respuesta == 3:
        res, tiempo = hitting_set_problem_pl(A, subconjuntos)
        print(f"{SOLUCION_PROGRAMACION_LINEAL}{res}")
        print(f"{TIEMPO_EJECUCION}{tiempo}")
    elif respuesta == 4:
        res, tiempo = hitting_set_problem_pl_relajado(A, subconjuntos)
        print(f"{SOLUCION_APROXIMACION_PROGRAMACION_LINEAL}{res}")
        print(f"{TIEMPO_EJECUCION}{tiempo}")
    elif respuesta == 5:
        res, tiempo = hitting_set_problem_greedy(A, subconjuntos)
        print(f"{SOLUCION_APROXIMACION_GREEDY}{res}")
        print(f"{TIEMPO_EJECUCION}{tiempo}")
    elif respuesta == 6:
        imprimir_todos(A, subconjuntos)


if __name__ == "__main__":
   main()


