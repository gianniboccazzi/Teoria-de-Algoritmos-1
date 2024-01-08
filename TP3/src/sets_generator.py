from random import randint, sample
import os


script_dir = os.path.dirname(__file__)
DIRECTORIO = script_dir
MAX_POR_CONJUNTO = 6
JUGADORES_CONVOCADOS = 50

def set_generator(m, k, nombre_archivo):
    jugadores = [f"Jugador{i}" for i in range(1, JUGADORES_CONVOCADOS)]
    jugadores_optimos = sample(jugadores, k)
    with open(os.path.join(DIRECTORIO, nombre_archivo), 'w') as archivo:
        for _ in range(m):
            subconjunto = sample(jugadores, randint(1, MAX_POR_CONJUNTO))
            subconjunto.insert(randint(0, k - 1), jugadores_optimos[randint(0, k - 1)])
            archivo.write(','.join(subconjunto) + '\n')

