def obtener_subconjuntos(path):
    subconjuntos = []
    A = []
    with open(path) as archivo:
        for subconjunto in archivo.readlines():
            subconjunto_separado = {elemento.strip() for elemento in subconjunto.split(",")}
            for elemento in subconjunto_separado:
                if elemento not in A:
                    A.append(elemento)
            subconjuntos.append(set(subconjunto_separado))
    return A, subconjuntos