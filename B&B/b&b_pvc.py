# -*- coding: utf-8 -*-
"""B&B_PVC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xZQOoE9YLPcFZD1u1KXro0owGIDsQ1wX
"""

import numpy as np

# Matrice de distances entre les villes
D = np.array([[0, 10, 15, 20],
              [10, 0, 35, 25],
              [15, 35, 0, 30],
              [20, 25, 30, 0]])

# Fonction d'évaluation pour calculer la longueur totale d'un chemin
def evaluate_path(path):
    length = 0
    for i in range(len(path)-1):
        length += D[path[i], path[i+1]]
    length += D[path[-1], path[0]]
    return length

# Algorithme de branch and bound
def branch_and_bound():
    # Initialisation de la recherche
    start_node = {
        'path': [0],
        'length': 0,
        'available': set(range(1, D.shape[0]))
    }
    best_path = None
    best_length = np.inf
    nodes = [start_node]

    while nodes:
        # Sélection du nœud avec la plus petite longueur partielle
        node = min(nodes, key=lambda x: x['length'])

        # Développement du nœud
        for city in node['available']:
            child_path = node['path'] + [city]
            child_length = node['length'] + D[node['path'][-1], city]
            child_available = node['available'] - {city}
            child_node = {
                'path': child_path,
                'length': child_length,
                'available': child_available
            }

            # Évaluation de la longueur totale du chemin partiel
            if not child_available:
                # Solution complète trouvée
                length = evaluate_path(child_path)
                if length < best_length:
                    best_length = length
                    best_path = child_path
            elif child_length + min([D[node['path'][-1], c]
             for c in child_available]) < best_length:
                # Ajout du nœud à la liste des nœuds à explorer
                nodes.append(child_node)

        # Suppression du nœud exploré de la liste des nœuds à explorer
        nodes.remove(node)

    return best_path, best_length

# Exécution de l'algorithme de branch and bound
best_path, best_length = branch_and_bound()

# Affichage de la meilleure solution trouvée
print("Meilleure solution trouvée :", best_path)
print("Longueur de la meilleure solution trouvée :", best_length)