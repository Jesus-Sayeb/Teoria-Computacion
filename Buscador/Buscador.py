import pandas as pd
import graphviz
import time

#Se prepara texto.txt para leer
file = open("texto.txt", "r")

#Se prepara historia.txt para escribir sobre él
historia = open("historia.txt", "w")
txt = file.read()

#Se genera un arreglo vacío por cada palabra
web = [] 
webpage = [] 
website = [] 
webmaster = [] 
site = [] 
ebay = [] 
page = []

#Se genera un diccionario con cada nodo y sus conexiones 
estados = {
    1: {1, 2, 19, 23, 27},
    2: {2, 3, 1},
    3: {3, 4, 1},
    4: {4, 5, 9, 13, 1}, #web
    5: {5, 6, 1},
    6: {6, 7, 1},
    7: {7, 8, 1},
    8: {8, 1}, #webpage
    9: {9, 10, 1},
    10: {10, 11, 1},
    11: {11, 12, 1},
    12: {12 ,1}, #website
    13: {13, 14, 1},
    14: {14, 15, 1},
    15: {15, 16, 1},
    16: {16, 17, 1},
    17: {17, 18, 1},
    18: {18, 1}, #webmaster
    19: {19, 20, 1},
    20: {20, 21, 1},
    21: {21, 22, 1},
    22: {22, 1}, #ebay
    23: {23, 24, 1},
    24: {24, 25, 1},
    25: {25, 26, 1},
    26: {26, 1}, #page
    27: {27, 28, 1},
    28: {28, 29, 1},
    29: {29, 30, 1},
    30: {30, 1}
}

#Función principal del programa
def busca(txt, estados):
    #Se inicia un bucle por cada simb del texto, pasado a minúsculas y
    #se inicializan los valores de estado y lugar
    estado = 1
    lugar = 0
    for letra in txt.lower():
        #Dentro de historia se escribe el historial paso por paso
        historia.write(f"Estado actual: {estado}\tLetra Recibida: {letra}\n")
        #Se inicializa el lugar 1 o el primer simb y se va sumando 1 por cada operación
        lugar += 1
        #Las funciones if que deciden si la palabra es la correcta, basadas en los grafos
        if (estado == 1):
            if (letra == "w"):
                estado = 2
            elif (letra == "e"):
                estado = 19
            elif (letra == "p"):
                estado = 23
            elif (letra == "s"):
                estado = 27
            else:
                estado = 1
            continue

        if (estado == 2):
            if (letra == "w"):
                estado = 2
            elif (letra == "e"):
                estado = 3
            else:
                estado = 1
            continue

        if (estado == 3):
            if (letra == "e"):
                estado = 3
            elif(letra == "b"):
                estado = 4
            else:
                estado = 1
            continue

        if (estado == 4):
            if (letra == "b"):
                estado = 4
            elif(letra == "p"):
                estado = 5
            elif(letra == "s"):
                estado = 9
            elif(letra == "b"):
                estado = 13
            #En caso de encontrar un match, añaden al arreglo particular la posicion en la que se encontró
            #la palabra, en este caso es:    
            #web
            else:
                web.append(lugar-3)
                estado = 1
            continue

        if (estado == 5):
            if (letra == "p"):
                estado = 5
            elif(letra == "a"):
                estado = 6
            else:
                estado = 1
            continue

        if (estado == 6):
            if (letra == "a"):
                estado = 6
            elif(letra == "g"):
                estado = 7
            else:
                estado = 1
            continue

        if (estado == 7):
            if (letra == "g"):
                estado = 7
            #webpage
            elif(letra == "e"):
                webpage.append(lugar-7)
                estado = 8
            else:
                estado = 1
            continue

        if (estado == 8):
            if (letra == "e"):
                estado = 8
            else:
                estado = 1
            continue

        if (estado == 9):
            if (letra == "s"):
                estado = 9
            elif(letra == "i"):
                estado = 10
            else:
                estado = 1
            continue

        if (estado == 10):
            if (letra == "i"):
                estado = 10
            elif(letra == "t"):
                estado = 11
            else:
                estado = 1
            continue

        if (estado == 11):
            if (letra == "t"):
                estado = 11
            #website
            elif(letra == "e"):
                website.append(lugar-7)
                estado = 12
            else:
                estado = 1
            continue

        if (estado == 12):
            if (letra == "e"):
                estado = 12
            else:
                estado = 1
            continue

        if (estado == 13):
            if (letra == "b"):
                estado = 13
            elif(letra == "a"):
                estado = 14
            else:
                estado = 1
            continue

        if (estado == 14):
            if (letra == "a"):
                estado = 14
            elif(letra == "s"):
                estado = 15
            else:
                estado = 1
            continue

        if (estado == 15):
            if (letra == "s"):
                estado = 15
            elif(letra == "t"):
                estado = 16
            else:
                estado = 1
            continue

        if (estado == 16):
            if (letra == "t"):
                estado = 16
            elif(letra == "e"):
                estado = 17
            else:
                estado = 1
            continue

        if (estado == 17):
            if (letra == "e"):
                estado = 17
            #webmaster
            elif(letra == "r"):
                webmaster.append(lugar-9)
                estado = 18
            else:
                estado = 1
            continue

        if (estado == 18):
            if (letra == "r"):
                estado = 18
            else:
                estado = 1
            continue

        if (estado == 19):
            if (letra == "e"):
                estado = 19
            elif(letra == "b"):
                estado = 20
            else:
                estado = 1
            continue

        if (estado == 20):
            if (letra == "b"):
                estado = 20
            elif(letra == "a"):
                estado = 21
            else:
                estado = 1
            continue

        if (estado == 21):
            if (letra == "a"):
                estado = 21
            #ebay
            elif(letra == "y"):
                ebay.append(lugar-4)
                estado = 22
            else:
                estado = 1
            continue

        if (estado == 22): 
            if (letra == "y"):
                estado = 22
            else:
                estado = 1
            continue

        if (estado == 23):
            if (letra == "p"):
                estado = 23
            elif(letra == "a"):
                estado = 24
            else:
                estado = 1
            continue

        if (estado == 24):
            if (letra == "a"):
                estado = 24
            elif(letra == "g"):
                estado = 25
            else:
                estado = 1
            continue

        if (estado == 25): 
            if (letra == "g"):
                estado = 25
            #page
            elif(letra == "e"):
                page.append(lugar-4)
                estado = 26
            else:
                estado = 1
            continue

        if (estado == 26): 
            if (letra == "e"):
                estado = 26
            else:
                estado = 1
            continue
    
        if (estado == 27):
            if (letra == "s"):
                estado = 27
            elif(letra == "i"):
                estado = 28
            else:
                estado = 1
            continue

        if (estado == 28):
            if (letra == "i"):
                estado = 28
            elif(letra == "t"):
                estado = 29
            else:
                estado = 1
            continue

        if (estado == 29):
            if (letra == "t"):
                estado = 29
            #site
            elif(letra == "e"):
                site.append(lugar-4)
                estado = 30
            else:
                estado = 1
            continue

        if (estado == 30):
            if (letra == "e"):
                estado = 30
            else:
                estado = 1
            continue

    #Se "cierran" o dejan de escribir y leer los archivos de texto usados
    file.close()
    historia.close()

    #Se genera otro diccionario con los datos obtenidos
    datos = {
        "Palabra": ["web","webpage","website","webmaster","ebay","page","site"],
        "Total": [len(web),len(webpage),len(website),len(webmaster),len(ebay),len(page),len(site)],
        "Posción": [web, webpage, website, webmaster, ebay, page, site]
    }
    #Se convierte el diccionario a dataframe y se pasa a .xlsx
    frecuencia = pd.DataFrame(datos)
    frecuencia.to_excel("Frecuencia_palabras.xlsx")

    #Se genera un dataframe con el primer diccionario y se convierte a .xlsx
    con = pd.DataFrame(estados.items(), columns=['Estado', 'Conexiones'])
    con.to_excel("Estados.xlsx")

#Función de graficado de DataFrames como grafos mediante graphviz
def grafica(estadosConectados):
    g = graphviz.Digraph()

    for key, value in estadosConectados.items():
        g.node(str(key))
        for v in value:
            g.edge(str(key), str(v))
    g.render(format='png', filename=f'grafo_cambiosEstados')

print("Bienvenido al programa Buscador")
print("Se buscarán las siguientes palabras en el texto:")
print("Web\nWebpage\nWebsite\nWebmaster\nSite\nEbay\nPage")
print("Buscando...")
busca(txt, estados)
time.sleep(3)
print("Busqueda terminada")
#Dependiendo de la respuesta, el programa graficará o no el grafo del autómata
d = input("¿Desea generar una imagen del grafo? S/N\n")
if(d == "s"):
    #Se grafica el diccionario de estados resultante mediante la función grafica 
    grafica(estados)
    print("Grafo generado")
print("Programa finalizado c:")
