import numpy as np
from copy import deepcopy

matrice_distances = np.array([[0, 52, 7, 16, 8, 10],
              [np.inf, 0, 3, 8, 4, 10],
              [1, np.inf, 0, 2, 16, 10],
              [5, 3, 15, 0, 10, 10],
              [2, np.inf, 4, np.inf, 0, 10],
              [2, np.inf, 4, np.inf, 10, 0]])


nombre_villes = matrice_distances.shape[0]
niveau_ancien = [[]] * nombre_villes
niveau_courant = [[]] * nombre_villes

def init_niveau():
    niveau_ancien[0] = []
    for i in range(1, nombre_villes): 
        niveau_ancien[i] = [[0]]
    niveau_courant = [[]] * nombre_villes
        
def calculerCout(list):
    i = 0
    j = 1
    cout = 0
    for i in range(len(list)-1):
        cout += matrice_distances[list[i]][list[j]]
        j += 1
    return cout

if __name__=='__main__' :
    init_niveau()
    for niveau in range(1, matrice_distances.shape[0] - 1 ):
        for i in range(1, matrice_distances.shape[0]):
            for j in range(1, matrice_distances.shape[0]):
                if(i != j):
                    for état in niveau_ancien[j]:
                        if(not (i in état) ):
                            nouveau_état = [None]
                            nouveau_état = deepcopy(état)
                            nouveau_état.append(j)
                            if(len(nouveau_état) == len(set(nouveau_état))):
                               niveau_courant[i].append(nouveau_état)

                            
        niveau_ancien = deepcopy(niveau_courant)
        niveau_courant = [[]] * nombre_villes
        


    cpt = 0
    niveau_courant = [[]] * nombre_villes
    i = 0
    nouveau_état = [None]
    min = np.inf
    for j in range(1, matrice_distances.shape[0]):
        for état in niveau_ancien[j]:
            nouveau_état = deepcopy(état)
            nouveau_état.append(j)
            cpt+=1
            if(len(nouveau_état) == len(set(nouveau_état))):
                cout = calculerCout(nouveau_état) + matrice_distances[j][0]
                if(cout < min):
                    sol = deepcopy(nouveau_état)
                    nouveau_état.append(j)
                    min = cout    
    sol.append(0)    

    print("la meilleur solution est : ", sol, " avec un cout de ", min )
    print(cpt, nombre_villes)