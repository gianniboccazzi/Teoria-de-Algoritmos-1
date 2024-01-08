def verificador_hitting_set(A, C, subconjuntos, k):
    subconjuntos_intersecados = []
    if len(C) > k or len(C) == 0:
        return False
    for jugador in C:
        if jugador not in A:
            return False
        if len(subconjuntos_intersecados) == len(subconjuntos):
            continue
        for subconjunto in subconjuntos:
            if jugador in subconjunto and subconjunto not in subconjuntos_intersecados:
                subconjuntos_intersecados.append(subconjunto)
    return len(subconjuntos_intersecados) == len(subconjuntos)

