import random as rnd

def par(palindromo, opc):
    if opc == 0: # si la variable opc toma el valor 0 entonces P se reemplaza por un vacio
        palindromo = palindromo.replace("P","") # es reemplazada
        regla = reglas_prod[0] # la variable regla toma la posicion 0 de nuestro arreglo de reglas
    if opc == 1: # si la variable opc toma el valor 1 entonces P sera reemplazado por 0P0
        palindromo = palindromo.replace("P","0P0") # se hace el reemplazo
        regla = reglas_prod[3] # la regla toma el valor de de la posicion 3 del arreglo
    if opc == 2: # si opc toma el valor de 2
        palindromo = palindromo.replace("P","1P1") # se reemplaza P por 1P1
        regla = reglas_prod[4] # regla toma el valor de la posicion 4
    return palindromo, regla # se retorna el valor que tomo palindromo y regla

def impar(palindromo, opc):
    # las opcines aleatorias de 0 o 1 son para generar el ultimo digito del palindromo impar
    if opc == 0:
        palindromo = palindromo.replace("P","0")
        regla = reglas_prod[1]
    if opc == 1:
        palindromo = palindromo.replace("P","1")
        regla = reglas_prod[2]
    # la opcion aleatoria de 2 o 3 es para generar los digitos del tamañano del alindromo -1 / 2
    if opc == 2:
        palindromo = palindromo.replace("P","0P0")
        regla = reglas_prod[3]
    if opc == 3:
        palindromo = palindromo.replace("P","1P1")
        regla = reglas_prod[4]
    return palindromo,regla

def validacion_par(tam):
    res = tam%2
    if res == 0:
        return True
    if res == 1:
        return False

if __name__ == "__main__":
    sel = int(input("Desea ejecutar el programa de forma \n 1 = manual \n 2 = automatico: \n" ))
    if sel == 1:
        long = int(input("Ingrese longitud de palindromo: "))
    if sel == 2:
        long = rnd.randint(0, 100000)
        print(f"Longitud palindromo generado: {long}")

    reglas_prod = ["(1) P -> e", "(2) P -> 0", "(3) P -> 1", "(4) P -> 0P0", "(5) P -> 1P1"]
    palindromo = "P"
    file = open("palindromo.txt","w")
    #print(palindromo)
    #file.write(f"{palindromo}\a")
    if validacion_par(long): # mandamos a llamar a la funcion para validar si el tamaño del palindromo es par o impar
        for i in range(0,int(long/2)): # hacemos un recorrido desde 0 hasta la mitad del tamaño del palindromo
            opc = rnd.randint(1, 2) # se genera un numero aleatorio ya sea 1 o 2
            palindromo, regla = par(palindromo, opc) # las variables palindromo y regla tomaran los valores
            # que regrese la funcion par la cual recibe palindromo y opc como parametros
            print(regla)
            file.write(f"{regla}\n")
            print(palindromo)
            file.write(f"{palindromo}\n")
        # acabando el ciclo for por default se manda un valor cero por default para vaciar la variable palindromo
        palindromo, regla = par(palindromo, 0)
        print(regla) # se imprime la regla que se uso
        file.write(f"{regla}\n") # se escribe en el txt la regla que se uso
        print(palindromo) # el palindromo generado de forma aleatoria se imprime en pantalla
        file.write(f"{palindromo}\n") # el palindromo generado se escribe en el txt
        print(f"Palindromo final: {palindromo}") # el palindromo final, es impreso en pantalla
        file.write(f"Palindromo final: {palindromo}") # el palindromo final se escribe en el txt
    else:
        for i in range(0,int((long-1)/2)): # se hace un recorrido de 0 hasta la mitad menos 1 del tamaño de la cadena
            opc = rnd.randint(2, 3) # se genera un numero aleatorio ya sea 2 o 3
            palindromo, regla = impar(palindromo, opc) # palindromo y regla van a tomar los valores que regrese la
            # funcion impar
            print(regla) # se imprime en pantalla que regla se utiliza
            file.write(f"{regla}\n") # se escribe en el documento la regla
            print(palindromo) # el palindro generado aleatoriamente se imprime en pantalla
            file.write(f"{palindromo}\n") # se escribe en el txt el palindromo generado hasta el momento
        opcf = rnd.randint(0,1) # se genera un numero aleatorio ya sea 0 o 1
        palindromo, regla = impar(palindromo, opcf)
        print(regla) # se imprime la regla usada en este paso
        file.write(f"{regla}\n")
        print(palindromo)
        file.write(f"{palindromo}\n")

        print(f"Palindromo final: {palindromo}") # se imprime en pantalla el palindromo final
        file.write(f"Palindromo final: {palindromo}") # se escribe en el txt el palindromo final