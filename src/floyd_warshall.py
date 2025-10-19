from graph import GraphLink
import math

def floyd_warshall (g: GraphLink):
    n = len(g.vertices)

    if n == 0:
        return None, None, None

    index = {v.data: i for i, v in enumerate(g.vertices)}
    dist  = [[float('inf')] * n for _ in range(n)]
    next  = [[None] * n for _ in range(n)]

    # INICIALIZA PESOS DIRECTOS
    for i, v in enumerate(g.vertices):
        dist[i][i] = 0
        for edge in v.adj_list:
            j = index[edge.dest.data]
            dist[i][j] = edge.weight
            next[i][j] = j

    # ALG. PRINCIPAL
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]

            if dik == float('inf'):
                continue

            for j in range(n):
                alt = dik + dist[k][j]
                
                if alt < dist[i][j]:
                    dist[i][j] = alt
                    next[i][j] = next[i][k]
    
    return dist, next, index


def obtener_camino (origen, destino, g: GraphLink, next, index):
    i = index[origen]
    j = index[destino]

    if next[i][j] is None:
        return []
    
    camino_detallado = []
    actual = origen

    while i != j:
        i = next[i][j]
        siguiente = g.vertices[i].data
        peso      = g.get_edge_weight(actual, siguiente)
        camino_detallado.append((actual, siguiente, peso))
        actual    = siguiente

    return camino_detallado


def reconstruir_grafo_floyd (origen, grafo, dist, next, index):
    grafo_rutas = GraphLink()

    for v in grafo.vertices:
        grafo_rutas.insert_vertex(v.data)

    if origen not in index:
        print("Vértice no existe en el grafo.")
        return grafo_rutas

    for destino in index:
        if destino == origen:
            continue

        camino = obtener_camino(origen, destino, grafo, next, index)

        for (a, b, peso) in camino:
            grafo_rutas.insert_edge(a, b, peso)

    return grafo_rutas