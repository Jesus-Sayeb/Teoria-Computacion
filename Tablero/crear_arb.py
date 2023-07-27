import graphviz
#import pygraphviz as pgv

tablero = {
    0: {'b': [5], 'r': [1,4]},
    1: {'b': [0,2,5], 'r': [4,6]},
    2: {'b': [5,7], 'r':[1,3,6]},
    3: {'b': [2,7], 'r': [6]},
    4: {'b': [0,5,8], 'r': [1,9]},
    5: {'b': [0,2,8,10], 'r':[1,4,6,9]},
    6: {'b': [2,5,7,10], 'r':[1,3,9,11]},
    7: {'b': [2,10], 'r':[3,6,11]},
    8: {'b': [5,13], 'r': [4,9,12]},
    9: {'b': [5,8,10,13], 'r': [4,6,12,14]},
    10: {'b': [5,7,13,15], 'r': [6,9,11,14]},
    11: {'b': [7,10,15], 'r': [6,14]},
    12: {'b': [8,13], 'r':[9]},
    13: {'b': [8,10], 'r': [9,12,14]},
    14: {'b': [10,13,15], 'r': [9,11]},
    15: {'b': [10], 'r': [11,14]}
}

def agregar_nodo(G, route, pos, node, length):
    if pos == length:
        return

    if route[pos] == 'b':
        for neighbor in tablero[node]['b']:
            G.add_edge(node, neighbor)
            agregar_nodo(G, route, pos + 1, neighbor, length)
    else:
        for neighbor in tablero[node]['r']:
            G.add_edge(node, neighbor)
            agregar_nodo(G, route, pos + 1, neighbor, length)


def arbol(route, p1):
    G = pgv.AGraph(directed=True )

    if p1:
        agregar_nodo(G, route, 0, 0, len(route))
        G.write("black.dot")
        with open("black.dot", "r") as f:
            dot_graph = f.read()
        graph = graphviz.Source(dot_graph)
        graph.render(filename="grafo1")
    else:
        agregar_nodo(G, route, 0, 3, len(route))
        G.write("red.dot")
        with open("red.dot", "r") as f:
            dot_graph = f.read()
        graph = graphviz.Source(dot_graph)
        graph.render(filename="grafo2")

