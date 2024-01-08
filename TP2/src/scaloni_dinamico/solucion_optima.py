import time

def scaloni_dinamico(n, ganancia, energia):
  inicio = time.time_ns()
  res = [[0] * n for _ in range (n)]
  res[0][0] = min ( ganancia[0] , energia[0])
  if n == 1:
        fin = time.time_ns()
        return (res, fin - inicio)
  res[1][0] = min ( ganancia[1] , energia[0])
  res[1][1] = res [0][0] + min ( ganancia[1] , energia[1])
  for dia in range (2 , n ) :
    res[dia][0] = max (res[dia -2]) + min(energia[0], ganancia[dia])
    for e in range (1 , n ) :
      if e > dia:
        break
      res[dia][e] = res[dia-1][e-1] + min(ganancia[dia], energia[e])
  fin = time.time_ns()
  return (res, fin - inicio)

def obtener_resultado(res, n):
  if n == 1:
        optimo = res[0][0]
        orden = ['Entreno']
        return (optimo, orden)
  optimo = max(res[n - 1])
  orden = ['Descanso'] * n
  dia_actual = n - 1 # Filas
  energia_actual = res[n-1].index(optimo) # Columnas
  while dia_actual >= 0:
    for i in range (energia_actual + 1):
      orden[dia_actual] = 'Entreno'
      if (i != energia_actual):
         dia_actual -= 1
      if (dia_actual < 0):
        break
    dia_actual -= 2
    energia_actual = res[dia_actual].index(max(res[dia_actual]))
  return (optimo, orden)
