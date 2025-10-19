from graph import GraphLink, Vertex



def floyd_warshall (matriz):
    n = len(matriz)

    dist = [fila[:] for fila in matriz]

    for k in range(n):
        for i in range(n):
            dik = dist[i][k]

            if dik == float('inf'):
                continue
                
            row_k = dist[k]
            row_i = dist[i]

            for j in range(n):
                alt = dik + row_k[j]
                
                if alt < row_i[j]:
                    row_i[j] = alt
    
    return dist