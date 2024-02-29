# #karatsuba

# def karatsuba(num1, num2):
#     si son chicos, hago simplemente la multiplicacion
#     num1 = a * 2**n/2 + b
#     num2 = c * 2**n/2 + d
#     ac = karatsuba(a, c)   # O (n *1,6)
#     bd = karatsuba(d, b)
#     p = karatsuba(a+b, c+d)
#     return ac 2**n + (p-ac-bd) * 2**n/2 + bd



# def closest_pairs(plano):
#     construir px
#     construir py 
#     p0, p1 = closest_pairs_rec(px, py)
#     return p0, p1

# def closest_pairs_rec(px, py):
#     if len(px) <= 3: return minimo de los 3
#     construir rx, ry
#     consttruir qx, qy
#     d0, d1 = closest_pairs_rec(rx, ry)
#     d2, d3 = closest_pairs_rec(qx, qy)
#     minimo = min((d0, d1), (d2, d3))
#     x_estrella = max_pos_x()
#     construyo S que estén <= d de x_estrella
#     por cada punto s de Sy computar distancia contra los siguientes 15 puntos
# 	quedarse con s y s' que minimizan esa distancia
# 	if d(s, s') < d: return s, s'
# 	elif d(q0, q1) < d(r0, r1): return q0, q1
# 	else: return r0, r1






# #Implementar una funcion por div y conquista de orden O(NlogN) que
# dado un arreglo de n numeros enteros devuelva true o False
# si existe algun elemento que aparezca mas de la mitad de las veces.
# Justificar el orden de la solucion.

def _mas_de_la_mitad(arreglo):
    if len(arreglo) == 1:
        return arreglo[0], True
    candidato_izq, _ = _mas_de_la_mitad(arreglo[:len(arreglo) // 2])
    candidato_der, _ = _mas_de_la_mitad(arreglo[len(arreglo) // 2:])
    cant_izq = 0
    cant_der = 0
    for i in range(len(arreglo)):
        if arreglo[i] == candidato_izq:
            cant_izq += 1
        if arreglo[i] == candidato_der:
            cant_der += 1
    if cant_izq > len(arreglo) // 2:
        return candidato_izq, True
    if cant_der > len(arreglo) // 2:
        return candidato_der, True
    if cant_izq > cant_der:
        return candidato_izq, False
    return candidato_der, False

def mas_de_la_mitad(arreglo):
    _, es_valido = _mas_de_la_mitad(arreglo)
    return es_valido

# ej1 = [1, 2, 1, 2, 3]
# ej2 = [1, 1, 2, 3]
# ej3 = [1, 2, 3, 1, 1, 1]
# ej4 = [1]

# print(mas_de_la_mitad(ej1))
# print(mas_de_la_mitad(ej2))
# print(mas_de_la_mitad(ej3))
# print(mas_de_la_mitad(ej4))








# Tenemos un arreglo de tamaño 2n de la forma
# {C1, C2, C3, .. Cn, D1, D2, D3, ... Dn} tal que la cantidad total de
# elementos del arreglo es potencia de 2 (por ende, n tambien lo es)
# Implementar un algoritmo de division y conquista que modifique
# el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3 ..., Cn, Dn}
# sin utilizar espacion adicional. Cual es la complejidad del algo?
# pista: pensar primero como habria que hacer si el arreglo tuviera
# 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de alli
# el caso de 8 elementos, etc... para enconrtar el padron.


def _intercalado_dyc(arreglo, inicio, fin):
    if fin - inicio < 2:
        return arreglo
    medio = (inicio + fin) // 2
    arreglo =_intercalado_dyc(arreglo, inicio, medio)
    arreglo = _intercalado_dyc(arreglo, medio, fin)
    i = inicio + 1
    j = medio
    while i < medio:
        arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        i += 2
        j += 2
    return arreglo
    
def intercalado_dyc(arreglo):
    arreglo_res = arreglo.copy()
    _intercalado_dyc(arreglo_res, 0, len(arreglo))
    return arreglo_res


# arreglo1 = ["C1", "C2", "D1", "D2"]
# arreglo2 = ["C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]
# arreglo3 = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
# print(intercalado_dyc(arreglo1))
# print(intercalado_dyc(arreglo2))
# print(intercalado_dyc(arreglo3))


    



# Dado un arreglo de n enteros, encontrar el subarreglo contiguo de máxima suma
# , utilizando División y Conquista.
# Indicar y justificar la complejidad del algoritmo.

def suma_maxima_contigua(arreglo):
    res_izquierdo = _suma_maxima_contigua(arreglo[:len(arreglo) // 2])
    res_derecho = _suma_maxima_contigua(arreglo[len(arreglo) // 2:])
    sum_mayor_actual = 0
    mayor_arreglo = []
    suma_actual =  arreglo[len(arreglo) // 2]
    for i in range(len(arreglo) // 2-1, -1, -1):
        if suma_actual + arreglo[i] > sum_mayor_actual:
            mayor_arreglo = arreglo[i:len(arreglo) // 2]
            sum_mayor_actual = suma_actual + arreglo[i]
        suma_actual += arreglo[i]
    suma_actual = arreglo[len(arreglo) // 2 -1]
    for j in range(len(arreglo)// 2, len(arreglo)):
        if suma_actual + arreglo[j]> sum_mayor_actual:
            mayor_arreglo = arreglo[len(arreglo) // 2-1:j+1]
            sum_mayor_actual = suma_actual + arreglo[j]
        suma_actual += arreglo[j]
    i = 1
    j = len(arreglo) -2
    suma_actual = 0
    while i != len(arreglo) // 2-1 and j != len(arreglo) // 2:
        if suma_actual + arreglo[i] + arreglo[j]> sum_mayor_actual:
            mayor_arreglo = arreglo[i:j+1]
            sum_mayor_actual = suma_actual + arreglo[i] + arreglo[j]
        i += 1
        j -= 1
        suma_actual += arreglo[i] + arreglo[j]
    maximo = max(sum(res_izquierdo), sum(res_derecho), sum_mayor_actual)
    if maximo == sum_mayor_actual:
        return mayor_arreglo
    if maximo == sum(res_izquierdo):
        return res_izquierdo
    return res_derecho


def _suma_maxima_contigua(arreglo):
    if len(arreglo) == 1:
        return arreglo
    res_izquierdo = _suma_maxima_contigua(arreglo[:len(arreglo) // 2])
    res_derecho = _suma_maxima_contigua(arreglo[len(arreglo) // 2:])
    maximo = max(sum(res_izquierdo), sum(res_derecho), sum(arreglo))
    if maximo == sum(res_izquierdo):
        return res_izquierdo
    if maximo == sum(res_derecho):
        return res_derecho
    return arreglo

print(suma_maxima_contigua([2, 5, -3, 20, 32, 5, 8, 4, 2]))


#ECUacion de recurrencia = T(n) = 2T(n/2) + O(N) por teorema maestro = O(nlogn)



# Implementar un algoritmo que, por división y conquista, dado un arreglo de n números enteros
# devuelva true o false
# según si existe algún elemento que aparezca más de dos tercios de las veces. 
# El algoritmo debe ser O(n). Justificar la
# complejidad del algoritmo implementado.

def mas_de_dos_tercios(arreglo):
    candidato = _mas_de_dos_tercios(arreglo, 0, len(arreglo))
    cont = 0
    for i in range(len(arreglo)):
        if arreglo[i] == candidato:
            cont +=1
    if cont > len(arreglo) * (2/3):
        return True
    return False



def _mas_de_dos_tercios(arreglo, inicio, fin):
    if fin >= inicio:
        return arreglo[inicio]
    primer_tercio = (inicio + fin) // 3
    segundo_tercio = primer_tercio * 2
    candidato_1 = _mas_de_dos_tercios(arreglo, inicio, primer_tercio)
    candidato_2 = _mas_de_dos_tercios(arreglo, primer_tercio, segundo_tercio)
    cont_candidato1=0
    cont_candidato2= 0
    for i in range(inicio, fin):
        if arreglo[i] == candidato_1:
            cont_candidato1 += 1
        if arreglo[i] == candidato_2:
            cont_candidato2 += 1
    if cont_candidato1 > cont_candidato2:
        return candidato_1
    return candidato_2


# print(mas_de_dos_tercios([2, 2, 1, 2]))


#LA ecuacion de recurrencia resulta T(n) = 2T(n/3) + O(n) -> O(n) 



