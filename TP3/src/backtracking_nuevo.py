import time


def hitting_set_problem_BT_mejorado(A, subconjuntos):
    time_start = time.time()
    subconjuntos.sort(key=lambda x: len(x))
    solucion_minima = hitting_set_problem_BT_rec(subconjuntos, 0, set(), set())
    time_end = time.time()
    return solucion_minima, time_end - time_start

def hitting_set_problem_BT_rec(subconjuntos, actual, solucion_minima, solucion_parcial):
    if actual >= len(subconjuntos) or (len(solucion_parcial) >= len(solucion_minima) and len(solucion_minima) != 0):
        return solucion_minima
    for jugador in subconjuntos[actual]:
        if jugador in solucion_parcial or not hittea_nuevo_set(jugador, actual, subconjuntos):
            continue
        solucion_parcial.add(jugador)
        if cubre_todos_los_subconjuntos(solucion_parcial, subconjuntos):
            if len(solucion_minima) == 0 or len(solucion_parcial) < len(solucion_minima):
                solucion_minima = solucion_parcial.copy()
                solucion_parcial.remove(jugador)
                return solucion_minima
        subconjuntos_restantes = obtener_subconjuntos_restantes(jugador, actual, subconjuntos)
        solucion_minima = hitting_set_problem_BT_rec(subconjuntos_restantes, actual, solucion_minima, solucion_parcial)
        solucion_parcial.remove(jugador)
    return solucion_minima

def cubre_todos_los_subconjuntos(C, subconjuntos):
    for subconjunto in subconjuntos:
        if not subconjunto.intersection(C):
            return False
    return True
    
def hittea_nuevo_set(jugador, actual, subconjuntos):
    for i in range(actual, len(subconjuntos)):
        if jugador in subconjuntos[i]:
            return True
    return False

def obtener_subconjuntos_restantes(jugador, actual, subconjuntos):
    subconjuntos_restantes = subconjuntos.copy()
    for i in range(len(subconjuntos)-1, actual-1, -1):
        if jugador in subconjuntos_restantes[i]:
            subconjuntos_restantes.pop(i)
    return subconjuntos_restantes
