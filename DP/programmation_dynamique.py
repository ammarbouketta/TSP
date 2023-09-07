# -*- coding: utf-8 -*-
"""programmation_dynamique.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-LZ3Ue2fRXXdVMzmqYwpsOJ-K7Fx40ut
"""

import numpy as np
import time
from itertools import combinations

def tsp_dp(N, distances):
    # initialisation des variables
    all_sets = (1 << N) - 1
    C = {}
    path = {}

    # initialisation de C pour i = 0
    for i in range(1, N):
        C[(1 << i, i)] = distances[0][i]

    # calcul de C et path pour les autres i
    for subset_size in range(2, N):
        for subset in combinations(range(1, N), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for dest in subset:
                prev = bits & ~(1 << dest)

                for k in subset:
                    if k == 0 or k == dest:
                        continue
                    new_cost = C[(prev, k)] + distances[k][dest]
                    if (bits, dest) not in C or C[(bits, dest)] > new_cost:
                        C[(bits, dest)] = new_cost
                        path[(bits, dest)] = (prev, k)

    # trouver la solution optimale
    bits = (1 << N) - 2
    opt_cost = np.inf
    last_index = -1
    for dest in range(1, N):
        cost = C[(bits, dest)] + distances[dest][0]
        if opt_cost > cost:
            opt_cost = cost
            last_index = dest

    # reconstruction du chemin optimal
    p = path[(bits, last_index)]
    path_index = [last_index]
    while p:
        path_index.append(p[1])
        p = path.get(p, None)
    path_index.append(0)

    return opt_cost, list(reversed(path_index))

# exemple d'utilisation avec 5 villes
# Matrice de distances entre les villes
n = 20  # Nombre de villes
np.random.seed(42)  # Pour avoir des résultats reproductibles

# Génération de la matrice d'adjacence aléatoire
distances = np.random.randint(1, 101, size=(n, n))
np.fill_diagonal(distances, 0)
np.savetxt("matrix.txt", distances, fmt="%3d", delimiter="  ")

start_time = time.time()
cost, path = tsp_dp(n, distances)
path.append(0)
comp_time = time.time() - start_time
print(f"-> Computational Time: {comp_time} seconds")
print("Distance minimale:", cost)
print("Chemin optimal:", path)

import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(D):
    """
    Affiche un graphe représentant la matrice d'adjacence D.
    """
    # Création du graphe
    G = nx.Graph()
    G.add_nodes_from(range(D.shape[0]))

    # Ajout des arêtes
    for i in range(D.shape[0]):
        for j in range(i+1, D.shape[0]):
            G.add_edge(i, j, weight=D[i,j])

    # Affichage du graphe
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos, labels={i:i for i in range(D.shape[0])}, font_size=10, font_color='w',
                            font_weight='bold', verticalalignment='center', horizontalalignment='center')
    nx.draw_networkx_edges(G, pos)
    plt.axis('off')
    plt.show()

import networkx as nx
import matplotlib.pyplot as plt

def plot_cities(D, path):
    """
    Affiche un graphe coloré des villes en utilisant la matrice d'adjacence D
    et en connectant les villes dans l'ordre de visite spécifié dans path.
    """
    # Création du graphe
    G = nx.DiGraph()
    G.add_nodes_from(range(D.shape[0]))

    # Ajout des arêtes
    for i in range(D.shape[0]):
        for j in range(i+1, D.shape[0]):
            G.add_edge(i, j, weight=D[i,j])

    # Couleurs pour chaque ville
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

    # Affichage du graphe avec les couleurs et le chemin optimal
    pos = nx.circular_layout(G)
    for i in range(D.shape[0]):
        nx.draw_networkx_nodes(G, pos, nodelist=[i], node_color=colors[i % len(colors)], node_size=500)
        nx.draw_networkx_labels(G, pos, labels={i:i}, font_size=10, font_color='w', font_weight='bold',
                                verticalalignment='center', horizontalalignment='center')
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)] +
                           [(path[-1], path[0])], edge_color='r', width=2)
    plt.axis('off')
    plt.show()

plot_graph(distances)
plot_cities(distances, path)