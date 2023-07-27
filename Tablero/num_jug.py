import random

def ruta_random():
    ruta = ""
    # Esta función genera una ruta aleatoria compuesta por una secuencia de caracteres "b" y "r".
    # Se inicializa una cadena vacía llamada ruta y se itera 10 veces.
    # En cada iteración, se genera un número aleatorio rutabin que puede ser 0 o 1.
    for i in range(10):
        # Si rutabin es 0, se agrega el carácter "b" a la ruta. Si rutabin es 1, se agrega el carácter "r" a la ruta
        rutabin = random.randint(0,1)
        if rutabin == 0:
            ruta = ruta+"b"
        else:
            ruta = ruta+"r"
    return ruta

def num_jug_rand():
    # Esta función genera un número aleatorio que representa el número de jugador. Utiliza la función random.randint(1,2)
    # para generar un número entero aleatorio entre 1 y 2.
    # Luego, devuelve el número de jugador generado.
    num_jug = random.randint(1,2)
    return num_jug

def num_ruta_random(ruta):
    num_ruta = random.randint(0,len(ruta)-1)
    return num_ruta

# Esta función genera un orden aleatorio para los turnos de juego. Se crea una lista vacía llamada orden y
# se selecciona aleatoriamente un número entre 1 y 2 para determinar el jugador que va primero.
def orden_turnos():
    # Si el número seleccionado es 1, se agrega [primero,0] a la lista orden, lo cual indica que el jugador 1 va
    # primero y no tiene penalización de tiempo. Luego, se agrega [2,3] a la lista orden, lo cual indica que el
    # jugador 2 va después del jugador 1 y tiene una penalización de tiempo de 3 unidades.
    orden = []
    primero = random.randint(1,2)
    # Si el número seleccionado es 2, se realiza un proceso similar pero intercambiando los roles de los jugadores.
    # Al finalizar, se devuelve la lista orden que contiene el orden de los turnos.
    if primero == 1:
        orden.append([primero,0])
        orden.append([2,3])
    if primero == 2:
        orden.append([primero,3])
        orden.append([1,0])
    return orden