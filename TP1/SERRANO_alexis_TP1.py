############################## Exo 1 ############################## 

print("\n\n"+"-"*40+" Exo 1 "+"-"*40)
print("\n\n"+"-"*40+" Exo 1 "+"-"*40)

def matriceAgmentee(A, B):
    """
    Renvoie la matrice [A|B] (sans la ligne de séparation)

    @params
    - Matrice A 
    - Vecteur B
    """

    for i in range(0, len(A)): 
        A[i].append(B[i]) #On rajoute a chaque ligne la valeur associé
    return A

print("(1) Coder la matrice A")
A = [[1, 2, -1], [2, 2, 1], [1, 4, 1]]
print(A, "\n")

print("(2) Coder le vecteur B")
B = [4, 5, 2]
print(B, "\n")

print("(3) Coder la matrice augmentée C = [A|B]")
C = matriceAgmentee(A, B)

############################## Exo 2 ############################## 

print("\n\n"+"-"*40+" Exo 2 "+"-"*40)

print("(1) Créer la fonction permL qui prend en argument une matrice M, une ligne i et une ligne j, et\nqui renvoie l’opération Li <-> Lj sur M.")
def permL(M, i, j):
    """
    Applique et renvoie la matrice M avec une inversion des lignes i et j
    de la matrice
    Li <-> Lj
    
    @params
    - Matrice M
    - int i : indice allant de 0 à len(M)
    - int j : indice allant de 0 à len(M) (et différent de i)
    """
    #M[i], M[j] = M[j, M[i]]
    temp = M[i]
    M[i] = M[j]
    M[j] = temp
    return M

print(A)
print(permL(A, 1, 2))


print("\n(2) Créer la fonction ajoutS qui prend en argument une matrice M, une ligne i, une ligne j et un\nscalaire a, et qui renvoie l’opération Li <- Li + a*Lj sur M.")

def ajoutS(M, i, j, a):
    """
    Applique et renvoie la matrice M avec une affectation à la ligne i
    de la ligne i + a fois la ligne j
    Li <-> Li + a*Lj
    
    @params
    - Matrice M
    - int i : indice allant de 0 à len(M)
    - int j : indice allant de 0 à len(M) (et différent de i)
    - int a : (différent de 0)
    """
    for k in range(0, len(M[i])):
        M[i][k] = M[i][k] + a*M[j][k]
    return M
    
print(A)
print(ajoutS(A, 1, 2, 2))


print("\n(3) Créer la fonction multiS qui prend en argument une matrice M, une ligne i et un scalaire a,\net qui renvoie l’opération Li <- a*Li sur M.")

def multiS(M, i, a):
    """
    Applique et renvoie la matrice M avec une multiplication par le scalaire a
    de la ligne i
    Li <-> a*Li
    
    @params
    - Matrice M
    - int i : indice allant de 0 à len(M)
    - int a : (différent de 0)
    """
    for k in range(0, len(M[i])):
        M[i][k] *= a
    return M
    
print(A)
print(multiS(A, 1, 2))

print("\n(4) Tester les 3 fonctions sur la matrice A en affichant le résultat")
print("Je l'ai fait directement pour chaque question")


############################## Exo 3 ############################## 
print("\n\n"+"-"*40+" Exo 3 "+"-"*40)

print("(1) Créer la fonction pivotGauss qui échelonne-réduit une matrice A = (ai,j)i,j appartient à P M(n,m)([R) par l'algorithme")

def pivotGauss(A):
    """
    Applique et renvoie la matrice A devenue réduite et échelonnée 
    par le pivot de Gauss
    
    @params
    - Matrice M
    """
    p = 0
    n = len(A)
    m = len(A[0])
    for j in range(0, m):
        k = argMax(A, p, n, j)
        if A[k][j] != 0:
            multiS(A, k, 1/(A[k][j]))
            if k != p:
                permL(A, k, p)
            for i in range(0, n):
                if i != p:
                    ajoutS(A, i, p, -A[i][j])
            p+=1
    return A

def argMax(A, p, n, j):
    """
    Renvoie l'argument de la valeur maximale sur la colonne j de la ligne n à p
    Comme nous n'utilisons pas la valeur maximale, la racine carrée n'est pas
    calculée car elle consomme du temps de calcul inutilement car le carré permet
    déjà de connaitre l'ordre

    @params
    - Matrice A
    - indice p : compris entre 0 et n
    - indice n : compris entre p et len(A)-1
    - indice j de la colonne
    """
    k = p
    max = A[p][j]**2
    for i in range(p+1, n):
        if A[i][j]**2 > max:
            k = i
            max = A[i][j]**2
    return k

print("\n(2) Tester la fonction pivotGauss sur la matrice A en affichant le résultat.")

A = [[1, 2, -1], [2, 2, 1], [1, 4, 1]]
print(pivotGauss(A))


############################## Exo 4 ############################## 
print("\n\n"+"-"*40+" Exo 4 "+"-"*40)

print("(1) Créer la fonction pivotGaussAug qui échelonne-réduit une matrice augmentée.")

def pivotGaussAug(C):
    """
    Applique et renvoie la matrice A *augmentée* devenue réduite 
    et échelonnée par le pivot de Gauss
    
    @params
    - Matrice M augmentée
    """
    p = 0
    n = len(C)
    m = len(C[0])
    for j in range(0, m-1):
        k = argMax(C, p, n, j)
        if A[k][j] != 0:
            multiS(C, k, 1/(A[k][j]))
            if k != p:
                permL(C, k, p)
            for i in range(0, n):
                if i != p:
                    ajoutS(C, i, p, -C[i][j])
            p+=1

print("\n(2) Tester la fonction pivotGaussAug sur la matrice augmentée C en affichant le résultat.")

A = [[1, 2, -1], [2, 2, 1], [1, 4, 1]]
B = [4, 5, 2]
C = matriceAgmentee(A, B)
pivotGaussAug(C)
print(C)

def getVectResult(C):
    """
    Renvoie le vecteur résultat d'une matrice augmentée échelonnée réduite
    
    @params
    - Matrice c augmentée échelonnée réduite
    """
    vecteur = []
    for i in range(0, len(C)):
        vecteur.append(C[i][-1])
    return vecteur

print("\n(3) Afficher le vecteur résultat.")
print(getVectResult(C))