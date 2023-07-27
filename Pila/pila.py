# importamos las librerias a utilizar.
# en este caso las librerias provienen de otros archivos python
import tamCad as aux
import animacion as pb

# creamos la funcion principal
if __name__ == "__main__":
    opc = int(input("1 -> Cadena generada automáticamente \n2- > Ingresada desde teclado \n"))
    # si se selecciona la primer opcion se manda a llamar a "aux"
    if opc == 1:
        cadena = aux.generar_cadena()
        # se imprime la cadena generada automaticamente
        print(cadena)

    if opc == 2:
        # variable cadena donde se almacena la cadena introducida por el teclado
        cadena = input("Ingrese la cadena en binario\n")
    # variable pila de tipo string
    pila = "Z0"
    estados = ["q1","q2","f"]
    select = 0
    actual = estados[0]
    file = open("Pila Teclado.txt", "w")
    # se escribe en un .txt una "inicializacion" donde aun no existe ningun cero en la pila
    file.write(f"       ID's\n")
    print(f"           ID's")
    # Este for itera desde cero hasta el final de la cadena el cual es su tamaño
    for i in range(0, len(cadena)):
    # se codifican los casos posibles que puede haber, segun la cadena ingresada
    # si select llega a tomar el valor de 1 se escribe en el txt que se comienza a trabajar los bloques con 1's
        if select == 1:
            # file.write(f"\nd(q,{cadena[i]}, X) = [(p,e)]\a")
            # print(f"\nd(q,{cadena[i]}, X) = [(p,e)]\a")
            file.write(f"\n los 0's que entraron ahora salen con los 1's\n")
            print(f"\n los 0's que entraron ahora salen con los 1's\n")
            w = " "
            t = int(len(cadena)/2)
            for k in range(t):
                w = w+"X"
            # print(f"d(p,1, X) = [(p,{w}Z0)]")
            # la variable actual, toma el valor de la posicion 1 en la cadena estados en este caso "p"
            actual = estados[1]
        if len(cadena) == 1:
            # si la cadena tiene un solo elemento, por defaut no es aceptada
            file.write("La cadena no pertenece al lenguaje")
            print("La cadena no pertenece al lenguaje")
            break
        # si la cadena en la posicion i es igual a 0 y al mismo tiempo la variable actual es igual a q
        # entonces se agrega una X a la pila
        if int(cadena[i]) == 0 and actual == "q1":
            pila = "X" + pila
        # solo se ejecuta si encuentra un 1 y al mismo tiempo esta en el estado p
        elif int(cadena[i]) == 1 and actual == "q2":
            # se elimina el primer elemento de la pila porque solo toma el segundo elemento y se actualiza
            pila = pila[1:]
        # si ninguna de las condicionales anteriores se cumple entonces significa que la cadena no pertenece al lenguaje
        else:
            file.write("La cadena no pertenece al lenguaje")
            # se escribe en el txt y en pantalla para que el usuario tenga en cuenta que la cadena no pertenece al lenguaje
            print("La cadena no pertenece al lenguaje")
            break
        # si i es menor al tamaño de la cadena ingresada - 1 entramos a un if anidado
        if i < len(cadena)-1:
            # si cadena en la posicion i + 1 es igual a 1 el selector pasa a tomar el valor 1
            if cadena[i+1] == "1":
                # el select aumenta cuando antes valia cero ahora vale 1 y pasa al estado p
                # lo que significa que vamos a empezar a trabajar con los 1's
                select+=1
        # esta parte esta en los 0's por lo que escribe en el txt y muestra en pantalla
        # la parte de la pila que corresponde al "conteo de 0's"
        file.write(f"({actual},{cadena[i]}) = [({actual},{pila})]\n")
        print(f"({actual},{cadena[i]}) = [({actual},{pila})]")
        # si i es igual al tamaño de la cadena -1
        # significa que se ha llegado al final de la pila osea que ahora esta vacia
        if i == len(cadena)-1:
            # se escribe en el txt y en pantalla que la pila ahora esta vacia
            file.write(f"\n(empty) = [(final,{pila})]\n")
            print(f"\n(empty) = [(final,{pila})]")
    # afuera del for hacemos la siguiente validacion
    # si nos quedamos con el id Z0 y select mayor a cero se
    # imprime y escribe que la cadena si pertenece al lenguaje
    if pila == "Z0" and select>0:
        file.write(f"La cadena {cadena} pertenece al lenguaje")
        print(f"La cadena {cadena} pertenece al lenguaje")
    # si la validacion anterior no se cumple, significa que la cadena no pertenece al lenguaje
    else:
        file.write("La cadena no pertenece al lenguaje")
        print("La cadena no pertenece al lenguaje")
    file.close()
    # si la cadena tiene menos de 10 elementos
    # se manda a llamar a la funcion para graficar
    if len(cadena) <= 10:
        pb.dib_pila(cadena)
