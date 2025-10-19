from graph import GraphLink, Vertex
import heapq

def dijkstra(grafo : GraphLink, inicio):
    start_vertex : Vertex = grafo.search_vertex(inicio)
    if not start_vertex:
        return {}, {}

    dist = {v.data: float('inf') for v in grafo.vertices}
    dist[inicio] = 0

    prev = {v.data: None for v in grafo.vertices}

    pq = [(0, start_vertex)]

    actual_dist : float
    actual_vertex : Vertex

    while pq:
        actual_dist, actual_vertex = heapq.heappop(pq)

        if actual_dist > dist[actual_vertex.data]:
            continue

        for edge in actual_vertex.adj_list:
            vecino = edge.dest 
            peso = edge.weight
            nueva_dist = actual_dist + peso

            if peso == 0:
                continue

            if nueva_dist < dist[vecino.data]:
                dist[vecino.data] = nueva_dist
                prev[vecino.data] = actual_vertex.data 
                heapq.heappush(pq, (nueva_dist, vecino))
    return dist, prev

def reconstruir_grafo_dijkstra(grafo_original : GraphLink, prev):
    grafo_rutas = GraphLink()

    for v in grafo_original.vertices:
        grafo_rutas.insert_vertex(v.data)

    for nodo, nodo_prev in prev.items():
        if nodo_prev is not None:
            vertice_prev = grafo_original.search_vertex(nodo_prev)
            peso = None
            for edge in vertice_prev.adj_list:
                if edge.dest.data == nodo:
                    peso = edge.weight
                    break
            if peso is not None:
                grafo_rutas.insert_edge(nodo_prev, nodo, peso)

    return grafo_rutas


if __name__ == "__main__":
    grafo = GraphLink()
    grafo.insert_vertex("A")
    grafo.insert_vertex("B")
    grafo.insert_vertex("C")
    grafo.insert_vertex("D")
    grafo.insert_vertex("E")

    grafo.insert_edge("A", "B", 4)
    grafo.insert_edge("A", "C", 2)
    grafo.insert_edge("B", "C", 1)
    grafo.insert_edge("B", "D", 5)
    grafo.insert_edge("C", "D", 8)
    grafo.insert_edge("C", "E", 10)
    grafo.insert_edge("D", "E", 2)

    print("Grafo:")
    grafo.print_graph()

    distancias, recorrido = dijkstra(grafo, "B")

    new_graph = reconstruir_grafo_dijkstra(grafo, recorrido)

    print("\nNuevo grafo creado con con caminos más cortos desde B")
    new_graph.print_graph()
