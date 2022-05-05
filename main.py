import numpy as np
"""
pre :
A : Une matrix numpy, une matrice d'adjacence d'un graph dirigé, pndérer et régulier G
alpha : un float ,qui est le paramètre de téléportation(entre 0 et 1 ) 0.9 par défaut 
v : Vecteur de personalisation
post : 
vecteur x contenant les scores d'importance des noeuds ordonnés dans le même ordre que la matrice d'adjacence
"""
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
def pageRankPower(A, alpha, v):
    """
        Renvoie la matrice de probabilité d'une matrice A
        (A est une matrice numpy)
        """
    def ToProb(A):
        b = []
        for i in range(len(A)):
            sum = 0
            b.append([])
            for j in range(len(A[i])):
                sum += A[i][j]
            for j in range(len(A[i])):
                if A[i,j] == 0:
                    b[i].append(0)
                else:
                    b[i].append(A[i,j]/sum)
        p = np.array(b)
        return p
    pass

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
