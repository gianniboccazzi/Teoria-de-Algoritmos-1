from ayuda_scaloni.solucion_optima import comparar_tiempos

SEP = "------------------------------------------------------------"
MENSAJE = "Elegi una opcion: \n 1. Comparar tiempos para 3, 10, 100 y 1000 elementos \n 2. Encontrar soluciones para 3, 10, 100, 1000 elementos \n 3. Ambas \n 4. Salir"
RETRY = "Respuesta invalida, intenta nuevamente"
START = "                     Ayuda a Scaloni!"
FUTBOL = "    -   \O                                     ,  .-.___       \n  -     /\                                   O/  /xx\XXX\      \n -   __/\ `                                  /\  |xx|XXX|      \n    `    \, ()                              ` << |xx|XXX|      \n^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

def main():
  print(FUTBOL)
  print(START)
  respuesta = 0
  while respuesta != 4: 
      print(SEP)
      print(MENSAJE)
      respuesta = int(input())
      if respuesta not in [1, 2 , 3, 4]:
        print(RETRY)
        continue
      if respuesta == 4:
         return 0
      else: 
        comparar_tiempos(respuesta)

if __name__ == "__main__":
   main()

