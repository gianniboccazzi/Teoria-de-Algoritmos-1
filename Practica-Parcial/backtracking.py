from queue import Queue
from grafo import Grafo
import networkx as nx
#N Reinas
#Dado un tablero de ajedrez NxN, ubicar (si es posible) a N reinas de tal manera 
# que ninguna pueda comerse con ninguna. 

def n_reinas(n):
    tablero = [["_"] * n for _ in range(n)]
    res = _n_reinas(tablero,[], 0)
    return res


def _n_reinas(tablero,puestos, i):
    if len(puestos) == len(tablero):
        return puestos
    if i == len(tablero):
        return None
    for j in range(len(tablero)):
        if posicion_permitida(tablero, i, j):
            tablero[i][j] = "X"
            puestos.append((i, j))
            if _n_reinas(tablero, puestos, i+1):
                return puestos
            puestos.pop()
            tablero[i][j] = "_"
    return None

def posicion_permitida(tablero, i, j):
    if any(row[j] == "X" for row in tablero):
        return False
    if "X" in tablero[i]:
        return False
    k, l = i-1, j-1
    while k >= 0 and l >= 0:
        if tablero[k][l] == "X":
            return False
        k -= 1
        l -= 1
    k, l = i+1, j+1
    while k < len(tablero) and l < len(tablero):
        if tablero[k][l] == "X":
            return False
        k += 1
        l += 1
    k, l = i-1, j+1
    while k >= 0 and l < len(tablero):
        if tablero[k][l] == "X":
            return False
        k -= 1
        l += 1
    k, l = i+1, j-1
    while k < len(tablero) and l >= 0:
        if tablero[k][l] == "X":
            return False
        k += 1
        l -= 1
    return True


# print(n_reinas(20))






#Independent Set
# Quiero guardar en un grafo N elementos. Debo elegir N vértices en los cuales guardar cada 
# uno. Restricción! Queremos ver de ubicar N elementos sin que hayan dos adyacentes con elementos.

grafo = Grafo()
for i in range(8):
    grafo.agregar_vertice(i)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 5)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(5, 3)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(4, 5)
grafo.agregar_arista(5, 6)
grafo.agregar_arista(6, 7)
grafo.agregar_arista(4, 7)


def independent_set(grafo, n):
    vertices = grafo.obtener_vertices()
    return _independent_set(grafo,vertices, [], 0, n)


def _independent_set(grafo,vertices, solucion, i, n):
    if len(solucion) == n:
        return solucion
    if i == len(vertices) and i != 0:
        return None
    if es_compatible(grafo, solucion, vertices[i]):
        solucion.append(vertices[i])
        solucion_nueva = _independent_set(grafo,vertices, solucion, i+1, n)
        if solucion_nueva:
            return solucion_nueva
        solucion.pop()
    return _independent_set(grafo,vertices, solucion, i+1, n)
    

def es_compatible(grafo, solucion, v):
    for w in solucion:
        if v in grafo.adyacentes(w):
            return False
    return True

    
# print(independent_set(grafo, 4))

def max_independent_set(grafo):
    vertices = grafo.obtener_vertices()
    return _max_independent_set(grafo,vertices, [], [], 0)


def _max_independent_set(grafo, vertices, solucion_parcial, solucion_maxima, i):
    if i == len(vertices):
        if len(solucion_parcial) > len(solucion_maxima):
            return solucion_parcial.copy()
        return solucion_maxima.copy()
    if es_compatible(grafo, solucion_parcial, vertices[i]):
        solucion_parcial.append(vertices[i])
        solucion_nueva = _max_independent_set(grafo, vertices, solucion_parcial, solucion_maxima, i + 1)
        if len(solucion_nueva) > len(solucion_maxima):
            solucion_maxima = solucion_nueva
        solucion_parcial.pop()
    solucion_nueva = _max_independent_set(grafo, vertices, solucion_parcial, solucion_maxima, i + 1)
    if len(solucion_nueva) > len(solucion_maxima):
        return solucion_nueva

    return solucion_maxima


# print(max_independent_set(grafo))


def camino_hamiltoniano(grafo):
    for v in grafo.obtener_vertices():
        camino = []
        visitados = set()
        camino.append(v)
        visitados.add(v)
        if _camino_hamiltoniano(grafo, v, camino, visitados):
            return camino


def _camino_hamiltoniano(grafo, v, camino, visitados):
    if len(visitados) == len(grafo.obtener_vertices()):
        if len(camino) == len(grafo.obtener_vertices()):
            return True
        return False
    for w in grafo.adyacentes(v):
        if w in visitados:
            continue
        camino.append(w)
        visitados.add(w)
        if _camino_hamiltoniano(grafo, w, camino, visitados):
            return True
        camino.pop()
        visitados.remove(w)
    return False

# print(camino_hamiltoniano(grafo))







#k-coloreo
# Dado un grafo y K colores diferentes, ¿es posible pintar 
# los vértices de tal forma que ningún par de vértices adyacentes tengan el mismo color?


def crear_mapa():
    g = nx.Graph()
    g.add_nodes_from(["Argentina", "Brasil", "Uruguay", "Chile", "Perú", "Paraguay", "Bolivia", "Ecuador", "Venezuela",
                      "Colombia", "Surinam", "Guyana", "Guyana Francesa"])
    g.add_edges_from([("Argentina", "Uruguay"), ("Argentina", "Chile"), ("Argentina", "Bolivia"),
                      ("Argentina", "Brasil"), ("Argentina", "Paraguay"), ("Brasil", "Uruguay"), ("Brasil", "Paraguay"),
                      ("Brasil", "Bolivia"), ("Brasil", "Surinam"), ("Brasil", "Guyana Francesa"), ("Brasil", "Guyana"),
                      ("Brasil", "Venezuela"), ("Brasil", "Colombia"), ("Brasil", "Perú"), ("Chile", "Bolivia"),
                      ("Chile", "Perú"), ("Paraguay", "Bolivia"), ("Perú", "Bolivia"), ("Ecuador", "Perú"),
                      ("Ecuador", "Colombia"), ("Colombia", "Perú"), ("Colombia", "Venezuela"), ("Venezuela", "Guyana"),
                      ("Surinam", "Guyana"), ("Surinam", "Guyana Francesa")])
    return g


def es_compatible(grafo, colores, v):
    for w in grafo.neighbors(v):
        if w in colores and colores[w] == colores[v]:
            return False
    return True


def _coloreo_rec(grafo, k, colores, v):
    for color in range(k):
        colores[v] = color
        if not es_compatible(grafo, colores, v):
            continue
        correcto = True
        for w in grafo.neighbors(v):
            if w in colores:
                continue
            if not _coloreo_rec(grafo, k, colores, w):
                correcto = False
                break
        if correcto:
            return True
    del colores[v]
    return False


def coloreo(grafo, k):
    colores = {}
    if _coloreo_rec(grafo, k, colores, "Argentina"):
        print(colores)
        return True
    else:
        print(colores)
        return False

# print(coloreo(crear_mapa(), 4))






#sudoku
    
tablero = [[6, 0, 0, 0, 1, 0, 0, 9, 0],
           [0, 0, 0, 7, 0, 9, 2, 0, 0], 
           [0, 0, 7, 0, 0, 0, 8, 0, 0], 
           [0, 0, 2, 0, 7, 1, 0, 6, 0],
            [0, 0, 6, 0, 4, 0, 9, 0, 7],
            [0, 0, 1, 0, 5, 3, 0, 2, 0], 
            [0, 0, 9, 0, 0, 0, 3, 0, 0], 
            [0, 0, 0, 5, 0, 7, 1, 0, 0],
            [4, 0, 0, 0, 3, 0, 0, 7, 0]]


def sudoku(tablero):
    if _sudoku(tablero, 0, 0):
        print(tablero)
        return True
    return False

def _sudoku(tablero, i, j):
    i, j = find_empty(tablero)
    if i == None:
        return True

    for num in range(1, 10):
        if valid(tablero, num, (i, j)):
            tablero[i][j] = num
            if _sudoku(tablero, i, j):
                return True
            tablero[i][j] = 0
    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None, None

# print(sudoku(tablero))




#caballo

def caballo():
    tablero = [[-1] * 8 for _ in range(8)]
    tablero[0][0] = 0
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
    if _caballo(tablero, 0, 0, 1, move_x, move_y):
        print(tablero)
        return True
    return False


def _caballo(tablero, i, j, cant, move_x, move_y):
    if(cant == 8**2): 
        return True
    for k in range(8): 
        new_x = i + move_x[k] 
        new_y = j + move_y[k] 
        if es_permitido(new_x, new_y, tablero): 
            tablero[new_x][new_y] = cant 
            if _caballo(tablero, new_x, new_y,cant+1, move_x, move_y): 
                return True 
            tablero[new_x][new_y] = -1
    return False
    
                
  
def es_permitido(x, y, tablero): 
    if(x >= 0 and y >= 0 and x < len(tablero) and y < len(tablero) and tablero[x][y] == -1): 
        return True
    return False
  
# print(caballo())


# def isomorfismo(grafo1, grafo2):
#     res = {}
#     if _isomorfismo(grafo1, grafo2, res, 1, len(grafo1.obtener_vertices()), set()):
#         print(res)
#         return True
#     return False

#Queda pendiente por hacer


#QUEDA PENDIENTE EL DE HORARIOS TAMBIEN







#Sumatoria de n-dados
# Escribir un algoritmo de tipo Backtracking que reciba una cantidad de dados n y una suma s. 
# La función debe devolver todas las tiradas posibles de n dados cuya suma es s. 
# Por ejemplo, con n = 2 y s = 7, debe devolver [1, 6] [2, 5] [3, 4] [4, 3] [5, 2] [6, 1].


def suma_dados(n, s):
    soluciones = []
    for i in range(1, 7):
        solucion_parcial = [i]
        soluciones = _suma_dados(n,1,i,  s, solucion_parcial, soluciones)
    return soluciones


def _suma_dados(n, i, cont, s, solucion_parcial, soluciones):
    if i == n:
        if cont == s:
            soluciones.append(solucion_parcial[:])
        return soluciones
    for j in range(1, 7):
        if cont + j > s or s - cont > (n-i+1) * 6:
            return soluciones
        solucion_parcial.append(j)
        soluciones = _suma_dados(n, i+1, cont + j, s, solucion_parcial, soluciones)
        solucion_parcial.pop()
    return soluciones

# print(suma_dados(2, 7))











#SUBSET SUM
# Escribir una función que, utilizando backtracking, dada una lista de enteros positivos L y
# un entero n devuelva todos los subconjuntos de L que suman exactamente n.


def subset_sum(numeros, n):
    solucion = _subset_sum(numeros, 0, 0, n, [], [])
    return solucion



def _subset_sum(numeros, i, cont, n, solucion_parcial, soluciones):
    if i == len(numeros):
        return soluciones
    if numeros[i] + cont <= n:
        solucion_parcial.append(numeros[i])
        if numeros[i] + cont == n:
            soluciones.append(solucion_parcial[:])
            solucion_parcial.pop()
            return soluciones
        soluciones = _subset_sum(numeros, i+1, cont + numeros[i], n, solucion_parcial, soluciones)
        solucion_parcial.pop()
    soluciones = _subset_sum(numeros, i+1, cont, n, solucion_parcial, soluciones)
    return soluciones


# print(subset_sum([2, 9, 10, 1, 99, 3],15))


# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.



def bodegon_backtracking(P, W):
    solucion = []
    if _bodegon_backtracking(P, W, 0, solucion, 0):
        return solucion
    return False

def _bodegon_backtracking(P, W, i, solucion, cant_actual):
    if i == len(P):
        if cant_actual == W:
            return True
        return False
    if cant_actual + P[i] <= W:
        cant_actual += P[i]
        solucion.append(P[i])
        if _bodegon_backtracking(P, W, i+1, solucion, cant_actual):
            return True
        cant_actual-=P[i]
        solucion.pop()
    if _bodegon_backtracking(P, W, i+1, solucion, cant_actual):
        return True
    return False


# print(bodegon_backtracking([2, 9, 10, 1, 99, 3],15))
# print(subset_sum([2, 9, 10, 1, 99, 3],15))









# Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah 
# decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo
# color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar 
# todas las líneas de colectivos. Por problemas presupuestarios, sólo pueden pintar los colectivos
# de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren parecer 
# un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber
# si es posible cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal 
# forma que no hayan dos de mismo color coincidiendo en la misma parada). Considerando que se 
# tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el 
# problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
# el problema. Indicar la complejidad del algoritmo implementado.

def colectivos(grafo, k):
    colores = {}
    if _colectivos(grafo, k, colores, k):
        return colores
    return False



def _colectivos(grafo, v, colores, k):
    for i in range(k):
        colores[v] = i
        correcto = True
        if not es_compatible(grafo, colores, v):
            continue
        for w in grafo.adyacentes(v):
            if w in colores:
                continue
            if not _colectivos(grafo, w, colores, k):
                correcto = False
                break
            if correcto:
                return True
    del colores[v]
    return False
            




# Implementar un algoritmo que, por backtracking, obtenga todos los posibles ordenamientos 
# topológicos de un grafo
# dirigido y acíclico.


def ordenamientos_topologicos(grafo):
    grados = {}
    soluciones = []
    candidatos = []
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grados[w] = grados.get(w, 0) + 1
    for v in grafo.obtener_vertices():
        if not v in grados or grados[v] == 0:
           candidatos.append(v)
    for candidato in candidatos:
        soluciones = _ordenamientos_topologicos(grafo, candidato, grados, candidatos, [candidato], soluciones)
    return soluciones



def _ordenamientos_topologicos(grafo, v, grados,candidatos, solucion_actual, soluciones):
    if len(solucion_actual) == len(grafo.obtener_vertices()):
        soluciones.append(solucion_actual.copy())
        return soluciones
    cambios = set()
    for w in grafo.adyacentes(v):
        grados[w] -= 1
        if grados[w] == 0:
            candidatos.append(w)
        else:
            cambios.add(w)
    for candidato in candidatos: 
        if candidato in solucion_actual:
            continue       
        solucion_actual.append(candidato)
        soluciones = _ordenamientos_topologicos(grafo, candidato, grados,candidatos.copy(), solucion_actual, soluciones)
        solucion_actual.pop()
        if candidato not in grados:
            continue
        grados[candidato] += 1
    for v in cambios:
        grados[v] += 1
    return soluciones


        

# grafoo = Grafo(True)
# for i in range(1, 6):
#     grafoo.agregar_vertice(i)

# grafoo.agregar_arista(1, 2)
# grafoo.agregar_arista(1, 5)
# grafoo.agregar_arista(5, 2)
# grafoo.agregar_arista(2, 3)
# grafoo.agregar_arista(5, 4)
# grafoo.agregar_arista(4, 3)

# print(ordenamientos_topologicos(grafoo))






    
# Implementar un algoritmo que reciba un Grafo y un número k y devuelva un dominating set 
# de dicho grafo de a lo
# sumo k vértices (si existe).



def dominating_set(grafo, k):
    solucion = []
    if _dominating_set(grafo, grafo.obtener_vertices(), 0, k, solucion):
        return solucion
    return False


def _dominating_set(grafo, vertices, i,k,solucion):
    if es_dominating_set(solucion, grafo, vertices):
        return True
    if len(solucion) == k or i == len(vertices):
        return False
    solucion.append(vertices[i])
    if _dominating_set(grafo, vertices, i+1, k, solucion):
        return True
    solucion.pop()
    return _dominating_set(grafo, vertices, i+1, k, solucion)


def es_dominating_set(solucion, grafo, vertices):
    marcados = set()
    for v in solucion:
        marcados.add(v)
        for w in grafo.adyacentes(v):
            marcados.add(w)
    return len(marcados) == len(vertices)

grafo = Grafo()
for i in range(7):
    grafo.agregar_vertice(i)

grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 6)
grafo.agregar_arista(2, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(0, 5)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(3, 5)
grafo.agregar_arista(4, 5)
grafo.agregar_arista(6, 5)

# print(dominating_set(grafo,3))




# # 1. Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto 
# de vértices que representen un
# # mínimo Vertex Cover del mismo.


def vertex_cover(grafo):
    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas()
    return _vertex_cover(grafo, vertices, 0, [], [], aristas, set())


def _vertex_cover(grafo, vertices, i, solucion_parcial, solucion_minima, aristas_totales, aristas_marcadas:set):
    if len(aristas_totales) == len(aristas_marcadas):
        if not solucion_minima or len(solucion_parcial) < len(solucion_minima):
            solucion_minima = solucion_parcial.copy()
        return solucion_minima
    if i == len(vertices) or (len(solucion_parcial) > len(solucion_minima) and len(solucion_minima) != 0):
        return solucion_minima
    if agrega_aristas(vertices[i], grafo, aristas_marcadas):
        nuevo_set = aristas_marcadas.copy()
        for w in grafo.adyacentes(vertices[i]):
            nuevo_set.add((vertices[i], w))
            nuevo_set.add((w, vertices[i]))
        solucion_parcial.append(vertices[i])
        solucion_minima = _vertex_cover(grafo, vertices, i+1, solucion_parcial, solucion_minima, aristas_totales, nuevo_set)
        solucion_parcial.pop()
    return _vertex_cover(grafo, vertices, i+1, solucion_parcial, solucion_minima, aristas_totales, aristas_marcadas)

def agrega_aristas(v, grafo, aristas_marcadas):
    for w in grafo.adyacentes(v):
        if (v, w) not in aristas_marcadas:
            return True
    return False

#K-CLique

def k_clique(grafo):
    vertices = grafo.obtener_vertices()
    return _k_clique(grafo, vertices, 0, [], [])
    


def _k_clique(grafo, vertices, i, solucion_parcial, solucion_max):
    if i == len(vertices):
        return solucion_max
    if es_agregable(grafo, vertices[i], solucion_parcial):
        solucion_parcial.append(vertices[i])
        if len(solucion_parcial) > len(solucion_max):
            solucion_max = solucion_parcial[:]
        solucion_max = _k_clique(grafo, vertices, i+1, solucion_parcial, solucion_max)
        solucion_parcial.pop()
    return _k_clique(grafo, vertices, i+1, solucion_parcial, solucion_max)


def es_agregable(grafo, v, solucion_parcial):
    for w in solucion_parcial:
        if not grafo.hay_arista(v, w):
            return False
    return True


grafo = Grafo()
for i in range(1, 7):
    grafo.agregar_vertice(i)

grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(3, 2)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(3, 5)
grafo.agregar_arista(3, 6)
grafo.agregar_arista(5, 6)
grafo.agregar_arista(4, 6)
grafo.agregar_arista(4, 5)



print(k_clique(grafo))





def k_coloreo():



def _k_coloreo(grafo, colores, v, k):
    for i in range(k):
        colores[v] = i
        correcto = True
        if not es_compatible(grafo, colores, v):
            continue
        for w in grafo.adyacentes(v):
            if w in colores:
                continue
            if not _k_coloreo(grafo, colores, w, k):
                correcto = False
                break
            if correcto:
                return True
    del colores[v]
    return False

