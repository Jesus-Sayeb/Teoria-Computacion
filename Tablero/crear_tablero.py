import pygame

tablero = {
    0: [0, 0],
    1: [1, 0],
    2: [2, 0],
    3: [3, 0],
    4: [0, 1],
    5: [1, 1],
    6: [2, 1],
    7: [3, 1],
    8: [0, 2],
    9: [1, 2],
    10: [2, 2],
    11: [3, 2],
    12: [0, 3],
    13: [1, 3],
    14: [2, 3],
    15: [3, 3]
}

def un_jugador(casillas):
    # Inicializar Pygame
    # Esta función permite que un solo jugador mueva una pieza en el tablero. Comienza inicializando la ventana y el
    # tamaño del tablero. Luego, dibuja el tablero en la pantalla utilizando la función pygame.draw.rect. Después,
    # dentro de un bucle principal, se manejan los eventos de pygame. Si se detecta un evento de pulsación del botón
    # del mouse, se verifica si se han recorrido todas las casillas disponibles. Si no se han recorrido todas las
    # casillas, se obtiene la posición actual de la pieza y se dibuja en el tablero utilizando la función screen.blit.
    pygame.init()
    # Establecer el tamaño de la ventana
    window_size = (400, 400)
    # Crear la ventana
    screen = pygame.display.set_mode(window_size)
    # Establecer el título de la ventana
    pygame.display.set_caption("Tablero")
    # Establecer el tamaño de las casillas del tablero
    board_size = 100
    # Crear una lista de colores para las casillas del tablero
    colors = [(0, 0, 0), (255, 0, 0)]

    # Dibujar el tablero
    for row in range(4):
        for col in range(4):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, (col * board_size, row * board_size, board_size, board_size))

    # Actualizar la pantalla
    pygame.display.flip()
    peon = pygame.image.load("peon.png")
    i = 0
    # Bucle del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if i == (len(casillas)):
                    running = False
                else:
                    x = tablero[casillas[i]][0] * board_size
                    y = tablero[casillas[i]][1] * board_size
                    # El usuario ha presionado el botón del mouse
                    for row in range(4):
                        for col in range(4):
                            color = colors[(row + col) % 2]
                            pygame.draw.rect(screen, color,
                                             (col * board_size, row * board_size, board_size, board_size))
                    screen.blit(peon, (x, y))
                    pygame.display.flip()
                    i = i + 1

            elif event.type == pygame.MOUSEBUTTONUP:
                # El usuario ha soltado el botón del mouse
                pass


def dos_jugadores(casillas1, casillas2, fig1, fig2):
    # Esta función permite que dos jugadores muevan piezas en el tablero. Al igual que en la función anterior,
    # se inicializa la ventana y el tamaño del tablero, y se dibuja el tablero en la pantalla. El bucle principal
    # maneja los eventos de pygame. Si se detecta un evento de pulsación del botón del mouse, se verifica si se han
    # recorrido todas las casillas disponibles para ambos jugadores. Si no se han recorrido todas las casillas, se
    # obtienen las posiciones actuales de las piezas y se dibujan en el tablero. Después de cada movimiento, se
    # actualiza la pantalla. El bucle se repite hasta que ambos jugadores hayan recorrido todas las casillas o se
    # cierre la ventana.
    # Inicializar Pygame
    pygame.init()
    # Establecer el tamaño de la ventana
    window_size = (400, 400)
    # Crear la ventana
    screen = pygame.display.set_mode(window_size)
    # Establecer el título de la ventana
    pygame.display.set_caption("Tablero")
    # Establecer el tamaño de las casillas del tablero
    board_size = 100
    # Crear una lista de colores para las casillas del tablero
    colors = [(0, 0, 0), (255, 0, 0)]
    # Dibujar el tablero
    for row in range(4):
        for col in range(4):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, (col * board_size, row * board_size, board_size, board_size))
    # Actualizar la pantalla
    pygame.display.flip()
    pieza1 = pygame.image.load(f"{fig1}.png")
    pieza2 = pygame.image.load(f"{fig2}.png")

    i = 0
    maximo = max(len(casillas1), len(casillas2))
    # Bucle del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # El usuario ha presionado el botón del mouse
                if i == maximo:
                    running = False
                if i < len(casillas1):
                    if i != 0:
                        colb = tablero[casillas1[i - 1]][0]
                        rowb = tablero[casillas1[i - 1]][1]
                        color = colors[(rowb + colb) % 2]
                        pygame.draw.rect(screen, color, (colb * board_size, rowb * board_size, board_size, board_size))
                    col = tablero[casillas1[i]][0]
                    row = tablero[casillas1[i]][1]
                    x1 = col * board_size
                    y1 = row * board_size
                    screen.blit(pieza1, (x1, y1))
                    pygame.display.flip()


            elif event.type == pygame.MOUSEBUTTONUP:
                # El usuario ha soltado el botón del mouse
                if i < len(casillas2):
                    if i != 0:
                        colb2 = tablero[casillas2[i - 1]][0]
                        rowb2 = tablero[casillas2[i - 1]][1]
                        color = colors[(rowb2 + colb2) % 2]
                        pygame.draw.rect(screen, color,
                                         (colb2 * board_size, rowb2 * board_size, board_size, board_size))
                    col2 = tablero[casillas2[i]][0]
                    row2 = tablero[casillas2[i]][1]
                    x2 = col2 * board_size
                    y2 = row2 * board_size
                    screen.blit(pieza2, (x2, y2))
                    pygame.display.flip()
                i = i + 1

