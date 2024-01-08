import time


def hitting_set_problem_greedy(A, subconjuntos):
    time_start = time.time()
    solucion = set()
    subconjuntos_intersecados = []
    subconjuntos_copia = subconjuntos[:]
    while len(subconjuntos_intersecados) < len(subconjuntos):
        diccionario_cantidad_apariciones = cantidad_apariciones(A, subconjuntos_copia)
        jugador = max(diccionario_cantidad_apariciones, key=diccionario_cantidad_apariciones.get)
        solucion.add(jugador)
        for subconjunto in subconjuntos_copia:
            if jugador in subconjunto:
                subconjuntos_intersecados.append(subconjunto)
        subconjuntos_copia = [s for s in subconjuntos_copia if s not in subconjuntos_intersecados]
    time_end = time.time()
    return solucion, time_end - time_start


def cantidad_apariciones(A, subconjuntos):
    diccionario_cantidad_apariciones = {}
    for jugador in A:
        for subconjunto in subconjuntos:
            if jugador in subconjunto:
                diccionario_cantidad_apariciones[jugador] = diccionario_cantidad_apariciones.get(jugador, 0) + 1
    return diccionario_cantidad_apariciones
