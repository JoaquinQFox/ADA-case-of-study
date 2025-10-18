import networkx as nx
import matplotlib.pyplot as plt
import random
from graph import GraphLink

def graficar_grafo(grafo : GraphLink):
    G = nx.Graph()

    for vertices in grafo.vertices:
        G.add_node(vertices.data)

    for vertex in grafo.vertices:
        for edge in vertex.adj_list:
            if not G.has_edge(vertex.data, edge.dest.data):
                G.add_edge(vertex.data, edge.dest.data, weight=edge.weight)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)

    nx.draw_networkx_edges(G, pos, width=2)

    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    g = GraphLink()

    for i in range(15):
        g.insert_vertex(chr(65 + i))

    for i in range(len(g.vertices)):
        for j in range(i + 1, len(g.vertices)):
            peso = random.randint(1, 10)
            g.insert_edge(g.vertices[i].data, g.vertices[j].data, peso)

    g.print_graph()

    graficar_grafo(g)
