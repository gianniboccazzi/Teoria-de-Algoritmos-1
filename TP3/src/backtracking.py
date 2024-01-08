import time

def hitting_set_problem_BT(A, subconjuntos):
    time_start = time.time()
    set_subconjuntos = get_set_subconjuntos(subconjuntos)
    solucion_minima, solucion_parcial, actual  = [], [], 0
    hitting_set_problem_BT_rec(A,subconjuntos, actual, solucion_minima, solucion_parcial, set_subconjuntos)
    time_end = time.time()
    return solucion_minima, time_end - time_start

def hitting_set_problem_BT_rec(A, subconjuntos, actual, solucion_minima, solucion_parcial, set_subconjuntos):
    if actual == len(A) or (len(solucion_parcial) >= len(solucion_minima) and len(solucion_minima) != 0):
        return 
    if A[actual] in set_subconjuntos:
        solucion_parcial.append(A[actual])
        if cubre_todos_los_subconjuntos(solucion_parcial, subconjuntos):
            if len(solucion_minima) == 0 or len(solucion_parcial) < len(solucion_minima):
                solucion_minima[:] = solucion_parcial[:]
                solucion_parcial.pop()
                return
        hitting_set_problem_BT_rec(A, subconjuntos, actual+1, solucion_minima, solucion_parcial, set_subconjuntos)
        solucion_parcial.pop()
    hitting_set_problem_BT_rec(A, subconjuntos, actual+1, solucion_minima, solucion_parcial, set_subconjuntos)


def get_set_subconjuntos(subconjuntos:list):
    set_subconjuntos = set()
    for subconjunto in subconjuntos:
        set_subconjuntos.update(subconjunto)
    return set_subconjuntos

def cubre_todos_los_subconjuntos(C, subconjuntos):
    for subconjunto in subconjuntos:
        if not subconjunto.intersection(C):
            return False
    return True