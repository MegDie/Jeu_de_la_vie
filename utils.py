import matplotlib.pyplot as plt
import numpy as np

def calcul_nb_voisins(Z):
    
    """Fonction calculant le nombre de voisins pour une grille composée de 0 et de 1 
    
    Entrée: une matrice composée de 1 et de 0
    Sortie: nombre de voisins de chaque cellule sauf pour le bord
    
    """
    
    forme = len(Z), len(Z[0]) 
    N = [[0, ] * (forme[0]) for i in range(forme[1])] 
    for x in range(1, forme[0] - 1): 
        for y in range(1, forme[1] - 1): 
            N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] \
            + Z[x-1][y] + 0 + Z[x+1][y] \
            + Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1] 
    return N

def iteration_jeu(Z): 
    
    """Entrée: une liste de listes composées de 1 ou de 0
       
       Sortie: une itération du jeu"""
    
    forme = len(Z), len(Z[0]) 
    N = calcul_nb_voisins(Z) 
    for x in range(1, forme[0]-1): 
        for y in range(1, forme[1]-1): 
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3): 
                Z[x][y] = 0 
            elif Z[x][y] == 0 and N[x][y] == 3: 
                Z[x][y] = 1 
    return Z

def show(M):
    
    """Cette fonction affiche 10 itérations du jeu de la vie pour une matrice donnée"""
    
    plt.figure(figsize=(10, 5))
    # On doit préalablement transformer nos listes en array pour pouvoir les traiter sous matplotlib
    M = np.array(M)  

    for i in range (1, 11):
        plt.subplot(2, 5, i) # Les itérations seront représentées sur 2 lignes et 5 colonnes
        plt.imshow(M) # On affiche Z
        plt.title ('Etape ' + str(i-1)) # titre de chaque image
        M = iteration_jeu(M) # M prend les valeurs de l'itération suivante du jeu 
        
        
# Configurations stables 

R = np.zeros((50, 50)) # ruche
R[24, 25] = R[24, 26] = R[25, 24] = \
R[25, 27] = R[26, 25] = R[26, 26] = 1

T = np.zeros((50, 50)) # tube
T[24, 25] = T[25, 24] = T[25, 26] = \
T[26, 25] = T[26, 27] = T[27, 26] = 1

N = np.zeros((50, 50)) # navire
N[24, 24] = N[24, 25] = N[25,24] = \
N[25, 26] = N[26, 25] = N[26, 26] = 1

# Configuration oscillante

G = np.zeros((50, 50)) # grenouille
G[25, 25] = G[25, 26] = G[25, 27] = \
G[26, 24] = G[26, 25] = G[26, 26] = 1