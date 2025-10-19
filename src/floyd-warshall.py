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