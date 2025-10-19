from dijsktra import dijkstra, reconstruir_grafo_dijkstra
from graph import GraphLink
from grafo_prueba import get_graph, get_posiciones
from graficador import graficar_grafo

if __name__ == "__main__":
    grafo = get_graph()
    posiciones = get_posiciones()

    costos, recorrido = dijkstra(grafo, 1)

    new_graph = reconstruir_grafo_dijkstra(grafo, recorrido)

    graficar_grafo(new_graph, posiciones)