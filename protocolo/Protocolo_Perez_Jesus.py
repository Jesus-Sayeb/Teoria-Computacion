import random
from graphics import *

estado = 0
def q0(number):
    global estado

    if number == 0:
        estado = 1
    if number == 1:
        estado = 3
def q1(number):
    global estado
    if number == 0:
        estado = 0
    if number == 1:
        estado = 2
def q2(number):
    global estado

    if number == 0:
        estado = 3
    if number == 1:
        estado = 1
def q3(number):
    global estado

    if number == 0:
        estado = 2
    if number == 1:
        estado = 0

def validadorestados(number): #recibe un numero int ya sea 0 o 1
    global estado # seguimos haciendo uso de la variable global estado
    switch = {
        0 :q0,
        1 :q1,
        2 :q2,
        3 :q3,
    }
    func = switch.get(estado, lambda : None)
    return func(number)

def automata(string): # esta funcion recibe cadena por cadena segun el ciclo for
    global estado # variable global valida para a fuera de la funcion
    estado = 0 # igualamos el estado en el estado de inicio/aceptacion
    for number in string:  # recorremos la cadena que le pasamos a la funcion
        validadorestados(int(number)) #y pasamos cada iteacion a la funcion
        # osea que aqui el str lo convertimos a un int
    return estado == 0 # solo regresamo el estado si es igual a cero osea que llego al estado de aceptacion/inicio


def gencadenasbinarias(contenido, num_cadenas, txt): #recibe el
    # Generador de cadenas
    def generarandom(n):
        randnum = "" # string vacio para almacenar una cadena de 0's y 1's aleatorios

        for j in range(n): # ciclo que se detiene cuando cumple el tamaño que debe tener cada cadena
            num = str(random.randint(0, 1)) # se generar "a" numeros 0's y 1's que conforman 1 cadena, pero de tipo string
            randnum += num # se concatena cada numero 0 o 1 hasta cumplir el tamaño de la cadena
        return randnum # se regresa la cadena aleatoria
   # stringsN = ""
    for i in range(num_cadenas): # ciclo que se ejecuta hasta cumplir el numero de cadenas deseadas
        stringsN = generarandom(contenido) + ", " # durante el ciclo se manda a llamar a la funcion, y el valor que
        # retorna se concatena en una lista separada por , cumpliendo el numero de cadenas aleatorias
        escrituracadenas(txt, stringsN) # durante el mismo for se le pasa informacion a la funcion addtext


def validarcad(txt): # se recibe el archivo txt
    text = leertxt(txt) # se manada a llamar a la funcion leertxt y se le pasa el archivo
    text = text.split(", ") # la informacion se separa cada que se encuentra una ,
    text = text[:-1] # quitamos la ultima ,
    aceptadas = "1_rechazadas.txt"  # se le da nombre a donde se almacenal las cadenas rechazadas
    rechazadas = "2_aceptadas.txt"# se le da nombre a donde se van a almacenar las cadenas aceptadas

    for string in text: # hacemos un recorrido del txt donde estan todas las cadenas generadas
        if (automata(string)): # mandamos a llamar a la funcion automata y le pasamos el valor que haya tomado la cadena en dicha iteracion
            escrituracadenas(aceptadas, string + ", ") # si estado regresado es cero se escribe en cadenas aceptadas
        else:
            escrituracadenas(rechazadas, string + ", ") # si no es cero se ira a cadenas aceptadas

    escrituracadenas(aceptadas, "\n") # se escibe y hacemos un salto de linea por cada vez que se ejecute
    escrituracadenas(rechazadas, "\n")


def leertxt(file): #recibe el archivo txt
    with open(file, 'r', encoding="utf-8") as archivo: # lee el archivo
        return archivo.read() # regresa la informacion que contiene dicho archivo

def escrituracadenas(file, text): # recibe un nombre de archivo y las cadenas 1 por 1
    file = open(file,"a") # con "a" se escribe una detras de otra
    file.write(text) # se escriben en un documento
    file.close # se cierra el documento


def main():
    while random.randint(0,1) == 1:
        print("\n PROGRAMA ENCENDIDO")
        gencadenasbinarias(8, 6, "CadenasTotales.txt") # primero se manda a llamar esta funcion y se le pasan
        print("Generando cadenas...")
        time.sleep(3)
        print("¡Cadenas generadas!")
        print("Procede a validar cadenas...")
        validarcad("CadenasTotales.txt") # Teniendo el archivo txt lo mandamos a la funcion de evaluacion
        time.sleep(3)
        print("Cadenas evaluadas")
        print("se generaron los txt correspondientes.")
        print("\n")
        time.sleep(3)
    selec = input("Desea graficar el protocolo completo? s/a \a")
    if selec == "s":
        from GraficarAFD import dibujoo
        dibujoo()
        sys.exit(0)
    else:
        print("Programa Apagado")
main()
