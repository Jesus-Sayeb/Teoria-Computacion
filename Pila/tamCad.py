# se importa la libreria a utilizar
import random as rnd

# al ser llamada este programa, esta funcion es la primera en ejecutarse
def generar_cadena():
    # se tiene una variable llamada cadena de tipo string
    cadena = ""
    # la variable tam se genera de manera aleatoria y sera un numero entero entre 1 y 10
    tam = rnd.randint(1, 10)
    # con un bucle for se itera desde 0 hasta el valor de tam
    for i in range(0,tam):
        num = rnd.randint(0,1) # numero aleatorio que solo sera 0 o 1
        cadena = cadena + str(num) # se concatena al string cadena el numero generado de forma aleatoria
    return cadena
