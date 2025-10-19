from floyd_warshall import floyd_warshall, reconstruir_grafo_floyd
from graph import GraphLink
from grafo_prueba import get_graph, get_graph_negative, get_posiciones
from graficador import graficar_grafo

if __name__ == "__main__":

    print("Caso 1 pesos positivos: ")
    grafo = get_graph()
    posiciones = get_posiciones()

    dist, next, index, ciclos_negativos = floyd_warshall(grafo)

    new_graph = reconstruir_grafo_floyd(1, grafo, dist, next, index, ciclos_negativos)

    graficar_grafo(new_graph, posiciones)

    print("\nCaso 2 ciclos negativos: ")
    grafo = get_graph_negative()
    posiciones = get_posiciones()

    dist, next, index, ciclos_negativos = floyd_warshall(grafo)

    new_graph = reconstruir_grafo_floyd(1, grafo, dist, next, index, ciclos_negativos)

    graficar_grafo(new_graph, posiciones)