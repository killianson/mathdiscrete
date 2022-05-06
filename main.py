import numpy as np
def pageRankPower(A, alpha = 0.9, v=vector):
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
            print("fini")
            print(i)
            break
        v1 = v2
    return v1

def pageRankLinear(A, alpha, v):
    pass
"""
pre :
A : Une matrix numpy, une matrice d'adjacence d'un graph dirigé, pndérer et régulier G
alpha : un float ,qui est le paramètre de téléportation(entre 0 et 1 ) 0.9 par défaut 
v : Vecteur de personalisation
post :Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
le même ordre que la matrice d’adjacence.
"""

"""res
Vous devez donc calculer les scores PageRank de deux façons différentes :
– En Python, en résolvant un système d’équations linéaires. Pour cette technique, vous
pouvez utiliser les fonctions numpy permettant de résoudre un système d’équations
linéaires.
– En Python, en calculant le vecteur propre dominant de gauche de la matrice Google,
en utilisant la power method. Pour cette technique, vous devez implémenter vousmême la power method, et donc la boucle permettant de calculer le vecteur propre
dominant de gauche de la matrice.
"""

"""
main lit un fichier csv
contenant la matrice d’adjacence A du graphe présenté ci-dessous (séparez vos valeurs par
une virgule et chaque ligne de la matrice par un passage à la ligne), qui exécute le calcul de
PageRank (via vos méthodes pageRankPower et pageRankLinear) et imprime les résultats
"""
def main():
    pass
