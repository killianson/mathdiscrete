import numpy as np
import csv


def get_prob_matrix(A):
    """
    Retourne la matrice des probabilités de transition (la somme des éléments de chaque ligne vaut 1)
    """
    n = len(A)
    P = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if A[i, j] != 0:
                P[i, j] = A[i, j] / np.sum(A[i])
            else:
                P[i, j] = 0
    return P


def pageRankLinear(A, alpha, v):
    """
    pré :
    A : Une matrix numpy, une matrice d'adjacence d'un graphe dirigé, pondéré et régulier G
    alpha : un float ,qui est le paramètre de téléportation(entre 0 et 1 ) 0.9 par défaut
    v : Vecteur de personalisation
    post :
    vecteur x contenant les scores d'importance des noeuds ordonnés dans le même ordre que la matrice d'adjacence
    """
    # matrice des probabilités de transition
    P = get_prob_matrix(A)

    # résolution de l'équation
    new_matrix = np.transpose((np.identity(len(P)) - alpha * P))
    pr_vector = np.linalg.solve(new_matrix, (1 - alpha) * v)

    return pr_vector / pr_vector.sum()  # normalisation du vecteur


def pageRankPower(A, alpha, v):
    """
    pré :
    A : Une matrix numpy, une matrice d'adjacence d'un graph dirigé, pondéré et régulier G
    alpha : un float, qui est le paramètre de téléportation (entre 0 et 1) 0.9 par défaut
    v : Vecteur de personalisation
    post : 
    vecteur x contenant les scores d'importance des noeuds ordonnés dans le même ordre que la matrice d'adjacence
    """

    def get_google_matrix(P):  # Détermine G
        e = np.ones(len(P))
        return (alpha * P) + (1 - alpha) * np.matmul(e, v.T)

    # matrice des probabilités de transition
    P = get_prob_matrix(A)
    print("matrice de proba\n", P, "\n\n") #--------------------------print--funct--------------------------------
    # matrice Google
    G = get_google_matrix(P)
    print("matrice Google\n", G, "\n\n") #--------------------------print--funct--------------------------------
    # mise à jour du vecteur de personnalisation jusqu'à convergence
    loop = True
    i = 0
    while loop:
        v_prev = v
        v = np.matmul(v, G)
        v /= v.sum()
        i+=1
        if i<4 : print("matrice itérations vecteurs des score numéro ",i,":\n", v, "\n")#--------------------------print--funct--------------------------------
        if abs(v[0] - v_prev[0]) < 10e-10 and abs(v[1] - v_prev[1]) < 10e-10 and abs(
                v[0] - v_prev[0]) < 10e-10:
            loop = False
    return v


def main():
    """
    main lit un fichier csv
    contenant la matrice d’adjacence A du graphe présenté ci-dessous (séparez vos valeurs par
    une virgule et chaque ligne de la matrice par un passage à la ligne), qui exécute le calcul de
    PageRank (via vos méthodes pageRankPower et pageRankLinear) et imprime les résultats
    """
    # lit le fichier csv et crée un numpy array avec les données
    with open('matrice.csv', mode='r') as file:
        file = csv.reader(file)
        mat = np.array([lines for lines in file], int)

    # vecteur de personnalisation
    v = np.array([0.1179, 0.1674, 0.2309, 0.1784, 0.0009, 0.1548, 0.049, 0.0315, 0.0105, 0.0587])

    # alpha
    a = 0.9

    # execution + print
    print("\nPage Rank Linear results : \n", pageRankLinear(mat, a, v), "\n")
    print("Page Rank Power results : \n", pageRankPower(mat, a, v), "\n")


if __name__ == '__main__':
    main()
