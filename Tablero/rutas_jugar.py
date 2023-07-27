import re
import num_jug as md
import numpy as np

def obtener_rutas_ganadoras(archivo):
    # Esta función recibe como entrada el nombre de un archivo y devuelve una lista de casillas ganadoras.
    # El código lee el contenido del archivo, divide el contenido en líneas y elimina la última línea. Luego,
    # selecciona aleatoriamente una de las rutas ganadoras y extrae las casillas numéricas de esa ruta.
    # Estas casillas se devuelven como una lista de enteros.
    r_gan = open(archivo,'r').read()
    r_gan = r_gan.split("\n")
    r_gan.pop(-1)
    if len(r_gan) == 0:
        return None
    else:
        sel_ruta = md.num_ruta_random(r_gan)
        casillas = [int(i) for i in re.findall("\d+",r_gan[sel_ruta])]
        return casillas

def reconfiguracion_rutas(ruta1, ruta2):
    print(f"Ruta: {ruta1}")
    print(f"Ruta: {ruta2}")
    pos = np.arange(len(ruta1))
    for i,r1,r2 in zip(pos,ruta1,ruta2):
        if r1 == r2:
            ruta2.insert(i,ruta2[i-1])
            print(f"Ruta p: {ruta1}")
            print(f"Ruta r: {ruta2}")
        if r1 == ruta2[i-1]:
            ruta1.insert(i,ruta1[i-1])
            print(f"Ruta r: {ruta1}")
            print(f"Ruta p: {ruta2}") 
            if ruta1[i] == ruta2[i]:
                print("No se puede finalizar el juego porque las piezas van a chocar")
           
    return ruta1,ruta2

def encontrar_jugadorGanador(jugador1, jugador2):
    # Esta función recibe dos jugadores como entrada, donde cada jugador es una tupla que contiene
    # un nombre de jugador y una lista de casillas.
    casillas1 = len(jugador1[1])
    casillas2 = len(jugador2[1])
    # Si ambos jugadores tienen la misma cantidad de casillas, se devuelve el nombre del jugador 1.
    if casillas1 < casillas2:
        return jugador1[0]
    elif casillas2 < casillas1:
        return jugador2[0]
    elif casillas1 == casillas2:
        return jugador1[0]

            
