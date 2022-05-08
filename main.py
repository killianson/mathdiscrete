import numpy as np
import csv


def pageRankLinear(A, alpha, v):
    """
    pre :
    A : Une matrix numpy, une matrice d'adjacence d'un graphe dirigé, pondéré et régulier G
    alpha : un float ,qui est le paramètre de téléportation(entre 0 et 1 ) 0.9 par défaut
    v : Vecteur de personalisation
    post :
    vecteur x contenant les scores d'importance des noeuds ordonnés dans le même ordre que la matrice d'adjacence
    """
    def get_stochastic_matrix(A):
        """
        Retourne la matrice stochastique (la somme des éléments de chaque ligne vaut 1)
        """
        n = len(A)
        P = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if A[i,j] != 0:
                    P[i, j] = A[i, j]/ np.sum(A[i])
                else : 
                    P[i,j]=0
        return P

    def update_until_converge(P, v):
        """
        Produit entre P et v jusqu'à ce que v converge
        """
        new_vector = np.matmul(P, v)
        loop = True
        while loop:
            v = new_vector
            new_vector = np.matmul(P, new_vector)
            for i in range(len(v)):
                if abs(v[0] - new_vector[0]) < 10e-10 and abs(v[1] - new_vector[1]) < 10e-10 and abs(
                        v[0] - new_vector[0]) < 10e-10:
                    loop = False
        return new_vector

    # Matrice stochastic : la somme des éléments de chaque ligne vaut 1
    P = get_stochastic_matrix(A)

    # Mettre à jour le vecteur de personnalisation jusqu'à convergence
    return update_until_converge(P.T, v)




def pageRankPower(A, alpha, v):
    """
    pre :
    A : Une matrix numpy, une matrice d'adjacence d'un graph dirigé, pndérer et régulier G
    alpha : un float ,qui est le paramètre de téléportation(entre 0 et 1 ) 0.9 par défaut 
    v : Vecteur de personalisation
    post : 
    vecteur x contenant les scores d'importance des noeuds ordonnés dans le même ordre que la matrice d'adjacence
    """
    def ToProb(A):#détermine la matrice de probabilité de la matrice A
        b = []
        for i in range(len(A)):
            sum = 0
            b.append([])
            for j in range(len(A[i])):
                sum += A[i][j]
            for j in range(len(A[i])):
                if A[i, j] == 0:
                    b[i].append(0)
                else:
                    b[i].append(A[i, j] / sum)
        p = np.array(b)
        return p
    def vecteur_taille(A,vect = v):#ajustement de la taille du vecteur pour certains test
        l = []
        for i in range(len(A[0])):
            l.append(vect[i])
        v = np.array(l)
        return v.T
    def M_chap(P = ToProb(A), a = alpha):#Détermine G
        E = np.ones((len(P[0]), len(P)))
        return ((alpha*P) + (1-alpha)*(E/(len(P))))
    def new_v2(P,v):#détermine p@v, à refaire car on peut pas utiliser numpy pour ça je pense 
        return P@v
    M2 = M_chap()
    v1 = vecteur_taille(A, v)
    max_iter = 100
    psy = 0.005
    for i in range(max_iter):
        v2 = new_v2(M2,v1)
        if np.linalg.norm(v2 - v1,1) < psy:
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
    #lit le fichier csv et crée un numpy array avec les données
    with open('matrice.csv', mode = 'r') as file: 
        file = csv.reader(file)
        mat = np.array([lines for lines in file ], int)

    #vecteur de personnalisation 
    v = np.array([0.1179, 0.1674, 0.2309, 0.1784, 0.0009, 0.1548, 0.049, 0.0315, 0.0105, 0.0587])

    #alpha
    a = 0.9

    #execution + print

    print("\nPage Rank Linear results : \n", pageRankLinear(mat,a,v), "\n")
    print("Page Rank Power results : \n", pageRankPower(mat,a,v), "\n")
    pass
main()