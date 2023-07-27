import tablero as tab
import num_jug as mod
import rutas_jugar as jug
import crear_tablero as dib_tab
import crear_arb as arbol

if __name__ == "__main__":
    modo = int(input("El juego sera de forma:\n1 -> automatico(todo)\n2 -> manual "))
    if modo == 1:
        num_jug = mod.num_jug_rand()
        print(f"El numero generado de jugadores es:\n{num_jug}")
        if num_jug == 1:
            ruta = mod.ruta_random()
            print(f"La ruta seleccionada es:\n{ruta}")
            tab.guardar_rutas(ruta, 0, 1)
            casilas_gan = jug.obtener_rutas_ganadoras(f"rutas_ganadoras_jugador1.txt")
            if not casilas_gan:
                print("No existe ruta que llegue al objetivo")
            else:
                print(f"La jugada que gana la partida es: \n{casilas_gan}")
                dib_tab.un_jugador(casilas_gan)
                arbol.arbol(ruta, True)
        if num_jug == 2:
            casilas_gan = []
            turnos = mod.orden_turnos()
            print(f"Iniciara el jugador numero: {turnos[0][0]}")
            for turno in turnos:
                datos = []
                ruta = mod.ruta_random()
                print(f"La ruta seleccionada para el jugador {turno[0]}:\n{ruta}")
                tab.guardar_rutas(ruta, turno[1], turno[0])
                datos.append(turno[0])
                datos.append(jug.obtener_rutas_ganadoras(f"rutas_ganadoras_jugador{turno[0]}.txt"))
                datos.append(ruta)
                casilas_gan.append(datos)
            if not casilas_gan[0][1] and not casilas_gan[1][1]:
                print("Ningún jugador gano la partida")
            elif not casilas_gan[0][1] and casilas_gan[1][1]:
                print(f"El jugador {casilas_gan[1][0]} gano el juego")
            elif not casilas_gan[1][1] and casilas_gan[0][1]:
                print(f"El jugador {casilas_gan[0][0]} gano el juego")
            else:
                ruta1, ruta2 = jug.reconfiguracion_rutas(casilas_gan[0][1], casilas_gan[1][1])
                casilas_gan[0][1] = ruta1
                casilas_gan[1][1] = ruta2
                ganador = jug.encontrar_jugadorGanador(casilas_gan[0], casilas_gan[1])
                if casilas_gan[0][0] == 1:
                    dib_tab.dos_jugadores(casilas_gan[0][1], casilas_gan[1][1], "peon", "pieza3")
                elif casilas_gan[0][0] == 2:
                    dib_tab.dos_jugadores(casilas_gan[0][1], casilas_gan[1][1], "pieza3", "peon")
                print(f"El jugador {ganador} gano el juego")
            if casilas_gan[0][0] == 1:
                arbol.arbol(casilas_gan[0][2], True)
                arbol.arbol(casilas_gan[1][2], False)
            elif casilas_gan[0][0] == 2:
                arbol.arbol(casilas_gan[0][2], False)
                arbol.arbol(casilas_gan[1][2], True)

    if modo == 2:
        num_jug = int(input("Ingresa el numero de jugadores (Maximo 2): "))
        if num_jug == 1:
            tipo_ruta = int(input("La ruta a seguir se generar de manera:\n1 -> manual\n2 -> automatica: "))
            if tipo_ruta == 1:
                ruta = input("Ingrese la ruta a seguir: ")
            if tipo_ruta == 2:
                ruta = mod.ruta_random()
            print(f"La ruta seleccionada es:\n{ruta}")
            tab.guardar_rutas(ruta, 0, 1)
            casilas_gan = jug.obtener_rutas_ganadoras(f"rutas_ganadoras_jugador1.txt")
            if not casilas_gan:
                print("No hay ruta ganadora")
            else:
                print(f"La jugada que llega al objetivo : \n{casilas_gan}")
                dib_tab.un_jugador(casilas_gan)
                arbol.arbol(ruta, True)
        if num_jug == 2:
            casilas_gan = []
            turnos = mod.orden_turnos()
            print(f"Inicia jugador {turnos[0][0]}")
            tipo_ruta = int(input("La ruta a seguir se generar de manera:\n1 -> manual\n2 -> automatica: "))
            for turno in turnos:
                datos = []
                if tipo_ruta == 1:
                    ruta = input(f"Ingrese la ruta a seguir pot el jugador {turno[0]}: ")
                if tipo_ruta == 2:
                    ruta = mod.ruta_random()

                print(f"Ruta seleccionada jugador {turno[0]}:\n{ruta}")
                tab.guardar_rutas(ruta, turno[1], turno[0])
                datos.append(turno[0])
                datos.append(jug.obtener_rutas_ganadoras(f"rutas_ganadoras_jugador{turno[0]}.txt"))
                datos.append(ruta)
                casilas_gan.append(datos)
            if not casilas_gan[0][1] and not casilas_gan[1][1]:
                print("Ningún jugador ha ganado :c")
            elif not casilas_gan[0][1] and casilas_gan[1][1]:
                print(f"El jugador {casilas_gan[1][0]} gano el juego")
            elif not casilas_gan[1][1] and casilas_gan[0][1]:
                print(f"El jugador {casilas_gan[0][0]} gano el juego")
            else:
                ruta1, ruta2 = jug.reconfiguracion_rutas(casilas_gan[0][1], casilas_gan[1][1])
                casilas_gan[0][1] = ruta1
                casilas_gan[1][1] = ruta2
                ganador = jug.encontrar_jugadorGanador(casilas_gan[0], casilas_gan[1])
                if casilas_gan[0][0] == 1:
                    dib_tab.dos_jugadores(casilas_gan[0][1], casilas_gan[1][1], "peon", "pieza3")
                elif casilas_gan[0][0] == 2:
                    dib_tab.dos_jugadores(casilas_gan[0][1], casilas_gan[1][1], "pieza3", "peon")
                print(f"El jugador {ganador} gano el juego")
            if casilas_gan[0][0] == 1:
                arbol.arbol(casilas_gan[0][2], True)
                arbol.arbol(casilas_gan[1][2], False)
            elif casilas_gan[0][0] == 2:
                arbol.arbol(casilas_gan[0][2], False)
                arbol.arbol(casilas_gan[1][2], True)