import tkinter as tk
import time

def dib_pila(cadena):

#Esta función toma un argumento cadena que representa una cadena de entrada a ser procesada por la simulación.
# Crea una ventana raíz (root) y un lienzo (canvas) dentro de la ventana con dimensiones de 600x600 píxeles.
# Crea una lista salida_pila que inicialmente contiene el símbolo "Z0" que representa el estado inicial de la pila.
# Establece algunas variables de control, como tam_an, bandera, bandera2 y estados, que se utilizan durante la simulación.
# Dibuja un rectángulo y un texto en el lienzo para representar el estado inicial "q1".

    root = tk.Tk()
    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()
    salida_pila = ["Z0"]
    tam_an = 0
    bandera = 0
    bandera2 = 0
    estados = ["q1","q2","f"]
    actual = estados[0]
    canvas.create_rectangle(250, 250, 350, 350)
    canvas.create_text(300, 300, text="q1", fill="blue", font=("Arial", 20, "bold"), tags="q1")


    for i in range(0,len(cadena)+1):

        """
El bucle principal itera a través de cada caracter de la cadena de entrada y realiza las siguientes acciones:
Comprueba si la cadena no pertenece al lenguaje y muestra un mensaje de error en el lienzo si se cumple la condición.
Comprueba si el caracter actual es "1" y actualiza el estado actual a "q2" si es así.
Actualiza el lienzo eliminando el texto del estado anterior y dibuja el nuevo estado actual.
Actualiza el lienzo eliminando el texto y los elementos de la pila generados en la iteración anterior.
Dibuja el texto restante de la cadena en el lienzo.
Dibuja los elementos de la pila en el lienzo.
Realiza pausas de 8 segundos para visualizar el progreso de la simulación.
        """
        if (len(cadena) == 1 and cadena[i]=="1") or len(salida_pila) == 0:
            canvas.create_text(300, 100, text="No pertenece al lenguaje", fill="red", font=("Arial", 15, "bold"))
            break
        if len(cadena) >i:
            if cadena[i] == "1":
                bandera2 += 1
                actual = estados[1]
        if bandera == 1:
            canvas.delete("q1")
            canvas.create_text(300, 300, text="q2", fill="blue", font=("Arial", 20, "bold"), tags="q2")
        if i  == len(cadena):
                canvas.delete("q2")
                canvas.create_text(300, 300, text="f", fill="blue", font=("Arial", 20, "bold"), tags="q2")

        if i > 0:
            canvas.delete(f"texto{i-1}")
            canvas.update()
            for m in range(0,tam_an):
                canvas.delete(f"salida{m}")
                canvas.update()

        canvas.create_text(300, 230, text=cadena[i:], fill="green", font=("Arial", 15, "bold"), tags=f"texto{i}")
        for j in range(0,len(salida_pila)):
            canvas.create_text(300, 370+((j)*20), text=salida_pila[-(j+1)], fill="green", font=("Arial", 15, "bold"), tags = f"salida{j}")
            canvas.update()
            
        if i < len(cadena):

            tam_an =  len(salida_pila)
            
            if cadena[i] == "0" and actual == "q1":

                cad_pila = "X"
                salida_pila.append(cad_pila)

            elif cadena[i] == "1" and len(salida_pila)>0 and actual == "q2":
                bandera += 1
                salida_pila.pop(-1)
            else:
                canvas.create_text(300, 100, text="Cadena no pertenece al lenguaje", fill="red", font=("Arial", 15, "bold"))
                break 

        canvas.update()
        time.sleep(8)
    if len(salida_pila) == 0:
        canvas.create_text(300, 100, text="Cadena no pertenece al lenguaje", fill="red", font=("Arial", 15, "bold"))
    elif salida_pila[0] == "Z0" and len(salida_pila) == 1 and bandera>0:
        canvas.create_text(300, 100, text="Cadena pertenece al lenguaje", fill="green", font=("Arial", 15, "bold"))
    else:
        canvas.create_text(300, 100, text="Cadena no pertenece al lenguaje", fill="red", font=("Arial", 15, "bold"))
    canvas.update()
    root.mainloop()