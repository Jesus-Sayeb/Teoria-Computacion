# se importan los módulos pygame y threading
import pygame
import threading

def animacion():
    # función llamada animacion(), que será ejecutada en un hilo separado.

    # algunas variables, como el color de fondo, los colores de los elementos, el tamaño de la pantalla y el
    # tamaño de un rectángulo de la ventana principal.
    fondo = 255, 133, 107
    ne = (0, 0, 0)
    posi = (78, 205, 74)
    tam = (1000, 400)

    rectangulo = (int((tam[0] / 12) * 10), int(tam[1] / 5))

    datos = []
    # Se abre un archivo llamado "hist_Tur.txt" en modo de lectura y se leen todas las líneas del archivo.
    # Cada línea se procesa para eliminar los caracteres no deseados y se guarda en una lista llamada datos.
    archivo = open('hist_Tur.txt', mode='r', encoding='utf-8')
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        dato = linea.replace('\n', '').replace('(', '').replace(')', '').replace(' ', '')
        datos.append(dato.split(','))
    # Se inicializa el módulo Pygame, se crea una ventana de visualización con el tamaño especificado y se establece
    # el título de la ventana.
    pygame.init()
    pantalla = pygame.display.set_mode(tam)
    pygame.display.set_caption("Animacion Maquina de Turing")


    fuente = pygame.font.Font(None, 30)
    fuente_cadena = pygame.freetype.Font(None, 30)

    ejecucion = True
    while ejecucion:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecucion = False


        pantalla.fill(fondo)

        for iteracion in datos:

            pantalla.fill(fondo)
            estado_iteracion = iteracion[0]
            cadena_iteracion = iteracion[1]
            pygame.draw.rect(pantalla, ne, (tam[0] / 12, (tam[1] / 5) * 3, rectangulo[0], rectangulo[1]), 3)

            ancho_division = rectangulo[0] // 10
            for i in range(1, 10):
                x = (ancho_division * i) + tam[0] / 12
                pygame.draw.line(pantalla, ne, (x, (tam[1] / 5) * 3), (x, (tam[1] / 5) * 4), width=3)

            x_texto_division = tam[0] // 24
            estado = 0
            for j in range(2, 21, 2):
                estado_texto = 'q' + str(estado)
                if estado_texto == estado_iteracion:
                    x = x_texto_division * j + x_texto_division
                    y = (tam[1] / 5) * 3 + tam[1] / 10
                    flecha_puntos = [(x - 30, y), (x, y - 30), (x + 30, y), (x, y + 30)]
                    pygame.draw.polygon(pantalla, posi, flecha_puntos)

                texto = fuente.render(estado_texto, True, ne)
                pantalla.blit(texto,
                              (x_texto_division * j + x_texto_division - 15, (tam[1] / 5) * 3 + tam[1] / 10 - 15))
                estado += 1


            texto_superficie, texto_rectangulo = fuente_cadena.render(cadena_iteracion, ne)

            texto_rectangulo.center = (tam[0] // 2, tam[1] // 5 * 1 + tam[1] // 10)

            pantalla.blit(texto_superficie, texto_rectangulo)

            pygame.display.flip()

            if estado_iteracion == 'q0':
                pygame.time.wait(3000)
            else:
                pygame.time.wait(50)

    pygame.quit()

if __name__ == '__main__':
    # Finalmente, se verifica si el código se está ejecutando como un script principal y no como un módulo importado.
    # En ese caso, se crea un hilo utilizando la función threading.Thread(), se le pasa la función animacion como
    # objetivo y se inicia y espera a que termine el hilo de Pygame.
    pygame_thread = threading.Thread(target=animacion)
    pygame_thread.start()
    pygame_thread.join()