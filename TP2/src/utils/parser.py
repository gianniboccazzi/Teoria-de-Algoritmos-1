import os

script_dir = os.path.dirname(__file__)
DIRECTORIO = script_dir + '/ejemplos'

def parse_archivos():
  inputs = []
  for filename in os.listdir(DIRECTORIO):
      output = []
      with open(os.path.join(DIRECTORIO, filename)) as archivo:
          for linea in archivo.readlines():
              output.append(int(linea.strip()))
          n = output[0]
          E = output[1:1+n]
          S = output[1+n:]
      inputs.append((n, E, S, filename))
  return inputs
        
                
