tablero = {
    0: {'b': [5], 'r': [1,4]},
    1: {'b': [0,2,5], 'r': [4,6]},
    2: {'b': [5,7], 'r':[1,3,6]},
    3: {'b': [2,7], 'r': [6]},
    4: {'b': [0,5,8], 'r': [1,9]},
    5: {'b': [0,2,8,10], 'r':[1,4,6,9]},
    6: {'b': [2,5,7,10], 'r':[1,3,9,11]},
    7: {'b': [2,10], 'r':[3,6,11]},
    8: {'b': [5,13], 'r': [4,9,12]},
    9: {'b': [5,8,10,13], 'r': [4,6,12,14]},
    10: {'b': [5,7,13,15], 'r': [6,9,11,14]},
    11: {'b': [7,10,15], 'r': [6,14]},
    12: {'b': [8,13], 'r':[9]},
    13: {'b': [8,10], 'r': [9,12,14]},
    14: {'b': [10,13,15], 'r': [9,11]},
    15: {'b': [10], 'r': [11,14]}
}

def get_rutas(ruta,inicio):
    if not ruta:
        yield (inicio,)
        return
    for casilla in tablero[inicio][ruta[0]]:
        for camino in get_rutas(ruta[1:],casilla):
            yield (inicio,) + camino



def guardar_rutas(ruta, inicio, jugador):
    winner_file = open(f'rutas_ganadoras_jugador{jugador}.txt','w')
    with open(f'rutas_posibles_jugador{jugador}.txt','w') as file:
        
        for i in get_rutas(ruta,inicio):
            file.write(str(i)+"\n")

            if jugador == 1 and i[-1] == 15:
                winner_file.write(str(i)+"\n")
            if jugador == 2 and i[-1] == 12:
                winner_file.write(str(i)+"\n")
