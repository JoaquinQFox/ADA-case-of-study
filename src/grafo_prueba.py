from graph import GraphLink
from graficador import graficar_grafo

def get_graph():
    g = GraphLink()

    INF = float('inf')
    GRANDE = 999

    for i in range(1, 31):
        g.insert_vertex(i)

    g.insert_edge(1, 2, 20)
    g.insert_edge(1, 8, 10)
    g.insert_edge(1, 9, 30)
    g.insert_edge(2, 3, 5)
    g.insert_edge(2, 6, 15)
    g.insert_edge(2, 8, 15)
    g.insert_edge(3, 4, 10)
    g.insert_edge(3, 5, GRANDE)
    g.insert_edge(3, 6, 10)
    g.insert_edge(4, 5, 10)
    g.insert_edge(4, 6, 5)
    g.insert_edge(5, 6, 5)
    g.insert_edge(6, 7, 10)
    g.insert_edge(7, 11, GRANDE)
    g.insert_edge(7, 13, 20)
    g.insert_edge(7, 17, 40)
    g.insert_edge(8, 12, 30)
    g.insert_edge(8, 18, 25)
    g.insert_edge(9, 18, 10)
    g.insert_edge(10, 11, 25)
    g.insert_edge(10, 19, 5)
    g.insert_edge(12, 13, 10)
    g.insert_edge(12, 17, 10)
    g.insert_edge(13, 14, 25)
    g.insert_edge(13, 16, 10)
    g.insert_edge(14, 15, 40)
    g.insert_edge(15, 16, 20)
    g.insert_edge(16, 17, 20)
    g.insert_edge(16, 22, 10)
    g.insert_edge(16, 23, 5)
    g.insert_edge(17, 27, 10)
    g.insert_edge(18, 20, 5)
    g.insert_edge(18, 21, GRANDE)
    g.insert_edge(18, 20, 5)
    g.insert_edge(18, 21, GRANDE)
    g.insert_edge(18, 19, 15)
    g.insert_edge(19, 18, 15)
    g.insert_edge(19, 29, 10)
    g.insert_edge(19, 30, 20)
    g.insert_edge(20, 21, 5)
    g.insert_edge(20, 17, 20)
    g.insert_edge(21, 22, 20)
    g.insert_edge(22, 23, 5)
    g.insert_edge(22, 26, 40)
    g.insert_edge(22, 27, 5)
    g.insert_edge(22, 28, 10)
    g.insert_edge(23, 25, 5)
    g.insert_edge(23, 26, 10)
    g.insert_edge(24, 25, 5)
    g.insert_edge(24, 26, 20)
    g.insert_edge(25, 26, 50)
    g.insert_edge(26, 27, 10)
    g.insert_edge(28, 29, 40)

    return g

def get_graph_negative():
    g = GraphLink()

    INF = float('inf')
    GRANDE = 999

    for i in range(1, 31):
        g.insert_vertex(i)

    g.insert_edge(1, 2, 20)
    g.insert_edge(1, 8, 10)
    g.insert_edge(1, 9, 30)
    g.insert_edge(2, 3, 5)
    g.insert_edge(2, 6, -15)
    g.insert_edge(2, 8, 15)
    g.insert_edge(3, 4, 10)
    g.insert_edge(3, 5, GRANDE)
    g.insert_edge(3, 6, 10)
    g.insert_edge(4, 5, 10)
    g.insert_edge(4, 6, 5)
    g.insert_edge(5, 6, 5)
    g.insert_edge(6, 7, 10)
    g.insert_edge(7, 11, GRANDE)
    g.insert_edge(7, 13, 20)
    g.insert_edge(7, 17, 40)
    g.insert_edge(8, 12, 30)
    g.insert_edge(8, 18, -25)
    g.insert_edge(9, 18, 10)
    g.insert_edge(10, 11, 25)
    g.insert_edge(10, 19, 5)
    g.insert_edge(12, 13, 10)
    g.insert_edge(12, 17, -10)
    g.insert_edge(13, 14, 25)
    g.insert_edge(13, 16, 10)
    g.insert_edge(14, 15, 40)
    g.insert_edge(15, 16, 20)
    g.insert_edge(16, 17, 20)
    g.insert_edge(16, 22, 10)
    g.insert_edge(16, 23, 5)
    g.insert_edge(17, 27, 10)
    g.insert_edge(18, 20, 5)
    g.insert_edge(18, 21, GRANDE)
    g.insert_edge(18, 20, 5)
    g.insert_edge(18, 21, GRANDE)
    g.insert_edge(18, 19, 15)
    g.insert_edge(19, 18, 15)
    g.insert_edge(19, 29, 10)
    g.insert_edge(19, 30, 20)
    g.insert_edge(20, 21, 5)
    g.insert_edge(20, 17, 20)
    g.insert_edge(21, 22, 20)
    g.insert_edge(22, 23, 5)
    g.insert_edge(22, 26, 40)
    g.insert_edge(22, 27, -5)
    g.insert_edge(22, 28, 10)
    g.insert_edge(23, 25, 5)
    g.insert_edge(23, 26, 10)
    g.insert_edge(24, 25, 5)
    g.insert_edge(24, 26, -20)
    g.insert_edge(25, 26, 50)
    g.insert_edge(26, 27, 10)
    g.insert_edge(28, 29, -40)

    return g

def get_posiciones():
    max_y = 2092  # altura total
    posiciones = {
        1: (202 , max_y - 1687),
        2: (972 , max_y - 1632),
        3: (1273 , max_y - 1820),
        4: (1772, max_y - 1820),
        5: (1692 , max_y - 1472),
        6: (1433 , max_y - 1565),
        7: (1113 , max_y - 1346),
        8: (612 , max_y - 1434),
        9: (227 , max_y - 1217),
        10: (147 , max_y - 862),
        11: (692 , max_y - 1137),
        12: (1052 , max_y - 1011),
        13: (1374 , max_y - 1123),
        14: (1839 , max_y - 1123),
        15: (1612 , max_y - 851),
        16: (1254 , max_y - 788),
        17: (812 , max_y - 782),
        18: (492 , max_y - 862),
        19: (117 , max_y - 590),
        20: (412 , max_y - 510),
        21: (732 , max_y - 469),
        22: (1052 , max_y - 469),
        23: (1490 , max_y - 510),
        24: (1810 , max_y - 510),
        25: (1810 , max_y - 136),
        26: (1452 , max_y - 183),
        27: (1029 , max_y - 82),
        28: (648 , max_y - 172),
        29: (332 , max_y - 216),
        30: (67 , max_y - 92)
    }

    return posiciones

if __name__ == "__main__":
    g = get_graph()
    posiciones = get_posiciones()

    graficar_grafo(g, posiciones)
