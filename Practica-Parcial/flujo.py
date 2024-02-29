from queue import Queue
from grafo import Grafo

#Algoritmo de ford-fuckelson
def flujo(grafo, s, t):
    flujo = {}
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0
    grafo_residual = grafo.copiar()
    while True:
        camino = obtener_camino(grafo_residual, s, t)
        if camino is None:
            break
        capacidad_residual_camino = min_peso(camino, grafo_residual)
        for i in range(1, len(camino)):
            if grafo.hay_arista(camino[i-1], camino[i]):
                flujo[camino[i-1], camino[i]] += capacidad_residual_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
            else:
                flujo[camino[i], camino[i-1]] -= capacidad_residual_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
    return flujo


def actualizar_grafo_residual(grafo_residual, v, w, capacidad_residual_camino):
    peso_anterior = grafo_residual.peso(v, w)
    grafo_residual.sacar_arista(v, w)

    if peso_anterior != capacidad_residual_camino:
        grafo_residual.agregar_arista(v, w, peso_anterior - capacidad_residual_camino)

    if not grafo_residual.hay_arista(w, v):
        grafo_residual.agregar_arista(w, v, capacidad_residual_camino)
    else:
        grafo_residual.sacar_arista(w, v)
        grafo_residual.agregar_arista(w, v, peso_anterior + capacidad_residual_camino)





#O(V*E²) TEOREMA EDMONDS-KARP




def obtener_camino(grafo_residual, s, t):
    cola = Queue()
    visitados = set()
    padres = {}
    orden = {}
    visitados.add(s)
    padres[s] = None
    orden[s] = 0
    cola.put(s)
    while not cola.empty():
        v = cola.get()
        for w in grafo_residual.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                orden[w] = orden[v] + 1
                cola.put(w)
    res = []
    if t not in visitados:
        return None
    res.append(t)
    actual = t
    while True:
        padre = padres[actual]
        res.append(padre)
        actual = padre
        if padre == s:
            break
    res.reverse()
    return res


def min_peso(res, grafo_residual):
    peso_min = grafo_residual.peso(res[0], res[1])
    for i in range(2, len(res)):
        peso = grafo_residual.peso(res[i-1], res[i])
        if peso < peso_min:
            peso_min = peso
    return peso_min


# grafo_flujo = Grafo(True)

# grafo_flujo.agregar_vertice("Fu")
# grafo_flujo.agregar_vertice("J")
# grafo_flujo.agregar_vertice("K")
# grafo_flujo.agregar_vertice("F")
# grafo_flujo.agregar_vertice("Su")
# grafo_flujo.agregar_vertice("A")
# grafo_flujo.agregar_vertice("C")
# grafo_flujo.agregar_vertice("E")
# grafo_flujo.agregar_arista("Fu", "J", 1)
# grafo_flujo.agregar_arista("J", "K", 1)
# grafo_flujo.agregar_arista("K", "F", 1)
# grafo_flujo.agregar_arista("F", "Su", 1)
# grafo_flujo.agregar_arista("Fu", "A", 8)
# grafo_flujo.agregar_arista("A", "F", 1)
# grafo_flujo.agregar_arista("C", "E", 9)
# grafo_flujo.agregar_arista("A", "C", 10)
# grafo_flujo.agregar_arista("E", "Su", 13)


# print(flujo(grafo_flujo, "Fu", "Su"))








#Perfect Bipartite Matching

# Dado un grafo no dirigido, un match es un subconjunto de las aristas en el cual para todo
# vértice V a lo sumo una arista del match incide en V (en el match, tienen grado a lo sumo 1).
# Decimos que el vértice v está matcheado si hay alguna arista que incida en él (sino, está 
# unmatcheado). El matching máximo es aquel en el que tenemos la mayor cantidad de aristas 
# (matcheamos la mayor cantidad posible). 

#POR SER GRAFO BIPARTITO QUEDA DE COMPLEJIDE O(E*V)

# grafo = Grafo(True)
# grafo.agregar_vertice("Fu")
# grafo.agregar_vertice("Su")
# grafo.agregar_vertice("A")
# grafo.agregar_vertice("B")
# grafo.agregar_vertice("C")
# grafo.agregar_vertice("D")
# grafo.agregar_vertice("E")

# grafo.agregar_vertice("F")
# grafo.agregar_vertice("G")
# grafo.agregar_vertice("H")
# grafo.agregar_vertice("I")

# grafo.agregar_arista("Fu", "A")
# grafo.agregar_arista("Fu", "B")
# grafo.agregar_arista("Fu", "C")
# grafo.agregar_arista("Fu", "D")
# grafo.agregar_arista("Fu", "E")

# grafo.agregar_arista("A", "F")
# grafo.agregar_arista("A", "G")
# grafo.agregar_arista("B", "F")
# grafo.agregar_arista("B", "H")
# grafo.agregar_arista("C", "H")
# grafo.agregar_arista("D", "H")
# grafo.agregar_arista("D", "I")
# grafo.agregar_arista("E", "I")

# grafo.agregar_arista("F", "Su")
# grafo.agregar_arista("G", "Su")
# grafo.agregar_arista("H", "Su")
# grafo.agregar_arista("I", "Su")


# print(flujo(grafo, "Fu", "Su"))









# Disjoint Paths

# Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). 
# Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos 
# disjuntos s-t en G. 

#aristas de 1 y listo

# grafo = Grafo(True)
# grafo.agregar_vertice(10)
# grafo.agregar_vertice(11)
# for i in range(6):
#     grafo.agregar_vertice(i)

# grafo.agregar_arista(10, 0)
# grafo.agregar_arista(0, 1)
# grafo.agregar_arista(10, 1)
# grafo.agregar_arista(1, 2)
# grafo.agregar_arista(1, 3)
# grafo.agregar_arista(2, 4)
# grafo.agregar_arista(3, 4)
# grafo.agregar_arista(4, 5)
# grafo.agregar_arista(4, 11)
# grafo.agregar_arista(5, 11)

# print(flujo(grafo, 10, 11))







# Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir
# hasta 10 libros de la biblioteca. La biblioteca tiene 3 copias de cada libro. 
# Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita 
# obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos
# sea máxima. 

#HECHO EN PAPEL







# Suponer que tenemos una empresa que vende k productos y tenemos el historial de compras de
# cada cliente. Queremos enviar encuestas a n clientes para ver cuáles son los productos
# que más les gustan. 
# Consideraciones: 
# Cada cliente será consultado por un subset de productos (y siempre que él/ella hayan comprado). 
# La cantidad de preguntas a un cliente i debe estar entre Ci y Ci'. 
# Para cada producto j deben haber entre Pj y Pj' consultas. 

#HECHO EN PAPEL








# Airlines Scheduling
# Suponer que queremos schedulear cómo los aviones van de un aeropuerto a otro para
# cumplir horarios y demás. 
# Podemos decir que podemos usar un avión para un segmento/vuelo i y luego para otro j si: 
# El destino de i y el origen de j son el mismo. 
# Podemos agregar un vuelo desde el destino de i al origen de j con tiempo suficiente. 
# Decimos que el vuelo j es alcanzable desde el vuelo i si es posible usar el avión
# del vuelo i y después para el vuelo j. 
# Problema: ¿Podemos cumplir con los m vuelos usando a lo sumo k aviones?









# Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta la capacidad a 
# una artista, permita
# obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la 
# complejidad del algoritmo
# implementado.

def aumento_flujo(grafo_residual,grafo_original, s, t, flujo):
    while True:
        camino = obtener_camino(grafo_residual, s, t)
        if camino is None:
            return flujo
        capacidad_minima = min_peso(camino, grafo_residual)
        for i in range(1, len(camino)):
            if grafo_original.hay_arista(camino[i-1], camino[i]):
                flujo[camino[i-1], camino[i]] += capacidad_minima
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_minima)
            else:
                flujo[camino[i], camino[i-1]] -= capacidad_minima
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_minima)

        #es O(V+E) Ya que se re correria para agregar el nuevo camino
                




# Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más
# clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva
# comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de N/2
# simpatizantes en la comisión, cada persona puede representar a solo un club, cada club debe estar representado por
# un miembro. Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a
# qué partido pertenecen), nos dé una lista de representantes válidos. Indicar y justificar la complejidad del algoritmo
# implementado.

def comision_flujo(lista):
    grafo = Grafo(True)
    agregados = set()
    grafo.agregar_vertice("Fu")
    grafo.agregar_vertice("Su")
    for candidato in lista:
        if len(candidato) < 3:
            continue
        for i in range(len(candidato)):
            if candidato[i] in agregados:
                continue
            agregados.add(candidato[i])
            grafo.agregar_vertice(candidato[i])
            if i == 0:
                grafo.agregar_arista("Fu", candidato[0], len(lista) // 2)
            if i == 2:
                grafo.agregar_arista(candidato[2], "Su")
        grafo.agregar_arista(candidato[0], candidato[1])
        grafo.agregar_arista(candidato[1], candidato[2])
    flujo_personas = flujo(grafo, "Fu", "Su")
    print(flujo_personas)
    res = []
    for candidato in lista:
        if flujo_personas[candidato[0], candidato[1]] == 1 and flujo_personas[candidato[1], candidato[2]] == 1:
            if candidato[1] in res:
                continue
            res.append(candidato[1])
    return res

# lista = [["Milei", "Pepe", "San Lorenzo"], ["Massa", "Robby", "Boca"], ["Bullrich", "Juan", "Boca"], ["Otro", "Roberto", "Rasin"]]
# print(comision_flujo(lista))








# # En un hospital, se tiene un conjunto de médicos y un conjunto de pacientes. Cada médico 
# tiene un horario con franjas
# # horarias disponibles para citas médicas. Nuestro objetivo es emparejar médicos con pacientes
#  de manera que se maximice
# # el número total de citas médicas programadas. Implementar un algoritmo que resuelva dicho 
# problema de manera
# # eficiente. Indicar y justificar la complejidad del algoritmo implementado.
DOCTOR = 0
HORA = 1
NOMBRE = 2

def medicos_pacientes(franjas_horarias, pacientes):
    pacientes_agregados = set()
    grafo = Grafo(True)
    grafo.agregar_vertice("FU")
    grafo.agregar_vertice("SU")
    for franja in franjas_horarias:
        grafo.agregar_vertice(franja)
        grafo.agregar_arista("FU", franja)   #COMPLEJIDAD O(V*E) por ser bipartito
    for paciente in pacientes:
        if not paciente[NOMBRE] in pacientes_agregados:
            grafo.agregar_vertice(paciente[NOMBRE])
            grafo.agregar_arista(paciente[NOMBRE], "SU")
            pacientes_agregados.add(paciente[NOMBRE])
        grafo.agregar_arista((paciente[DOCTOR], paciente[HORA]), paciente[NOMBRE])
    flujo_max = flujo(grafo, "FU", "SU")
    return flujo_max



# franjas = [("dr1", 16), ("dr1", 18), ("dr1", 10), ("dr2", 9), ("dr2", 10), ("dr3", 16)]
# pacientes = [("dr1", 16,"pepe"), ("dr1", 18, "pepe"), ("dr2", 9, "juan"), ("dr2", 10, "rodri"), ("dr3", 16, "lucas"),  ("dr1", 10, "lucas")]
# print(medicos_pacientes(franjas, pacientes))



# Una empresa de autobuses se conformó luego de la fusión de varias
# compañías menores. Actualmente tienen diferentes rutas que cubrir.
# Cada una con horario de inicio en una ciudad y finalización en
# otra. Existe la posibilidad de cubrir con un mismo micro
# diferentes rutas.
# Siempre la ruta comienza desde donde parte el micro, pero también
# puede pasar que el micro tenga tiempo suficiente para trasladarse
# hasta otro punto y cubrir otra ruta. Cuentan con una flota activa
# de N micros. Necesitan saber si les es posible cubrir con ella los
# requerimientos o si requieren contar con micros extra.
# Resolver el problema utilizando como parte del mismo redes de
# flujo. Analice su complejidad temporal y espacial.

#IGUAL QUE EL DE LOS AVIONES



 # Definimos el Problema de la Evacuación de la siguiente manera: Se tiene un grafo dirigido 
# G = (V, E) que describe una red de caminos. 
# Tenemos una colección de nodos X ⊂ V que son los nodos poblados (ciudades) y otra colección
#  de nodos S ⊂ V que son los nodos de refugio (supondremos que X y S son disjuntos). 
# En caso de una emergencia queremos poder definir un conjunto de rutas de evacuación de 
# los nodos poblados a los refugios. 
# Un conjunto de rutas de evacuación es un conjunto de caminos en G tales que (i) cada
#  nodo en X es el origen de un camino, 
# (ii) el último nodo de cada camino es un refugio (está en S), y (iii) los caminos no 
# comparten aristas entre sí. 
 # Se pide: dados G, X y S, mostrar cómo se puede decidir en tiempo polinomial si es posible 
# construir un conjunto de rutas de evacuación 
# (usar flujo en redes para eso. Construir la red adecuada).


#DISJOINT PATHS


# Una empresa global de tecnología tiene un conjunto de "c" centros
# de cómputos. Cada centro "i" tiene una capacidad de procesamiento
# "pi" por día. Todos los centros están conectados en una red
# privada. En la red se encuentran enlaces punto a punto que fueron
# construidos en diferentes momentos. Por lo tanto cada enlace "j"
# tiene una capacidad de transmisión diaria de "ej" en ambos
# sentidos. Un enlace conecta dos centros de cómputos. No todos los
# centros de cómputos están conectados entre sí. Cada uno tiene
# enlaces a un subconjunto de ellos. Para un proceso intensivo han
# separado los centros de cómputos en dos conjuntos. Los primeros
# realizan un procesamiento de un lote de datos y los empaquetan
# para enviarselos a los segundos. Los segundos reciben los paquetes
# y terminan con un segundo procesamiento. No hay dependencia entre
# paquetes de datos ni impedimentos en determinar los tamaños de
# cada paquete.
# En base a una instancia de este problema desean determinar si va a
# ser posible o no procesar en el día todos los datos "d" .
# Modelar el problema como una red de flujo y explicar como
# resolverlo paso a paso. Analizar complejidad espacial y temporal.

#FUENTE CON LA CAPACIDAD DE LOS PRIMEROCS; SUMIDERO CON ARISTAS cON LA CAPACIDAD DE LOS SEGUNDOS
#LAS DEMAS ARISTAS SON LAS DE ENLACE CON SU RESPECTIVA CAPACIDAD

