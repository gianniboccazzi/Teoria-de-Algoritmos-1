from scaloni_dinamico.solucion_optima import scaloni_dinamico, obtener_resultado
from utils.parser import parse_archivos

def main():
  inputs = parse_archivos()
  for input in inputs:
    n, E, S, filename = input
    resultado, tiempo = scaloni_dinamico(n, E, S)
    ganancia, orden = obtener_resultado(resultado, n)
    print(filename)
    print('Ganancia maxima: ' + str(ganancia))
    #print('Plan de entrenamiento: ' + ', '.join(orden))
    print('Tiempo de ejecucion: ' + str(tiempo) + ' ns')
    print('')

if __name__ == "__main__":
   main()

