#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include "GraphLink.h"

using namespace std;

template <typename T>
GraphLink<T> kruskal (GraphLink<T>& G) {
    
    vector<Vertex<T>*> vertices;
    for (auto v : G.getListVertex()) {
        vertices.push_back(v);
    }

    vector<tuple<Vertex<T>*, Vertex<T>*, int>> Q;
    for (auto v : vertices) {
        for (const auto& e : v->getAdj()) {
            if (v->getData() < e.getDest()->getData())
                Q.push_back({v, e.getDest(), e.getWeight()});
        }
    }

    sort(Q.begin(), Q.end(),
        [](const auto& a, const auto& b) {
        return get<2>(a) < get<2>(b);
    });

    int n = vertices.size();
    vector<int> comp (n);
    for (size_t i = 0; i < n; ++i) {
        comp[i] = i;
    }
    
    map<Vertex<T>*, int> vertexIndex;
    for (int i = 0; i < n; ++i) {
        vertexIndex[vertices[i]] = i;
    }

    GraphLink<T> tree;
    for (auto v : G.getListVertex()) {
        tree.insertVertex(v->getData());
    }

    for (const auto& [u, v, w] : Q) {
 
        int iU = vertexIndex[u];
        int iV = vertexIndex[v];

        if(comp[iU] != comp[iV]) {
            tree.insertEdge(u->getData(), v->getData(), w);
            tree.insertEdge(v->getData(), u->getData(), w);
        
            int oldComp = comp[iV];
            int newComp = comp[iU];

            for(auto& c : comp)
                if(c == oldComp)
                    c = newComp;
        }
    }
    
    return tree;
}

enum class Type : int {
    EDIFICIO,
    SERVIDOR
};

struct Punto {
    static int nextId;
    int id;
    Type type;

    Punto(Type type) {
        this->type = type;
        this->id = nextId++;
    }
    Punto() : id(-1), type(Type::EDIFICIO) {}


    bool operator==(const Punto& other) const {
        return id == other.id;
    }

    friend ostream& operator<<(ostream& os, const Punto& p) {
        if (p.type == Type::EDIFICIO)
            os << "EDIFICIO" << " " << p.id;
        else
            os << "SERVIDOR" << " " << p.id;

        return os;
    }
};

int Punto::nextId = 1;

int main() {
    GraphLink<Punto> grafo = GraphLink<Punto>();

    std::vector<Punto> puntos = {
        Punto(Type::EDIFICIO), Punto(Type::SERVIDOR), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::SERVIDOR), Punto(Type::EDIFICIO)
    };


    for (Punto p : puntos) {
        grafo.insertVertex(p);
    }

    grafo.insertEdge(puntos[0], puntos[1], 5);   // edificio 0 -> servidor 1
    grafo.insertEdge(puntos[1], puntos[2], 3);   // servidor 1 -> edificio 2
    grafo.insertEdge(puntos[2], puntos[3], 4);
    grafo.insertEdge(puntos[3], puntos[4], 2);
    grafo.insertEdge(puntos[4], puntos[5], 1);
    grafo.insertEdge(puntos[5], puntos[6], 3);
    grafo.insertEdge(puntos[6], puntos[7], 2);
    grafo.insertEdge(puntos[7], puntos[8], 1);
    grafo.insertEdge(puntos[8], puntos[9], 4);
    grafo.insertEdge(puntos[9], puntos[10], 2);

    grafo.insertEdge(puntos[2], puntos[5], 6);
    grafo.insertEdge(puntos[5], puntos[9], 3);
    grafo.insertEdge(puntos[10], puntos[1], 5);
    grafo.insertEdge(puntos[12], puntos[13], 2);
    grafo.insertEdge(puntos[14], puntos[15], 4);
    grafo.insertEdge(puntos[15], puntos[16], 3);
    grafo.insertEdge(puntos[16], puntos[28], 2); // hacia servidor 28
    grafo.insertEdge(puntos[28], puntos[20], 3);
    grafo.insertEdge(puntos[20], puntos[22], 4);
    grafo.insertEdge(puntos[22], puntos[24], 2);
    grafo.insertEdge(puntos[24], puntos[26], 3);

    // Conexiones cíclicas leves (para probar detección de bucles)
    grafo.insertEdge(puntos[10], puntos[5], 1);
    grafo.insertEdge(puntos[5], puntos[10], 1);
    grafo.insertEdge(puntos[15], puntos[14], 2);

    // Conexión entre los servidores
    grafo.insertEdge(puntos[1], puntos[28], 7);
    grafo.insertEdge(puntos[28], puntos[1], 7);

    grafo.printGraph();
}