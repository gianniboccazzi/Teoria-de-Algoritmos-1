from queue import Queue

#Fibonacci dinamico
from grafo import Grafo

def fibonacci_dinamico(n):
    nums = [0] * (n+1) #O(N)
    nums[0] = 0
    nums[1] = 1
    for i in range(2, n+1): #O(N)
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]


# print(fibonacci_dinamico(10))


#fib(n) = fib(n-1) + fib(n-2)


# Problema de Scheduling con pesos

# Tengo un aula/sala donde quiero dar charlas. Las charlas tienen horario de inicio 
# y fin, y un peso asociado al valor de cada charla. Quiero utilizar el aula para 
# maximizar la sumatoria de pesos de las charlas dadas. 
def obtener_ultimo_sin_interseccion(charlas):
    res = {}
    for i in range(len(charlas)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if charlas[i][0] >= charlas[j][1]:  #O(N²)
                res[i] = j
                break
    return res 
                


def scheduling_con_pesos(charlas, p):
    print(p)
    res = [0] * (len(charlas)+1)
    res[0] = 0
    res[1] = charlas[0][2]
    for i in range(2, len(charlas)+1):
        if not i-1 in p:     #O(N)
            p_actual = 0
        else:
            p_actual = p[i-1] + 1
        res[i] = max(res[i-1], charlas[i-1][2] + res[p_actual])
    return res

def imprimir_solucion(res, p, charlas):
    aux = []
    i = len(res)-1
    while i >= 0:
        if i-1 not in p:
            p_actual = 0
        else:
            p_actual = p[i-1] + 1
        if charlas[i-1][2] + res[p_actual] >= res[i-1]:
            aux.append(i-1)
            i = p_actual
        else:
            i -= 1
    aux.reverse()
    return aux
    

# charlas = [(0, 2, 2), (1, 5, 4), (4, 8, 4), (3, 10, 7), (9, 11, 2), (10, 12, 2)]
# p = obtener_ultimo_sin_interseccion(charlas)
# res = scheduling_con_pesos(charlas, p)
# print(res)
# print(imprimir_solucion(res, p, charlas))


#Ecuacion de recurrencia = OPT(n) = MAX(OPT(n-1), valor_actual + OPT(p(n)))








# Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, 
# pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar
# cada día, determinar por programación dinámica el máximo monto a ganar, sabiendo que no 
# aceptará trabajar dos días seguidos.

def juan_el_vago(dias):
    res = [0] * len(dias)
    res[0] = dias[0]
    res[1] = max(dias[0], dias[1])
    for i in range(2, len(dias)):  #O(N)
        res[i] = max(res[i-1], dias[i] + res[i-2])
    return res

dias1 = [100, 20, 30, 70, 50] 
dias2 = [100, 20, 30, 70, 20]

opt1 = juan_el_vago(dias1)
opt2 = juan_el_vago(dias2)


#Ecuacion de recurrencia OPT(n) = max(opt(n-1), valor[n] + opt(n-2))

def imprimir_recorrido(opt, dias):
    res = []
    i = len(opt)-1
    while i >= 2:
        if dias[i] + opt[i-2] > opt[i-1]:
            res.append(i)  #O(N)
            i -= 2
        else:
            i -= 1
    if i == 1 and dias[1] > dias[0]:
        res.append(1)
    else:
        res.append(0)
    res.reverse()
    return res

# print(opt1)

# print(imprimir_recorrido(opt1, dias1))
# print(opt2)

# print(imprimir_recorrido(opt2, dias2))
        










# Caminos posibles en un laberinto
# Dado un laberinto representado por una grilla, queremos calcular la cantidad
# de caminos posibles que existen para llegar desde la posición (0,0) hasta 
# la posición NxM
# Los movimientos permitidos son, desde la esquina superior izquierda (el 0,0), 
# nos podemos mover hacia abajo o hacia la derecha

def caminos_posibles_laberinto(n, m):
    matriz = [[0] * (m+1) for _ in range(n+1)]
    matriz[0][0] = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0 and j == 0:
                continue
            if j == 0:
                matriz[i][j] = matriz[i-1][j]
            elif i == 0:
                matriz[i][j] = matriz[i][j-1] 
            else:
                matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]
    return matriz[n][m]


# print(caminos_posibles_laberinto(2, 2))

#camino(n, m) = camino(n-1, m) + camino(n, m-1)

# Dado un laberinto representado por una grilla, queremos calcular la ganancia 
# máxima que existe desde la posición (0,0) hasta la posición NxM

def laberinto_ganancia_maxima(n, m, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if n == 0 and m == 0:
                continue
            if n == 0:
                matriz[i][j] += matriz[i][j-1]  #O(n*m)
            elif m == 0:
                matriz[i][j] += matriz[i-1][j]
            else:
                matriz[i][j] += max(matriz[i-1][j], matriz[i][j-1])
            print(matriz[i][j])
    return matriz

matriz = [[0, 1, 2], [4, 3, 3], [5, 2, 7]]

# print(laberinto_ganancia_maxima(1, 1, matriz))


#ganancia_max(n, m) = max(ganancia_max(n-1, m), ganancia_max(n, m-1))


        


# Caminos a través del teclado del teléfono

# Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad 
# de posibles números de longitud N empezando por cierto botón. Restricción: solamente 
# se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual.

# grafo = Grafo()
# for i in range(10):
#     grafo.agregar_vertice(i)
# grafo.agregar_arista(1, 2)
# grafo.agregar_arista(1, 4)
# grafo.agregar_arista(2, 5)
# grafo.agregar_arista(2, 3)
# grafo.agregar_arista(4, 5)
# grafo.agregar_arista(4, 7)
# grafo.agregar_arista(5, 6)
# grafo.agregar_arista(5, 8)
# grafo.agregar_arista(3, 6)
# grafo.agregar_arista(6, 9)
# grafo.agregar_arista(7, 8)
# grafo.agregar_arista(8, 9)
# grafo.agregar_arista(9, 0)



def teclado_numerico(k, grafo, n):
    res = []
    contador_inicial = {}
    for v in grafo.obtener_vertices():
        contador_inicial[v] = 1
    res.append(contador_inicial)
    for _ in range(1, n+1):
        contador_actual = {}
        for v in grafo.obtener_vertices():   #O(n*V*(V+E))
            contador_actual[v] = contador_actual.get(v, 0) + res[-1][v]
            for w in grafo.adyacentes(v):
                contador_actual[v] = contador_actual.get(v, 0) + res[-1][w]
        res.append(contador_actual)
    return res[n-1][k]

# print(teclado_numerico(5, grafo, 2))

#cant(numero, n) = cant(numero, n-1) + para cada vecino cant(vecino, n-1) 



#Problema de la mochila
# Tenemos una mochila con una capacidad W (ya sea peso, volumen). Hay elementos a guardar.
# Cada elemento tiene un peso que ocupa de la capacidad y un valor. Queremos maximizar 
# el valor de lo que llevamos sin exceder la capacidad.
#opt(n,W) = max(opt(n-1, W), elementos[n] + opt(n-1, W-peso[n]))

def mochila(W, elementos):
    opt = [[0] * (W+1) for _ in range(len(elementos)+1)]
    for i in range(1, len(opt)):
        for j in range(1, W+1):
            peso_elemento = elementos[i-1][1]
            if peso_elemento > j:                 #O(n*2^m)
                opt[i][j] = opt[i-1][j]
                continue
            opt_previo = opt[i-1][j-peso_elemento]
            opt[i][j] = max(opt[i-1][j], elementos[i-1][0] + opt_previo)
    return opt


elementos = [(10, 6), (1, 1), (8, 3), (100, 100), (6, 4), (11, 2), (7, 8), (2, 7), (11, 9)]
opt = mochila(11, elementos)
def reconstruir_mochila(res, W, elementos):
    sol = []
    i = len(elementos)
    j = W
    while i != 0 and j != 0:
        # print(res[i][j])
        if j-elementos[i-1][1] >= 0 and res[i-1][j-elementos[i-1][1]] + elementos[i-1][0] == res[i][j]:
            sol.append(elementos[i-1])
            j -= elementos[i-1][1]
        i -= 1
    return sol
            

# print(reconstruir_mochila(opt, 11, elementos))


#PROBLEMA DEL CAMBIO DINAMICO

# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio"
# de una determinada cantidad de plata. Implementar un algoritmo que devuelva el 
# cambio pedido, usando la mínima cantidad de monedas/billetes. 


def cambio(vuelto, sistema_monetario):
    res = [0] * (vuelto + 1)
    for i in range(1, len(res)):
        minimo = i
        for moneda in sistema_monetario:
            if moneda > i:
                continue
            if 1 + res[i-moneda] < minimo:
                minimo = 1 + res[i-moneda]
        res[i] = minimo
    return res

#ECUACION DE RECURRENCIA: cambio(n) = 1 + min(para cada moneda > n:  cambio(n-moneda))
# sistema_monetario = [1, 4, 9, 16] 
# vuelto = 10
#COMPLEJIDAD = O(V*S)
# print(cambio(vuelto, sistema_monetario))









# Calcular la Distancia de Edición entre dos cadenas
# En resumen: existen 4 opciones
# Los caracteres coinciden: habrá que calcular la solución óptima para un problema definido
# como: i-1 en cadena X y j-1 en cadena Y.
# Reemplazar caracteres: sumar un costo y calcular la solución óptima para un problema 
# definido como: i-1 en cadena X y j-1 en cadena Y.
# Brecha en la primera cadena: sumar un costo de brecha y calcular la solución óptima 
# para un problema definido como: i en cadena X y j-1 en cadena Y.
# Brecha en la segunda cadena: sumar un costo de brecha y calcular la solución óptima 
# para un problema definido como: i-1 en cadena X y j en cadena Y.


#ECUACION DE RECURRENCIA: OPT(i, j) =  si los caracteres coinciden -> opt(i-1, j-1)
                                    #min(costo de reemplazo de caracter + opt(i-1, j-1), brecha + 
                                     #opt(i-1, j), brecha + opt(i, j-1))

def costo_alineamiento(palabra1, palabra2):
    consonantes = set('bcdfghjklmnpqrstvwxyz')
    vocales = set('aeiou')
    res = [[0] * (len(palabra1)+1) for _ in range(len(palabra1)+1)]
    for i in range(1, len(palabra1)+1):
        res[i][0] = res[i-1][0] + 2
        res[0][i] = res[0][i-1] + 2 
    for i in range(len(palabra1)):
        for j in range(len(palabra1)):
            if palabra1[i] == palabra2[j]:               #O(n * m)
                res[i+1][j+1] = res[i][j]
            elif palabra1[i] in vocales and palabra2[j] in vocales:
                res[i+1][j+1] = min(2 + res[i+1][j], 2 + res[i][j+1], 1 + res[i][j])
            elif palabra1[i] in consonantes and palabra2[j] in consonantes:
                res[i+1][j+1] = min(2 + res[i+1][j], 2 + res[i][j+1], 1 + res[i][j])
            else:
                res[i+1][j+1] = min(2 + res[i+1][j], 2 + res[i][j+1], 3 + res[i][j])
    return res

# print(costo_alineamiento("flan", "hola"))
#FALTARIA ALGORITMO PARA IMPRIMIR RESULTADO





#Subset sum
# Tenemos un conjunto de números v1, v2, … Vn, y queremos obtener un subconjunto de todos 
# esos números cuya suma sea igual a un valor V, o bien aproximar lo mayor posible a ese valor V.
# En definitiva quisiéramos maximizar la suma de los
# elementos del subconjunto sin exceder el valor V.

def subset_sum(conjunto, V):
    res = [[0] * (V+1) for _ in range(len(conjunto)+1)]
    for i in range(1, len(conjunto)+1):
        for j in range(1, V+1):
            if conjunto[i-1] > j:
                res[i][j] = res[i-1][j]  #O(n*m)
                continue
            if conjunto[i-1] + res[i-1][j-conjunto[i-1]] > j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j], conjunto[i-1] + res[i-1][j-conjunto[i-1]])
    return res[len(conjunto)][V]
    
# print(subset_sum([1, 5, 3, 6, 3, 2], 20))


#RECURRENCIA OPT(N) = max(opt(n-1, V), opt(n-1, v-vi) + vi)






#Tú a Londres y yo a California

# Manejamos un negocio que atiende clientes en Londres y en California.
# Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación 
# para cada mes pueden variar y son dados: Li y Ci para todo n
# Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, 
# habrá un costo fijo M por la mudanza.
# Dados los costos de operación en Londres (L) y California (C), indicar la secuencia 
# de las n localizaciones en las que operar durante n meses, sabiendo que queremos minimizar
# los costos de operación. Se puede empezar en cualquier ciudad.

#ECUACION DE RECURRENCIA opt(n, londres) = min(opt(n-1, londres), opt(n-1, cali) + M) y viceversa
M = 5
C = [10, 5, 10, 7, 13, 12]
L = [8, 9, 2, 18, 2, 15]

def londres_california(M, C, L):
    res_cali = [0] * len(C)
    res_lon = [0] * len(L)
    res_cali[0] = C[0]
    res_lon[0] = L[0]
    for i in range(1, len(C)):
        res_cali[i] = min(res_cali[i-1], res_lon[i-1] + M) + C[i]
        res_lon[i] = min(res_lon[i-1], res_cali[i-1] + M) + L[i]
    return res_cali, res_lon

def obtener_itinerario(res_cali, res_lon, M):
    res = []
    i = len(res_cali)-1
    actual = "Cali"
    if res_cali[-1] >= res_lon[-1]:
        res.append("Londres")
        actual = "Londres"
    else:
        res.append("Cali")
    while i > 0:
        if actual == "Londres":
            if res_lon[i-1] < res_cali[i-1] + M:
                res.append("Londres")
            else:
                res.append("Cali")
                actual = "Cali"
        else:
            if res_cali[i-1] < res_lon[i-1] + M:
                res.append("Cali")
            else:
                res.append("Londres")
                actual = "Londres"
        i -= 1
    res.reverse()
    return res


# res_cali, res_lon = londres_california(M, C, L)
# print(obtener_itinerario(res_cali, res_lon, M))












# Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1
# 2
# , por lo que siempre existe solución.

# Sin embargo, la expresión 10 = 3^2 + 1^2

# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos
# términos. Además, tener en cuenta que no se piden los términos, sino la cantidad mínima de términos cuadráticos
# necesaria.


def potencia_minima(n):
    res = [0] * (n+1)
    res[0] = 0
    res[1] = 1
    for i in range(2, n+1):
        minimo = i
        j = 2
        while j ** 2 <= i:     #O(n^1.5) ? 
            if 1 + res[i-j**2] < minimo:
                minimo = 1 + res[i-j**2]
            j += 1
        res[i] = minimo
    return res

# print(potencia_minima(10))


#ECUACION DE RECURRENCIA = OPT(n) = 1 + min(para cada m**2 <= n: res[n-m])






# Dada una soga de n metros (n ≥ 2) implementar un algoritmo que, utilizando programación dinámica, 
# permita cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una 
# de las partes resultantes sea máximo. El algoritmo debe devolver el valor del producto máximo 
# alcanzable. Indicar y justificar la complejidad del algoritmo.
# Ejemplos:
# n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
# n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
# n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
# n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)

def soga(n):
    res = [0] * (n+1)
    res[0] = 0
    res[1] = 1
    for i in range(2, n+1):
        maximo = 0 
        for j in range(1, i):
            actual = max(res[j] * res[i-j], j * res[i-j], res[j] * (i-j), j * (i-j))
            if actual > maximo:
                maximo = actual
        res[i] = maximo
    return res

# print(soga(10))


#ECUACION DE RECURRENCIA = OPT(n) = max(i * n-i, opt(i) * opt(n-i), i * opt(n-i) * opt(i) * n-i)




# Sea G un grafo dirigido “camino” (las aristas son de la forma (vi , vi+1)). Cada vertice tiene
# un valor (positivo). Implementar un algoritmo que, utilizando programación dinámica, obtenga el
# Set Independiente de suma máxima dentro de un grafo de dichas características.
# Indicar y justificar la complejidad del algoritmo implementado.

grafo = Grafo(True)
grafo.agregar_vertice(100)
grafo.agregar_vertice(20)
grafo.agregar_vertice(30)
grafo.agregar_vertice(70)
grafo.agregar_vertice(50)
grafo.agregar_arista(100, 20)
grafo.agregar_arista(20, 30)
grafo.agregar_arista(30, 70)
grafo.agregar_arista(70, 50)

def independent_set_pd(grafo, v):
    res = [0] * (6)
    res[0] = 0
    cola = Queue()
    cola.put(v)
    res[1] = v
    i = 2
    while not cola.empty():
        v = cola.get()
        for w in grafo.adyacentes(v):   #O(V+E)
            res[i] = max(res[i-1], res[i-2] + w)
            cola.put(w)
        i += 1
    return res

# print(independent_set_pd(grafo, 100))

#ECUACION DE RECURRENCIA = OPT(N) = MAX(OPT(N-1), N + OPT(N-2))





# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.

def bodegon(P, W):
    res = [[0] * (W+1) for _ in range(len(P)+1)]
    res[0][0] = 0
    for i in range(1, len(P)+1):
        for j in range(1, W+1):
            if P[i-1] > j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j], P[i-1] + res[i-1][j-P[i-1]])
    return res
    

#ECUACION DE RECURENCIA = OPT(N, W) = MAX(OPT(N-1, W), P[N] + OPT(N-1, W-P[N]))
                

def reconstruccion_bodegon(res, P, W):
    elementos = []
    i = len(P)
    j = W
    while i != 0 and j != 0:
        if j-P[i-1] >= 0 and res[i-1][j-P[i-1]] + P[i-1] == res[i][j]:
            elementos.append(P[i-1])
            j -= P[i-1]
        i -= 1
    return elementos

# P = [2, 9, 10, 1, 99, 3]
# W = 15
# res = bodegon([2, 9, 10, 1, 99, 3],15)
# print(res)
# print(reconstruccion_bodegon(res, P, W))






# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar
# toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia
# realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa
# 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n − 1, que
# nos daría gn−1. Como la calle es circular, la casa 0 y la n − 1 son vecinas. El problema con el que cuenta el Lunático
# es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le
# daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos
# directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado
# que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un
# algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a
# partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia que
# correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.


def robo_lunatico(casas):
    res_1 = robar(casas[:len(casas)-2])
    res_2 = robar(casas[1:])   #O(2N) = O(N)
    if res_1[-1] >= res_2[-1]:
        return res_1, casas[:len(casas)-2]
    return res_2, casas[1:]

def robar(casas):
    res = [0] * len(casas)
    res[0] = casas[0]
    res[1] = max(casas[0], casas[1])     #O(N)
    for i in range(2, len(casas)):
        res[i] = max(res[i-1], casas[i] + res[i-2])
    return res

def reconstruccion_robo(res, casas):
    casas_robadas = []
    i = len(res)-1
    while i > 1:
        if res[i] == casas[i] + res[i-2]:
            casas_robadas.append(casas[i])
            i -= 2
        else:
            i -= 1
    if i == 1:
        casas_robadas.append(max(casas[1], casas[0]))
    if i == 0:
        casas_robadas.append(casas[0])
    casas_robadas.reverse()
    return casas_robadas


#ECUACION DE RECURRENCIA = OPT(barrio) = max(opt(plan1), opt(plan2))
#opt(n) = max(opt(n-1), ganancia[n] + opt(n-2))

# res, plan_robo = robo_lunatico([50, 20, 30, 90])
# print(res[-1])
# print(reconstruccion_robo(res, plan_robo))








# Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar de 0 a K, 
# siendo que las operaciones
# posibles son: (i) aumentar el valor del operando en 1; (ii) duplicar el valor del operando.
# Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones
# a realizar (y
# cómo son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y justificar
# la complejidad del algoritmo
# implementado.

def camino_operaciones_dinamico(k):
    res = [0] * (k+1)
    res[1] = 1
    res[2] = 2
    for i in range(3, k+1):
        if i % 2 != 0:
            res[i] = 1+ res[i-1]
        else:
            res[i] = 1 + min(res[i//2], res[i-1])
    return res

def reconstruccion_operaciones(res, k):
    solucion = []
    print(res)
    while k > 2:
        if res[k] == res[k-1] + 1 or k % 2 != 0:
            solucion.append("Sumé 1")
            k -= 1
        else:
            solucion.append("Dupliqué")
            k = k // 2
    solucion.append("Sume 1")
    solucion.append("Sume 1")
    solucion.reverse()
    return solucion

# res = camino_operaciones_dinamico(20)
# print(reconstruccion_operaciones(res, 20))



# Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un
# determinado presupuesto P que no
# puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La 
# campaña i cuesta $Ci. También se
# han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada
# campaña, que denominaremos Gi.
# Implementar un algoritmo que reciba esta información y devuelva cuáles campañas 
# debe realizar Carlitos. Indicar y
# justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores 
# están expresados en pesos argentinos,
# dólares u otra moneda? (haciendo la equivalencia de divisa, siempre
#  suponiendo valores enteros).
GANANCIA = 1
COSTO = 2
def carlitos_dinamico(publicidades, P):
    res = [[0] * (P+1) for _ in range(len(publicidades)+1)]
    for i in range(1, len(publicidades) + 1):
        for j in range(1, P+1):
            if publicidades[i-1][COSTO] > j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j], publicidades[i-1][GANANCIA] + res[i-1][j-publicidades[i-1][COSTO]])
    return res

def reconstruccion_carlitos(res, publicidades):
    sol = []
    i = len(res)-1
    j = len(res[i])-1
    while i > 0 and j > 0:
        if res[i][j] != res[i-1][j]:
            sol.append(publicidades[i-1])
            j -= publicidades[i-1][COSTO]
        i -= 1
    return sol
#COMPLEJIDAD ALGORITMICA = O(N*2^m)
#ECUACION DE RECURRENCIA = OPT(N, P) = MAX(OPT(N-1, P), GANANCIA[n] + OPT(N-1, P-costo[n]))
# publis = [("Publi1",10, 1), ("publi2",10, 1), ("publi3",1, 1), ("publi4",1, 1), ("publi5",8, 1), ("publi6",8, 1), ("publi7",2, 1), ("publi8",2, 1)]
# res = carlitos_dinamico(publis,2)
# print(reconstruccion_carlitos(res, publis))



# En su tiempo libre, Carlitos colecciona figuritas del mundial. Incluso a casi un año de la coronación de gloria, hay
# mucho entusiasmo por estas. Llegó a coleccionar tantas que ahora se dedica a revenderlas (para sacar unos pesos extra
# de su trabajo principal como publicista). Tiene tantas figuritas que ya no revende al público directamente, sino a otros
# revendedores y cadenas de kioscos. En general, cuando le piden, le piden figuritas “por una cantidad de dinero”. Cada
# tipo de figurita tiene un valor diferente (es decir, la de Messi no vale lo mismo que la del Bobo Weghorst). Podemos
# decir que absolutamente todos los tipos de figuritas tienen valores diferentes, todos valores enteros, y que Carlitos cuenta
# con una cantidad ridículamente alta de cada una de ellas. Por un análisis que hizo, sabe que si le piden figuritas por un
# determinado monto, le conviene dar la menor cantidad de figuritas posibles (siempre cumpliendo con el monto exacto
# pedido), incluso repitiendo figuritas en caso de ser necesario. El problema de las figuritas de Carlitos dice: dados los
# valores de los diferentes tipos de figuritas y un monto al que llegar, determinar cuáles figuritas debe dar Carlitos para
# cumplir exactamente con dicho monto dando la mínima cantidad de figuritas para ello.
# ¿Cuál problema de Carlitos sería el más difícil, el problema de las figuritas o el de su agencia publicitaria? Realizar una
# reducción polinomial de uno al otro para definir esto (redefinir como problemas de decisión como primer paso).


# El problema de la publicidad es más dificil que el problema de las figuritas. 
# Esto se debe a que el problema de las publicidades es un problema NP-Completo, ya que
# es una variante del problema de la mochila, el cual es NP Completo.
# Además, el problema de las figuritas es una variante del problema del cambio, 
# el cual está en P, y si fuese NP Completo, P = NP.
# Por lo tanto, se podría reducir el problema de las figuritas al problema de la publicidad.
# En problemas de decisión, el problema de las figuritas sería: "Se puede cumplir el monto con a lo sumo k figuritas?"
# mientras tanto, el problema de decision de las publicidades resulta: ¿se puede conseguir una ganancia G sin exceder un costo C de publicidades?
# Para realizar la reducción, a la "caja resolvedora del problema de publicidad" se le 
# debe pasar un arreglo de las siguientes caracteristicas:
# Cada figurita estará las veces necesarias hasta alcanzar el monto necesario
# Por ejemplo: Si se debe cumplir un monto de 5 y hay una figurita de valor 2, esta figurita
# debe estar 2 veces. (Este paso es polinomial)
# Además, cada figurita del arreglo tendrá costo 1.
# Entonces, simulando un ejemplo:
# En el problema de las figuritas se tiene un arreglo de figuritas de valores [2, 5, 4, 1] y se quiere alcanzar el valor 9 con 2 figuritas.
# Para reducir el problema, el arreglo que recibiría la caja resolvedora del problema de las publicidades sería [2, 2, 2, 2, 5, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Cada figurita tiene costo 1. Por lo tanto, se le pasa también un peso máximo 2. De esta forma, el problema tiene solucion ya que 5 y 4 llegan al valor deseado. 





# Para una inversión inmobiliaria un grupo inversor desea desarrollar un barrio privado 
# paralelo a la una ruta. Con ese motivo realizaron una evaluación de los diferentes terrenos 
# en un trayecto de la misma. Diferentes inversores participarán, pero a condición de comprar
# algún terreno en particular. El grupo inversor determinó para cada propiedad su evaluación
# de ganancia. El mismo surge como la suma de inversiones ofrecida por el terreno menos el 
# costo de compra. Debemos recomendar que terrenos contiguos comprar para que maximicen sus
# ganancias.  Ejemplo: S = [-2, 3, -3, 4, -1, 2]. La mayor ganancia es de 5, comprando los 
# terrenos de valor  [4, -1, 2]. Solucionar el problema mediante un algoritmo de programación
# dinámica.

def subconjunto_maximo(arreglo):
    res = [0] * len(arreglo)
    res[0] = arreglo[0]
    for i in range(1,len(arreglo)):
        res[i] = max(res[i-1] + arreglo[i], arreglo[i])
    return res

S =  [-2, 3, -3, 4, -1, 2]
res = subconjunto_maximo(S)

def reconstruccion_subconjunto(arreglo, res):
    suma_actual = 0
    reconstruccion = []
    for i in range(len(arreglo)):
        if arreglo[i] == res[i]:
            suma_actual = arreglo[i]
            reconstruccion = [arreglo[i]]
            continue
        suma_actual += arreglo[i]
        reconstruccion.append(arreglo[i])
        if suma_actual == res[-1]:
            return reconstruccion
        
print(reconstruccion_subconjunto(S, res))

