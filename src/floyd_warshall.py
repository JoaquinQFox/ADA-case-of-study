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
    
    ciclos_negativos = False
    for i in range(n):
        if dist[i][i] < 0:
            ciclos_negativos = True

    if ciclos_negativos:
        print("Se detectaron ciclos negativos.")
    else:
        print("No se detectaron ciclos negativos.")

    return dist, next, index, ciclos_negativos


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


def reconstruir_grafo_floyd(origen, grafo, dist, next, index, ciclos_negativos):
    grafo_rutas = GraphLink()

    for v in grafo.vertices:
        grafo_rutas.insert_vertex(v.data)

    if origen not in index:
        print("Vértice no existe en el grafo.")
        return grafo_rutas
    
    if ciclos_negativos:
        print("Error al reconstruir: el grafo tiene ciclos negativos.")
        return grafo_rutas

    i_origen = index[origen]

    for destino, j in index.items():
        if destino == origen:
            continue
        
        if dist[i_origen][j] == float('inf'):
            continue

        camino = obtener_camino(origen, destino, grafo, next, index)

        if not camino:
            continue

        for (a, b, peso) in camino:
            if peso == 0:
                continue
                
            if grafo_rutas.get_edge_weight(a, b) == -1:
                grafo_rutas.insert_edge(a, b, peso)

    return grafo_rutas


def mostrar_tabla_distancias(dist, index, g: GraphLink):
    vertices = sorted([v.data for v in g.vertices])
    n = len(vertices)
    ancho = 6
    
    print("\n" + "="*((ancho + 1) * (n + 1) + 1))
    print("TABLA DE DISTANCIAS MÍNIMAS (Floyd-Warshall)")
    print("="*((ancho + 1) * (n + 1) + 1))
    
    print(f"{'Desde':^{ancho}}", end=" ")
    for v in vertices:
        print(f"{v:^{ancho}}", end=" ")
    print()
    
    print("-"*((ancho + 1) * (n + 1) + 1))
    
    for v_origen in vertices:
        i = index[v_origen]
        print(f"{v_origen:^{ancho}}", end=" ")
        
        for v_destino in vertices:
            j = index[v_destino]
            valor = dist[i][j]
            
            if valor == float('inf'):
                print(f"{'∞':^{ancho}}", end=" ")
            elif valor == 0 and v_origen == v_destino:
                print(f"{'-':^{ancho}}", end=" ")
            else:
                print(f"{valor:^{ancho}.0f}", end=" ")
        print()
    
    print("="*((ancho + 1) * (n + 1) + 1))
    print()