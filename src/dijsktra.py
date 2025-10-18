from graph import GraphLink, Vertex
import heapq

def dijkstra(grafo : GraphLink, inicio):
    start_vertex : Vertex = grafo.search_vertex(inicio)

    if not start_vertex:
        return {}

    dist = {v.data: float('inf') for v in grafo.vertices}

    dist[inicio] = 0
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

            if nueva_dist < dist[vecino.data]:
                dist[vecino.data] = nueva_dist
                heapq.heappush(pq, (nueva_dist, vecino))
    return dist

if __name__ == "__main__":
    g = GraphLink()
    g.insert_vertex("A")
    g.insert_vertex("B")
    g.insert_vertex("C")
    g.insert_vertex("D")
    g.insert_vertex("E")

    g.insert_edge("A", "B", 4)
    g.insert_edge("A", "C", 2)
    g.insert_edge("B", "C", 1)
    g.insert_edge("B", "D", 5)
    g.insert_edge("C", "D", 8)
    g.insert_edge("C", "E", 10)
    g.insert_edge("D", "E", 2)

    print("Grafo:")
    g.print_graph()

    distancias = dijkstra(g, "B")
    print("\nDistancias desde B:")
    for nodo, distancia in distancias.items():
        print(f"{nodo}: {distancia}")