# Importa el módulo random, que se utiliza más adelante para generar números aleatorios.
import random as rd

print("El proceso de la maquina sera de forma:")
modo = int(input((" 1 - > Manual\n 2 -> Automatica\n")))
cadena = '' # Inicializa una variable llamada "cadena" como una cadena de texto vacía
if modo == 1:
    cadena = input("Ingresa la cadena de tipo ' *|a*|b* ' ") # Solicita al usuario que ingrese una cadena de texto con un formato específico
else:
    a = rd.randint(1, 45) #Genera un número entero aleatorio en el rango [1, 45] y lo asigna a la variable "a".
    b = rd.randint(1, 46 - a) #Genera otro número entero aleatorio en el rango [1, 46 - a] y lo asigna a la variable "b"
    cadena = '*' + '|' * a + '*' + '|' * b + '*' # El número de asteriscos y barras verticales se determina a partir
    # de los valores generados aleatoriamente para "a" y "b".

print(f"La cadena generada es: '{cadena}' ")


class maqu_Turing():
    def __init__(self, cadena): # Define el método de inicialización de la clase. Recibe como parámetro la cadena
        # que se utilizará como entrada para la máquina.
        self.cadena = [i for i in cadena] # Convierte la cadena en una lista de caracteres y la asigna a la variable
        # "self.cadena".
        self.estado = '1'
        self.salida = ''
        self.historial = '' #  Inicializa la variable "self.historial" como una cadena de texto vacía.

# Define el método "fun_trans" que realiza las transiciones de la máquina de Turing.
    # Recibe como parámetro el caracter o simbolo actual de la cinta.
    def fun_trans(self, simb):
        if self.estado == '1':
            if simb == '*': # Verifica si el caracter actual es un asterisco.
                self.estado = '2' # Cambia el estado actual a '2'.
                return ('X', 1) # Retorna una tupla con el caracter a escribir en la cinta ('X') y el
                # desplazamiento del cabezal de lectura/escritura (1 indica moverse hacia la derecha).
        if self.estado == '2':
            if simb == '*':
                self.estado = '3'
                return ('*', 1)
            if simb == '|':
                self.estado = '2'
                return ('|', 1)
        if self.estado == '3':
            if simb == '*':
                self.estado = '4'
                return ('X', -1)
            if simb == '|':
                self.estado = '3'
                return ('|', 1)
        if self.estado == '4':
            if simb == '*':
                self.estado = '4'
                return ('*', -1)
            if simb == '|':
                self.estado = '5'
                return ('a', 1)
            if simb == 'X':
                self.estado = '7'
                return ('X', 1)
        if self.estado == '5':
            if simb == ' ':
                self.estado = '6'
                return ('|', -1)
            if simb == '*':
                self.estado = '5'
                return ('*', 1)
            if simb == '|':
                self.estado = '5'
                return ('|', 1)
            if simb == 'X':
                self.estado = '5'
                return ('X', 1)
        if self.estado == '6':
            if simb == '*':
                self.estado = '6'
                return ('*', -1)
            if simb == '|':
                self.estado = '6'
                return ('|', -1)
            if simb == 'a':
                self.estado = '4'
                return ('|', -1)
            if simb == 'X':
                self.estado = '6'
                return ('X', -1)
        if self.estado == '7':
            if simb == '*':
                self.estado = '8'
                return ('*', 1)
            if simb == '|':
                self.estado = '7'
                return ('|', 1)
        if self.estado == '8':
            if simb == ' ':
                self.estado = '9'
                return ('*', -1)
            if simb == '|':
                self.estado = '8'
                return ('|', 1)
            if simb == 'X':
                self.estado = '8'
                return ('*', 1)
        if self.estado == '9':
            if simb == '*':
                self.estado = '9'
                return ('*', -1)
            if simb == '|':
                self.estado = '9'
                return ('|', -1)
            if simb == 'X':
                self.estado = '0'
                return ('*', 0)
            # El programa sigue definiendo las transiciones de acuerdo a los diferentes estados y caracteres.

    def convertir(self):
        # es un método de la clase maqu_Turing que se encarga de convertir la lista de caracteres self.cadena en una
        # cadena de texto. A continuación, explicaré paso a paso su funcionamiento:
        cadena = ''
        # la función recorre cada elemento de la lista self.cadena y los concatena uno por uno para formar una cadena
        # de texto. Al finalizar, retorna la cadena resultante. Esencialmente, esta función convierte la lista de
        # caracteres en una cadena de texto legible.
        for i in self.cadena:
            cadena += i
        return cadena


    def es_archivo(self, guardarArchivo=False):
        if guardarArchivo:
            self.historial += '(q{}, {} )'.format(self.estado, self.convertir())
            archivo = open('hist_Tur.txt', mode='w', encoding='utf-8')
            archivo.write(self.historial)
            archivo.close()
        else:
            self.historial += '(q{}, {})\n'.format(self.estado, self.convertir())

    def reajuste(self):
        if self.cadena[-1] != ' ':
            self.cadena.append(' ')

    def evaluar(self):
        lector = 0
        # ejecuta la máquina de Turing utilizando la cadena de entrada. Itera sobre la cinta, realiza transiciones
        # de acuerdo a los estados y caracteres leídos, actualiza la cinta, mueve el cabezal de lectura/escritura y
        # registra el historial de la ejecución. Al finalizar, almacena la salida generada por la máquina en self.salida.
        while self.estado != '0':
            self.es_archivo()
            valor, direccion = self.fun_trans(self.cadena[lector])
            self.cadena[lector] = valor
            lector += direccion
            self.reajuste()
        self.es_archivo(guardarArchivo=True)
        self.salida = self.convertir()


maquina = maqu_Turing(cadena)
maquina.evaluar()

print('Salida de la Maquina: ' + maquina.salida)