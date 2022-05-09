import numpy as np
import csv


def get_prob_matrix(A):
    """
    Retourne la matrice de probabilité (la somme des éléments de chaque ligne vaut 1)
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

def pageRankLinear(A, alpha=0.9, v=None):
    """
    pre :
    A : Une matrix numpy, une matrice d'adjacence d'un graphe dirigé, pondéré et régulier G
    alpha : un float ,qui est le paramètre de téléportation(entre 0 et 1 ) 0.9 par défaut
    v : Vecteur de personalisation
    post :
    vecteur x contenant les scores d'importance des noeuds ordonnés dans le même ordre que la matrice d'adjacence
    """
    if v is None: v = np.array([1/len(A)] * len(A))

    # Matrice de proba : la somme des éléments de chaque ligne vaut 1
    P = get_prob_matrix(A)

    new_matrix = np.transpose((np.identity(len(P)) - alpha * P))
    return np.linalg.solve(new_matrix, (1 - alpha) * v)


def pageRankPower(A, alpha=0.9, v=None):
    """
    pre :
    A : Une matrix numpy, une matrice d'adjacence d'un graph dirigé, pndérer et régulier G
    alpha : un float ,qui est le paramètre de téléportation(entre 0 et 1 ) 0.9 par défaut 
    v : Vecteur de personalisation
    post : 
    vecteur x contenant les scores d'importance des noeuds ordonnés dans le même ordre que la matrice d'adjacence
    """
    if v is None: v = np.array([1 / len(A)] * len(A))

    def vecteur_taille(A, vect=v):  # ajustement de la taille du vecteur pour certains test
        l = []
        for i in range(len(A[0])):
            l.append(vect[i])
        v = np.array(l)
        return v.T

    def M_chap(P, a=alpha):  # Détermine G
        E = np.ones((len(P[0]), len(P)))
        return ((alpha * P) + (1 - alpha) * (E / (len(P))))

    def new_v2(P, v):  # détermine p@v
        c = np.zeros(len(v))
        for i in range(len(P)):
            sum = 0
            for j in range(len(v)):
                sum += P[i][j] * v[j]
            c[i] = sum
        return c

    prob_matrix = get_prob_matrix(A)
    M2 = M_chap(prob_matrix)
    v1 = vecteur_taille(A, v)
    max_iter = 100
    psy = 0.005
    for i in range(max_iter):
        v2 = new_v2(M2, v1)
        if np.linalg.norm(v2 - v1, 1) < psy:
            break
        v1 = v2
    return v1


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
    pass


main()


