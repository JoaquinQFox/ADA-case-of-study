from graficador import graficar_grafo
from grafo_prueba import get_graph, get_posiciones

if __name__ == "__main__":
    grafo = get_graph()
    posiciones = get_posiciones()

    graficar_grafo(grafo, posiciones)