# -*- coding: utf-8 -*-
"""
Practica - 5 Algoritmo de Árbol de Máximo y Mínimo coste Kruskal.
Jayden Hammond Caballero - 22310235
"""
# =============================================================================
# #f5 Para ejecutar
# =============================================================================
# Simulador de rutas con Algoritmo de Árbol de Máximo y Mínimo coste Kruskal.
# Google Maps

import matplotlib.pyplot as plt
import networkx as nx

# MAPA
rutas = [
    ('Centro', 'Plaza Norte', 4),
    ('Centro', 'Estadio', 8),
    ('Plaza Norte', 'Estadio', 11),
    ('Plaza Norte', 'Hospital', 8),
    ('Hospital', 'Universidad', 2),
    ('Hospital', 'Museo', 4),
    ('Hospital', 'Aeropuerto', 7),
    ('Aeropuerto', 'Museo', 14),
    ('Aeropuerto', 'Playas', 9),
    ('Playas', 'Museo', 10),
    ('Museo', 'Parque Industrial', 2),
    ('Parque Industrial', 'Universidad', 6),
    ('Parque Industrial', 'Estadio', 1),
    ('Estadio', 'Universidad', 7)
]

# ALGORITMO
class UnionFind:
    def __init__(self, nodos):
        self.parent = {n: n for n in nodos}

    def find(self, nodo):
        if self.parent[nodo] != nodo:
            self.parent[nodo] = self.find(self.parent[nodo])
        return self.parent[nodo]

    def union(self, nodo1, nodo2):
        raiz1 = self.find(nodo1)
        raiz2 = self.find(nodo2)
        if raiz1 != raiz2:
            self.parent[raiz2] = raiz1
            return True
        return False

# PASOS
def kruskal(nodos, rutas, modo='minimo'):
    uf = UnionFind(nodos)
    seleccionadas = []
    pasos = []

    rutas_ordenadas = sorted(rutas, key=lambda x: x[2], reverse=(modo == 'maximo'))

    for origen, destino, distancia in rutas_ordenadas:
        if uf.union(origen, destino):
            seleccionadas.append((origen, destino, distancia))
            pasos.append(f"Conectando {origen} → {destino} ({distancia} km)")

    return seleccionadas, pasos

# GRAFICAR
def graficar(nodos, rutas, seleccionadas, titulo):
    G = nx.Graph()
    G.add_weighted_edges_from(rutas)
    pos = nx.spring_layout(G, seed=10)

    nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=850, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{w} km" for u, v, w in rutas})

    edges_marcadas = [(u, v) for u, v, _ in seleccionadas]
    nx.draw_networkx_edges(G, pos, edgelist=edges_marcadas, edge_color='green', width=3)

    plt.title(titulo)
    plt.axis('off')
    plt.show()

# RESULTADOS
if __name__ == "__main__":
    zonas = sorted(set([u for u, v, _ in rutas] + [v for u, v, _ in rutas]))

    print("Rutas de Mínima Distancia (estilo Google Maps):")
    rutas_min, pasos_min = kruskal(zonas, rutas, modo='minimo')
    for paso in pasos_min:
        print("  -", paso)

    print("\nRutas de Máxima Distancia Posible (por ejemplo, en modo escénico):")
    rutas_max, pasos_max = kruskal(zonas, rutas, modo='maximo')
    for paso in pasos_max:
        print("  -", paso)

    graficar(zonas, rutas, rutas_min, "Google Maps: Rutas de Mínima Distancia (Kruskal)")
    graficar(zonas, rutas, rutas_max, "Rutas")
