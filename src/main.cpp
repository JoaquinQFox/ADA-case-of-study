#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include "GraphLink.h"
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

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

    bool operator<(const Punto& other) const {
        return id < other.id;
    }

    friend ostream& operator<<(ostream& os, const Punto& p) {
        if (p.type == Type::EDIFICIO)
            os << "EDIFICIO" << " " << p.id;
        else
            os << "SERVIDOR" << " " << p.id;

        return os;
    }
};

void saveDot(GraphLink<Punto>& g, const string& filename) {
    ofstream file(filename);
    file << "graph G {\n";
    file << "  layout=dot;\n";
    file << "  rankdir=LR;\n";         // horizontal
    file << "  ratio=1.0;\n";          // cuadrado
    file << "  size=\"10,10!\";\n";    // tamaño de hoja
    file << "  nodesep=0.3;\n";        // separación horizontal
    file << "  ranksep=0.5;\n";        // separación vertical
    file << "  node [shape=circle, style=filled, fontcolor=white, fontsize=10, width=0.4, height=0.4, fixedsize=true];\n";
    file << "  edge [penwidth=1.5, fontsize=8];\n";

    // --- SERVIDORES al centro ---
    file << "  subgraph cluster_servidores {\n";
    file << "    rank=same;\n";  // mismo nivel horizontal
    for (auto v : g.getListVertex()) {
        const Punto& p = v->getData();
        if (p.type == Type::SERVIDOR) {
            file << "    \"" << p.id << "\" [fillcolor=\"#c8310e\"];\n";
        }
    }
    file << "  }\n";

    // --- DEMÁS NODOS ---
    for (auto v : g.getListVertex()) {
        const Punto& p = v->getData();
        if (p.type == Type::EDIFICIO) {
            file << "  \"" << p.id << "\" [fillcolor=\"#1f77b4\"];\n";
        }
    }

    // --- ARISTAS ---
    for (auto v : g.getListVertex()) {
        for (auto& e : v->getAdj()) {
            Punto u = v->getData();
            Punto w = e.getDest()->getData();
            if (u.id < w.id) {
                file << "  \"" << u.id << "\" -- \"" << w.id
                     << "\" [label=\"" << e.getWeight() << "\"];\n";
            }
        }
    }

    file << "}\n";
    file.close();

    // Generar PNG con buena resolución
    string cmd = "dot -Gdpi=200 -Tpng \"" + filename + "\" -o \"" +
                 filename.substr(0, filename.size() - 4) + ".png\"";
    system(cmd.c_str());
}


int Punto::nextId = 1;

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

int main() {
    GraphLink<Punto> grafo = GraphLink<Punto>();

    std::vector<Punto> puntos = {
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::SERVIDOR), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::SERVIDOR), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::EDIFICIO),
        Punto(Type::EDIFICIO), Punto(Type::EDIFICIO), Punto(Type::SERVIDOR)
    };


    for (Punto p : puntos) {
        grafo.insertVertex(p);
    }
    grafo.insertEdge(puntos[1], puntos[0], 30);
    grafo.insertEdge(puntos[2], puntos[1], 30);
    grafo.insertEdge(puntos[3], puntos[2], 30);
    grafo.insertEdge(puntos[4], puntos[3], 30);
    grafo.insertEdge(puntos[5], puntos[4], 30);
    grafo.insertEdge(puntos[6], puntos[5], 30);
    grafo.insertEdge(puntos[7], puntos[6], 30);
    grafo.insertEdge(puntos[8], puntos[7], 30);
    grafo.insertEdge(puntos[0], puntos[8], 30);

    grafo.insertEdge(puntos[2], puntos[9], 30);
    grafo.insertEdge(puntos[3], puntos[9], 30);
    grafo.insertEdge(puntos[5], puntos[9], 30);
    grafo.insertEdge(puntos[7], puntos[9], 30);
    grafo.insertEdge(puntos[8], puntos[9], 30);

    grafo.insertEdge(puntos[11], puntos[0], 30);
    grafo.insertEdge(puntos[21], puntos[10], 30);
    grafo.insertEdge(puntos[0], puntos[21], 30);

    grafo.insertEdge(puntos[11], puntos[10], 30);
    grafo.insertEdge(puntos[12], puntos[11], 30);
    grafo.insertEdge(puntos[13], puntos[12], 30);
    grafo.insertEdge(puntos[14], puntos[13], 30);
    grafo.insertEdge(puntos[15], puntos[14], 30);
    grafo.insertEdge(puntos[16], puntos[15], 30);
    grafo.insertEdge(puntos[17], puntos[16], 30);
    grafo.insertEdge(puntos[18], puntos[17], 30);
    grafo.insertEdge(puntos[10], puntos[18], 30);

    grafo.insertEdge(puntos[11], puntos[19], 30);
    grafo.insertEdge(puntos[12], puntos[19], 30);
    grafo.insertEdge(puntos[16], puntos[19], 30);
    grafo.insertEdge(puntos[17], puntos[19], 30);
    grafo.insertEdge(puntos[18], puntos[19], 30);

    grafo.insertEdge(puntos[21], puntos[20], 30);
    grafo.insertEdge(puntos[22], puntos[21], 30);
    grafo.insertEdge(puntos[23], puntos[22], 30);
    grafo.insertEdge(puntos[24], puntos[23], 30);
    grafo.insertEdge(puntos[25], puntos[24], 30);
    grafo.insertEdge(puntos[26], puntos[25], 30);
    grafo.insertEdge(puntos[27], puntos[26], 30);
    grafo.insertEdge(puntos[28], puntos[27], 30);
    grafo.insertEdge(puntos[20], puntos[28], 30);

    grafo.insertEdge(puntos[21], puntos[29], 30);
    grafo.insertEdge(puntos[22], puntos[29], 30);
    grafo.insertEdge(puntos[23], puntos[29], 30);
    grafo.insertEdge(puntos[27], puntos[29], 30);
    grafo.insertEdge(puntos[28], puntos[29], 30);

    grafo.printGraph();

    saveDot(grafo, "miGrafo.png");
}



