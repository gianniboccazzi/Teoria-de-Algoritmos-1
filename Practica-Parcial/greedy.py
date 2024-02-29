import heapq
import random
# Tengo un aula/sala donde quiero dar charlas. 
# Las charlas tienen horario de inicio y fin. 
# Quiero utilizar el aula para dar la mayor cantidad de charlas. 

def scheduling(charlas:list):
    charlas.sort(key=lambda x: x[1]) #O(nlogn)
    elecciones = []
    elecciones.append(charlas[0])
    for charla in charlas: #O(n)
        if elecciones[-1][1] <= charla[0]: #O(1)
            elecciones.append(charla)
    return elecciones


# charlas=[(0,3), (0, 4), (4, 5), (7, 10), (9, 10), (11, 16), (11, 13), (0, 10)]
# print(scheduling(charlas))

#Es siempre óptimo. De forma intuitiva, al agarrar el primero que termina es como si 
#estuvieramos achicando el intervalo y volvieramos a tener el mismo problema
#Estamos siempre haciendo lo mejor que podemos

#Según Eze, también se puede pensar como la charla que me va a liberar el aula lo antes posible

#Es greedy además porque iterativamente sigue una regla simple
# (en este caso, la próxima a finalizar) y me fijo que no intersequen



#ARBOL DE HUFFMAN

# def arbol_huffman(palabra):
#     heap = heap()
#     frecuencias = calcular_frecuencias()
#     for letra in frecuencia:
#         heapq.heappush(Hoja(caracter, frecuencia)) #sería O(nLogn) pero por heapify O(n)
#     while len(heap) > 1:
#         elem1= heapq.heappop(heap)
#         elem2 = heapq.heappop(heap)  #n veces en colo y desencolo (N log N)
#         heapq.heappush(Arbol(elem1[0]+elem2[0], elem1[1]+elem2[1]))
#     return codificar(heapq.heappop(heap)) #Por Buchwald, esto terminaria siendo o(nlogn)


#Cabe destacar que va 0 a la izquierda y 1 a la derecha. Cuando se va a descomprimir se pasa
#la tabla de frecuencias así se crea el mismo arbol de huffman y se descomprime.
#Para que quede el mismo arbol se debería usar el mismo heap y las cosas
#Se deberían guardar en el mismo orden.

#Es greedy porque la regla simple es sacar los de menos frecuencia siempre
#El óptimo local es llevar al fondo los menos frecuentes, y eso me lleva al global (texto más liviano)




#Problema del cambio

# Se tiene un sistema de monetario. Se quiere dar cambio de una deter-
# minada cantidad de plata. Implementar un algoritmo que devuelva el
# cambio pedido, usando la mınima cantidad de monedas/billetes.


def problema_cambio_greedy(sistema_monetario, vuelto):
    cant_monedas = 0
    for i in range(len(sistema_monetario)-1, -1, -1):
        if sistema_monetario[i] <= vuelto:
            cant_veces = vuelto // sistema_monetario[i]
            vuelto -= cant_veces * sistema_monetario[i]
            cant_monedas += cant_veces
        else:
            i -= 1
    return cant_monedas

#Complejidad O(n) suponiendo que estan ordenadas las monedas

# sistema_monetario = [1, 5, 6, 9] 
# vuelto = 23
# print(problema_cambio_greedy(sistema_monetario, vuelto))
#NO ES OPTIMO





#Problema de compras con inflación
# Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. 
# Cada día debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de 
# inflación y los precios aumentan todo el tiempo. 
# El precio del producto i el día j es R[i]**(j + 1) (j comenzando en 0). 
# Implementar un algoritmo greedy que nos indique el precio mínimo al que 
# podemos comprar todos los productos.


def problema_compras_inflacion(productos):
    productos.sort(reverse=True)
    precio_total = 0
    j = 0
    for precio in productos:
        precio_total += precio ** (j+1)
        j += 1
    return precio_total
#Complejidad O(nlog n)

# productos = [1, 5, 7, 2, 8, 3, 9, 3, 2]

# print(problema_compras_inflacion(productos))

#ES OPTIMO, por el absurdo se puede ver (invirtiendo)

#regla greedy: dame el más caro que queda (la optimizacion es ordenar, no es la razon de ser greedy)






#Problema de la carga de combustible
#Un camión debe viajar desde una ciudad a otra deteniéndose a 
#cargar combustible cuando sea necesario. El tanque le permite
#viajar hasta K kilometros.
#Las estaciones se encuentran distribuidas a lo largo de la ruta 
#siendo d_i la distancia desde la estacion i-1 a la estacion i
#Implementar un algoritmo que decida en qué estaciones debe
#cargar combustible de manera que se detenga la menor cantidad
#de veces posible

def carga_combustible(k, estaciones):
    estaciones_a_frenar = []
    nafta_actual = k
    for i in range(len(estaciones)):
        if nafta_actual - estaciones[i][1] < 0:
            estaciones_a_frenar.append(estaciones[i-1])   #O(N)
            nafta_actual = k
        nafta_actual -= estaciones[i][1]
    return estaciones_a_frenar
        
estaciones = [("hudson", 20), ("avellaneda", 10), ("bera", 40), ("san telmo", 50), ("canning", 10)]
k = 50

# print(carga_combustible(k, estaciones))

#ES OPTIMO, palabras de martin: Cuando cuesta encontrar contraejemplo, es posible que sea óptimo
#pero en este caso es muy dificil de demostrar






#Problema de la mochila
# Tenemos una mochila con una capacidad W (peso, volumen). Hay elementos a guardar. 
# Cada elemento tiene un peso y un valor. Queremos maximizar el valor de lo que nos
# llevamos sin pasarnos de la capacidad.

#menor a mayor peso no funciona. Contraejemplo -> [(8, 1),(9, 9), (100, 10)]
#mayor a menor valor no funciona. Contraejemplo -> [ (10, 10), (9, 9), (8, 1) ]
#ordenar de mayor a menor en relacion v/w. Contraejemplo -> [(3, 1), (10, 10)]

def problema_mochila_greedy(w, elementos, criterio_de_ordenar, reverse):
    elementos = sorted(elementos, key=criterio_de_ordenar, reverse=reverse)
    res, peso_actual = [], 0
    for elemento in elementos:
        if peso_actual + elemento[1] > w:  #O(n log n)
            break
        res.append(elemento)
        peso_actual += elemento[1]
    return peso_actual

def relacion_v_w(tupla):
    return tupla[0] / tupla[1]

def relacion_mayor_valor(tupla):
    return tupla[0]

def relacion_menor_peso(tupla):
    return tupla[1]

# W = 100
# elementos = [(random.randint(1, 100), random.randint(1, W)) for _ in range(50)]
# print("solucion por mayor valor: ", problema_mochila_greedy(W, elementos, relacion_mayor_valor, True))
# print("solucion por menor peso: ", problema_mochila_greedy(W, elementos, relacion_menor_peso, False))
# print("solucion por mayor relacion v/w: ", problema_mochila_greedy(W, elementos, relacion_v_w, True))

#Si podemos fraccionar la mochila, es greedy y el v/w es óptimo






#Problema de Scheduling II - Minimizando latencia máxima

# Ahora tenemos tareas con una duración y un deadline (fecha límite), pero pueden 
# hacerse en cualquier momento, siempre que se hagan antes del deadline. 
# Para este problema, buscamos minimizar la latencia máxima en el que las tareas 
# se ejecuten. Es decir, si definimos que una tarea i empieza en si, entonces 
# termina en f_i = s_i + t_i, y su latencia es l_i = f_i - d_i (si f_i > d_i, sino 0). 

def scheduling_con_deadline(tareas):
    latencia = 0
    tiempo_corrido = 0
    tareas.sort(key= lambda x: x[1])
    for tarea in tareas:                            #O(n log n)
        tiempo_corrido += tarea[0]
        if tiempo_corrido - tarea[1] > 0:
            latencia += tiempo_corrido - tarea[1]
    return latencia


# tareas =  [(1, 2), (10, 10)] 
# print(scheduling_con_deadline(tareas))
#ES OPTIMO, un algoritmo que no considera cuanto dura cada tarea es optimo




#Optimal caching
#problema de memoria cache. Es similar al del viajante, es optimo si sacamos el
#elemento que más tarde se va a volver a requerir (suponiendo que lo sabemos)
#si no lo sabemos, entonces siempre sacamos el que se haya usado hace mas tiempo.







# Una empresa tiene n empleados, y k proyectos posibles a realizar. Cada proyecto 
# debe ser realizado por unos empleados en particular, y cada empleado puede realizar
# a lo sumo dos trabajos en total, en el tiempo que se tiene destinado para realizar 
# todos los proyectos (suponer que podrían trabajar en ambos en simultáneo).
# Por lo tanto, puede no ser posible realizar todos los proyectos. Implementar un algoritmo-
# greedy que permita determinar los proyectos a realizar, de forma de maximizar las ganancias 
# (cada proyecto da una ganancia distinta).
# Primero resolvamos en caso que cada proyecto tenga un único empleado como alternativa.
# Luego, que cada proyecto tenga varias alternativas (necesita de un empleado para que se encargue). 
# Luego, que cada proyecto tenga que usar a todos los empleados que tiene en el listado. 

# def problema_empleados_greedy(trabajos, empleados):
#     res = []
#     trabajos.sort(lambda x: x[0])
#     for trabajo in trabajos:
#         if hay_empleado_disponible(trabajo):
#             realizar_trabajo(empleados, trabajo)
#             res.append(trabajo)
#     return res









# Se tiene como posibles grupos sanguíneos de personas O, A, B y AB. Alguien con sangre tipo O sólo puede recibir sangre
# tipo O. Alguien de sangre A sólo puede recibir sangre de tipo A u O. Alguien de sangre tipo B sólo puede recibir sangre
# de tipo B u O. Alguien con sangre tipo AB puede recibir sangre de cualquier tipo. Se tienen las cantidades de bolsas de
# sangre disponibles (SA, SB, SAB, SO) y la cantidad de personas a tratar (PA, PB, PAB, PO). Implementar un algoritmo
# greedy que determine cómo se puede satisfacer la demanda de sangre (o si no puede hacerse). Indicar el orden del
# algoritmo y justificar por qué el algoritmo propuesto es un algoritmo greedy.
#O -> O   A -> A y O, B -> B y O, AB -> Cualquiera

def asignar_sangre(sangres, personas):
    #Ordenado primero O, A, B y luego AB
    res = {"O": [], "A": [], "B": [], "AB": []}
    compatibles = {0: [], 1: [0], 2:[0], 3:[0, 1, 2]}
    for i in range(len(personas)):
        cant_usada = min(sangres[i][1], personas[i][1])
        res[sangres[i][0]].append((personas[i][0], cant_usada))
        sangres[i][1] -= cant_usada
        personas[i][1] -= cant_usada
        if personas[i][1] > 0:
            if i == 0:
                return "No se puede"
            for j in compatibles[i]:  #Los compatibles están identificados por su indice en sangres
                if sangres[j][1] > 0:
                    cant_usada = min(sangres[j][1], personas[i][1])
                    res[sangres[j][0]].append((personas[i][0], cant_usada))
                    sangres[j][1] -= cant_usada
                    personas[i][1] -= cant_usada
                    if personas[i][1] == 0:
                        break
            if personas[i][1] > 0:
                return "No se puede"
    return res
# #Asumo que siempre la entrada es de esta manera
# sangres_disponibles = [["O", 14], ["A",5], ["B", 5], ["AB", 18]]
# personas_a_tratar = [["O", 2], ["A", 10], ["B", 10], ["AB", 10]]

# print(asignar_sangre(sangres_disponibles, personas_a_tratar))







# Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para 
# iluminarlos a todos.
# Implementar un algoritmo que Greedy que dé la cantidad mínima de faros que se necesitan para
# que todos los
# submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes
# (incluyendo las
# diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y
#  justificar la complejidad
# del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima?

def submarinos_greedy(matriz):
    faros = []
    while True:
        pos_max = None
        max_iluminados = 0
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                cant_iluminados = obtener_cant_iluminados(matriz, i, j)
                if cant_iluminados > max_iluminados:
                    max_iluminados = cant_iluminados
                    pos_max = (i, j)
        if max_iluminados == 0:
            return faros
        faros.append(pos_max)
        iluminar(matriz, pos_max)


def obtener_cant_iluminados(matriz, i, j):
    iluminados = 0
    for n in range(i-2, i + 3):
        for m in range(j-2, j+3):
            if 0 <= n < len(matriz) and 0 <= m < len(matriz[n]) and matriz[n][m] == "S":
                iluminados += 1
    return iluminados
    

def iluminar(matriz, pos_max):
    for i in range(pos_max[0]-2, pos_max[0] + 3):
        for j in range(pos_max[1] - 2, pos_max[1] + 3):
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[i]) and matriz[i][j] == "S":
                matriz[i][j] = "X"
        

    
# matriz = [["_"] * 10 for _ in range(12)]
# matriz[2][1] = "S"
# matriz[2][8] = "S"
# matriz[4][3] = "S"
# matriz[4][6] = "S"
# matriz[7][3] = "S"
# matriz[7][6] = "S"
# matriz[9][1] = "S"
# matriz[9][8] = "S"
# for i in range(len(matriz)):
#     print(matriz[i])
# print(submarinos_greedy(matriz))
    

    





# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se
# rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor
# forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto
# para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado
# encuentra siempre la solución óptima? Justificar.
                

def bolsas_super(productos, P):
    productos = sorted(productos, reverse=True)
    bolsas = []
    agregados = set()
    for i in range(len(productos)):
        bolsa_actual = []
        cant_actual = 0
        if i in agregados:
            continue
        bolsa_actual.append(productos[i])
        cant_actual += productos[i]
        agregados.add(i)
        if cant_actual == P:
            bolsas.append(bolsa_actual)
            continue
        for j in range(i, len(productos)):
            if j in agregados:
                continue
            if productos[j] + cant_actual <= P:
                bolsa_actual.append(productos[j])
                cant_actual += productos[j]
                agregados.add(j)
            if cant_actual == P:
                break
        bolsas.append(bolsa_actual)
    return bolsas

# print(bolsas_super([4, 2, 1, 3, 5], 5))






# Tenés una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente
# enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas que disponés son de la
# misma capacidad L (se asegura que L ≥ n). Obviamente, no podés partir un libro para que vaya en múltiples cajas,
# pero sí podés poner múltiples libros en una misma caja, siempre y cuando no superen esa capacidad L. Implementar un
# algoritmo Greedy que obtenga la mínima cantidad de cajas a utilizar. Indicar y justificar la complejidad del algoritmo
# implementado. Justificar por qué se trata de un algoritmo greedy (no dar una respuesta genérica, sino aplicada a tu
# algoritmo). ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.

        
def min_cajas(libros, L):
    agregados = set()
    cant_actual = 0
    cajas = 0
    libros = sorted(libros, reverse=True)
    for i in range(len(libros)):
        if i in agregados:
            continue
        if libros[i] + cant_actual <= L:
            cant_actual += libros[i]
            agregados.add(i)
            if cant_actual == L:
                cajas += 1
                cant_actual = 0      #O(N²)
                continue
            for j in range(i, len(libros)):
                if j in agregados:
                    continue
                if libros[j] + cant_actual <= L:
                    cant_actual += libros[j]
                    agregados.add(j)
                    if cant_actual == L:
                        break
            cajas += 1
            cant_actual = 0
    return cajas


# print(min_cajas([3, 3, 2, 2, 2, 2], 7))

#ES un algoritmo greedy ya que utiliza una regla continuamente para encontrar un optimo local.
#en este caso, esa regla greedy sería siempre meter al próximo mayor libro, con el fin de 
#utilizar la menor cantidad de cajas posibles. Esto llevaría a que, meter el mas grande posible
#tendería a minimizar el peso de las cajas siguientes.
#Sin embargo, este algoritmo no es optimo:
#[3, 3, 2, 2, 2, 2] Peso 7: el algoritmo resuelve con 3, pero se puede resolver con 2






# Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la ciudad costera de Ciudad
# República. Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales
# no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el
# control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un rango de
# kilómetros (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 5, la mafia 2 le pide del 3 al 8, etc. . . ). Si hay una
# mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden
# solaparse). Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”,
# indistintamente de los kilómetros pedidos. Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con
# nadie, así lo único que le interesa es maximizar la cantidad de permisos otorgados (asegurándose de no otorgarle algún
# lugar a dos mafias diferentes). Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada
# mafia, y determine a cuáles se les otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su
# vez maximizando la cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado.
# Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

def arnook_greedy(pedidos):
    pedidos = sorted(pedidos,key= lambda x: x[1])
    res = [pedidos[0]]
    for i in range(1, len(pedidos)):
        if pedidos[i][0] >= pedidos[i][1]:
            res.append(pedidos[i])
    return res












# Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que
# usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que
# construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante
# conocido). Implementar un algoritmo Greedy que reciba las ubicaciones de las casas (número de kilómetro sobre esta
# ruta) y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura,
# y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo
# implementado. Justificar por qué se trata de un algoritmo greedy.

def antenas_greedy(casas, R):
    casas = sorted(casas)
    antenas = [casas[0]]
    for i in range(1, len(casas)):
        if antenas[-1] + R < casas[i]:
            antenas.append(casas[i])
    return antenas

casas = [0, 20, 50, 120, 130, 170, 180]
print(antenas_greedy(casas, 30))


#COMPLEJIDAD O(NLOGN)
#Se trata de un algoritmo greedy ya que el algoritmo sigue una regla que obtiene un optimo local.
#En este caso, esa regla greedy consiste en siempre poner una antena al proximo que no le alcance el radio de la ultima antena puesta.





# Un importante museo nacional tiene "n" piezas de arte en diferentes bóvedas de seguridad 
# (1 pieza por bóveda inicialmente). Se ha programado una exposición especial que requiere que 
# esas n piezas se reúnan para luego ser transportadas al lugar designado. Para la movilización 
# se ha contratado un seguro que cobra un valor cada vez que una pieza corre riesgo de robo (cuando
#  la bóveda que la contiene se abre). Cada pieza fue tasada con un valor determinado. Cuando se
# realiza un traslado hay 2 bóvedas involucradas. Se abren tanto la bóveda de origen como la de 
# destino. Por lo tanto se debe pagar al seguro los valores de los que están almacenados en ambas 
# bóvedas. En el traslado se pueden seleccionar cualquier cantidad de las piezas que están en las
# bóvedas involucradas. Deseamos determinar qué traslados realizar de forma de lograr unificar en
# una sola bóveda todos las piezas abonando la menor cantidad de plata a la aseguradora. Proponer 
# un algoritmo greedy que solucione el problema (y que sea óptimo).

# Ejemplo: Si tengo 4 piezas con sus respectivos valores en 4 bóvedas. A: p1=5 B: p2=4 C: p3=2
# D: p4=6 Si comienzo trasladando p1 a la bóveda B. Deberé abrir la bóveda A y B. Se pagará al 
# seguro 5+4=9 por el proceso. Si ahora se desea trasladar p3 a la bóveda B se deberá pagar
# 2+5+4=11. El proceso continúa hasta que todas las piezas estén unificadas.

VALOR = 1
def bovedas_greedy(bovedas):
    bovedas = sorted(bovedas, key=lambda x: x[VALOR])
    historial = []
    boveda_destino = bovedas[0]
    sumatoria_actual = 0
    cont_actual = bovedas[0][VALOR]
    for i in range(1, len(bovedas)):   #O(N)
        historial.append((bovedas[i], boveda_destino))
        cont_actual += bovedas[i][VALOR]
        sumatoria_actual += cont_actual
    return (sumatoria_actual, historial)

bovedas = [("boveda1", 5), ("boveda2", 4), ("boveda3", 3), ("boveda4", 6)]

print(bovedas_greedy(bovedas))
#Es un algoritmo greedy ya que constantemente se aplica una regla para obtener un óptimo local.
#En este caso esa regla consistiría en poner de menor a mayor, las bovedas en la boveda más chica
#Con lo cual siempre se buscaría sumar la menor cantidad de impuesto. Esto se realiza iterativamente
#Hasta obtener el menor precio
    



# Un fabricante de perfumes está intentando crear una nueva
# fragancia. Desea que la misma sea del menor costo posible. El
# perfumista le indicó un listado de ingredientes. Por cada uno de
# ellos determinó una cantidad mínima (puede ser cero) y una máxima
# que debe contar en la fórmula final. Cada ingrediente tiene
# asociado un costo por milímetros cúbicos. Conocemos que la
# presentación final es de X milímetros cúbicos totales. Presentar
# una solución utilizando metodología greedy que resuelva el
# problema. Analizar la complejidad temporal y espacial. Probar
# optimalidad

NOMBRE = 0
CAP_MINIMA = 1
CAP_MAXIMA = 2
VALOR = 3
def fabrica_perfumes_greedy(capacidad_total, ingredientes):
    resultado = {}
    precio_total = 0
    capacidad_actual = 0
    ingredientes = sorted(ingredientes, key=lambda x: x[VALOR])
    for ingrediente in ingredientes:
        resultado[ingrediente[NOMBRE]] = ingrediente[CAP_MINIMA]
        capacidad_actual += ingrediente[CAP_MINIMA]
        precio_total += ingrediente[CAP_MINIMA] * ingrediente[VALOR]
    for ingrediente in ingredientes:
        capacidad_posible = ingrediente[CAP_MAXIMA] - ingrediente[CAP_MINIMA]
        if capacidad_posible + capacidad_actual > capacidad_total:
            capacidad_posible = capacidad_total - capacidad_actual
            resultado[ingrediente[NOMBRE]] += capacidad_posible
            precio_total += capacidad_posible * ingrediente[VALOR]
            break
        resultado[ingrediente[NOMBRE]] += capacidad_posible
        precio_total += capacidad_posible * ingrediente[VALOR]
        capacidad_actual += capacidad_posible
    return resultado, precio_total

capacidad_total = 20
ingredientes = [("jabon", 1, 5, 15), ("otro jabon", 2, 6, 20), ("otro mas", 10, 12, 50)]
print(fabrica_perfumes_greedy(capacidad_total, ingredientes))

#Este algoritmo es greedy ya que para resolver el problema, se realiza una regla simple
#que iterativamente va obteniendo un optimo local, para finalmente obtener el optimo global
#esa regla, en este caso consiste en primero poner los mínimos requeridos de cada ingrediente
#y luego agregar lo más que se pueda del más barato hasta alcanzar su máximo posible, y así
#con cada ingrediente hasta alcanzar la capacidad requerida. De esta forma, esta regla
#permite primeramente cumplir con lo minimo requerido, y luego ir poniendo siempre lo mas
#barato dispoible. Es optimo.