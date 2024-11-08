############################## Exo 1 ############################## 

print("\n\n"+"-"*40+" Exo 1 "+"-"*40)

print("(1) Traduire cet énoncé sous la forme d’un problème d’optimisation linéaire sous forme standard")

print("max f = 2 - x1 + 2x2 + 3x3"+
        "\ns.c.    4x1 + 4x2 + 8x3 + x4 <= 2"+
        "\n         x1 - 3x2 + 5x3 + x5 <= 3"+
        "\n        3x1 + 7x2 - 3x3 + x6 <= 0"+
        "\n        x1, x2, x3 >= 0.")

print("L'objectif est de maximiser f sous les contraintes ci-dessus.")

print("(2) Coder la matrice augmentée M correspondante (sans les variables d’écart).")

M = [
    [4, 4, 8, 2],
    [1, -3, 5, 3],
    [3, 7, -3, 0],
    [-1, 2, 3, -2]
]

def afficher(T : list):
    """
    Affiche une matrice
    Paramètres :
        T : list
            Matrice à afficher
    """
    for row in T:
        print("[", end="")
        print(" ".join(f"{val:>5}" for val in row), end = "")
        print("]")

print("\nM : ")
afficher(M)

print("(3) Coder la fonction varEcart qui retourne une matrice Ms qui correspond au problème avec les variables d’écart.")


def varEcart(T : list):
    """
    Retourne une matrice Ms qui correspond au problème avec les variables d’écart.
    Paramètres :
        T : list
            Matrice à transformer
    Retourne :
        list
            Matrice transformée
    """
    Ms = T.copy()
    for i in range(0, len(T)):

        Ms[i] = T[i][0:len(M[0])-1]

        for j in range(0, len(T)-1):
            if j == i:
                Ms[i].append(1)
            else:
                Ms[i].append(0)
        Ms[i].append(T[i][-1])
    return Ms

Ms = varEcart(M)
print("\nMs :")
afficher(Ms)

print("(4) Coder la fonction base qui retourne le vecteur de base b définit tel que bj = i si xj est une variable de base, présente dans la ligne i, et bj = -1 sinon.")

def baase(Ts):
    """
    (Deuxième manière) Retourne le vecteur de base b définit tel que bj = i si xj est une variable de base, présente dans la ligne i, et bj = -1 sinon.
    Paramètres :
        Ts : list
            Matrice augmentée
    Retourne :
        list
            Vecteur de base b
    """
    B = []
    for i in range(len(Ts)-1):
        if Ts[i][0] == 0:
            isValid = True
            one = -1

            j = 1
            while isValid:
                if Ts[i][j] == 1 and one != -1:
                    isValid = False
                elif Ts[i][j] == 1 and one == -1:
                    one = j
                elif Ts[i][j] != 0:
                    isValid = False
                j += 1
            
            if isValid:
                B.append(one)
            else:
                B.append(-1)
            
        elif Ts[0][i] == 1:
            isOnlyOne = True
            j = 1
            while j < len(Ts) and isOnlyOne:
                if Ts[j][i] != 0:
                    isOnlyOne = False
                j += 1
            if isOnlyOne:
                B.append(i)
            else:
                B.append(-1)
        else:
            B.append(-1)  
    return B

def base(Ts):
    """
    Retourne le vecteur de base b définit tel que bj = i si xj est une variable de base, présente dans la ligne i, et bj = -1 sinon.
    Paramètres :
        Ts : list
            Matrice augmentée
    Retourne :
        list
            Vecteur de base b
    """
    B = []
    for i in range(0, len(Ts[0])-1):
        onePlacement = -1
        isOnePlaced = False
        j = 0
        while j < len(Ts) and Ts[j][i] in [0, 1]:
            if Ts[j][i] == 1 and not isOnePlaced:
                onePlacement = j
                isOnePlaced = True
            elif Ts[j][i] == 1 and isOnePlaced:
                onePlacement = -1
            j += 1

        if(j < len(Ts)):
            onePlacement = -1

        B.append(onePlacement)
    return B

b = base(Ms)
print("\nb : ")
print(b)

############################## Exo 2 ############################## 

print("\n\n"+"-"*40+" Exo 2 "+"-"*40)

print("(1) Créer la fonction solBase qui retourne la solution de base d’une matrice augmentée.")

def solBase(Ts):
    """
    Retourne la solution de base d’une matrice augmentée.
    Paramètres :
        Ts : list
            Matrice augmentée
    Retourne :
        list
            Solution de base de la matrice augmentée Ts
    """
    B = base(Ts)
    S = []
    for i in range(len(B)):
        if B[i] == -1:
            S.append(0)
        else:
            S.append(Ts[B[i]][-1])
    return S

sol = solBase(Ms)
print("\nsol :")
print(sol)

print("(2) Créer la fonction solBaseObj qui retourne la valeur de la fonction objectif évaluée en la solution de base.")

def solBaseObj(Ts):
    """
    Retourne la valeur de la fonction objectif évaluée en la solution de base.
    Paramètres :
        Ts : list
            Matrice augmentée
    Retourne :
        int
            Valeur de la fonction objectif évaluée en la solution de base
    """
    S = solBase(Ts)
    maxf = 0

    for i in range(len(Ts[-1])-1):
        maxf += S[i]*Ts[-1][i]
    maxf -= Ts[-1][-1]
    return maxf

maxf = solBaseObj(Ms)
print("\nmaxf :")
print(maxf)

print("(3) Créer la fonction echanger qui retourne le nouveau vecteur de base en fonction d’un pivot donné en (i, j).")

def echanger(i, j, B):
    """
    Retourne le nouveau vecteur de base en fonction d’un pivot donné en (i, j).
    Paramètres :
        i : int
            Ligne du pivot
        j : int
            Colonne du pivot
        B : list
            Vecteur de base
    Retourne :
        list
            Nouveau vecteur de base
    """
    newB = B.copy()

    k = 0
    while k < len(B) and B[k] != i:
        k+=1
    assert k < len(B)

    newB[k],newB[j] = newB[j],newB[k]
    return newB

newB = echanger(1, 0, b)
print("\nmnewB :")
print(newB)

print("(4) Tester ces fonctions.")

Test = [
    [1, 1, 1, 0, 2],
    [2, -1, 0, 1, 1],
    [2, 1, 0, 0, 0]
]

#B attendu : [-1, -1, 0, 1]
assert base(Test) == [-1, -1, 0, 1]


#solution de base attendue [0, 0, 2, 1]
assert solBase(Test) == [0, 0, 2, 1]

#valeur de la fonction objectif évaluée en la solution de base attendue
assert solBaseObj(Test) == 0

#B échangé en (1,0) attendu : [1, -1, 0, -1]
assert echanger(1, 0, base(Test)) == [1, -1, 0, -1]

print("Succès des tests")

############################## Exo 3 ############################## 

print("\n\n"+"-"*40+" Exo 3 "+"-"*40)

print("(1) Créer la fonction echelRed ramenant à 1 un pivot donné en (i, j) et à 0 les autres coefficients de la colonne du pivot à l’aide d’opérations usuelles sur les matrices augmentées.")

def echelRed(M, i, j):
    """
    Ramène à 1 un pivot donné en (i, j) et à 0 les autres coefficients de la colonne du pivot à l’aide d’opérations usuelles sur les matrices augmentées.
    Paramètres :
        M : list
            Matrice augmentée
        i : int
            Ligne du pivot
        j : int
            Colonne du pivot
    Retourne :
        None
    """
    pivot = M[i][j]
    for k in range(len(M[0])):
        M[i][k] /= pivot

    for l in range(len(M)):
        if l != i:
            factor = M[l][j]
            for k in range(len(M[0])):
                M[l][k] -= factor * M[i][k]


print("(2) Tester cette fonction.")

afficher(Test)
echelRed(Test, 0, 1)
print("\n")
afficher(Test)


############################## Exo 4 ############################## 

print("\n\n"+"-"*40+" Exo 4 "+"-"*40)

print("(1) Créer la fonction jPivot retournant l’indice de colonne donné par l’algorithme du simplexe sur une matrice M si il existe, -1 sinon.")

def jPivot(M):
    """
    Retourne l’indice de colonne donné par l’algorithme du simplexe sur une matrice M si il existe, -1 sinon.
    Paramètres :
        M : list
            Matrice augmentée
    Retourne :
        int
            Indice de colonne
    """
    j = 0
    isValid = False
    for jj in range(len(M)-1):
        if M[-1][jj] > 0:
            isValid = True
            if M[-1][jj] > M[-1][j]:
                j = jj
        
    if isValid:
        return j
    return -1

print("(2) Créer la fonction iPivot retournant l’indice de ligne donné par l’algorithme du simplexe sur la colonne d’une matrice M si il existe, -1 sinon.")

def iPivot(M):
    """
    Retourne l’indice de ligne donné par l’algorithme du simplexe sur la colonne d’une matrice M si il existe, -1 sinon.
    Paramètres :
        M : list
            Matrice augmentée
    Retourne :
        int
            Indice de ligne
    """
    i = 0
    j = jPivot(M)

    if j <= 0:
        return -1
    
    isValid = False
    for ii in range(len(M)-1):
        if M[ii][-1] != 0 and M[ii][j] / M[ii][-1] > 0:
            isValid = True
            if M[ii][-1] / M[ii][j] < M[i][-1] / M[i][j]:
                i = ii
    
    if isValid:
        return i
    return -1

print("(3) Tester ces fonctions.")

assert (iPivot(M),jPivot(M)) == (0, 2)

Test = [
    [4, 4, 8, 2],
    [1, -3, 5, 3],
    [3, 7, -3, 0],
    [-1, -2, -3, -2]
]

assert (iPivot(Test),jPivot(Test)) == (-1, -1)

Test = [
    [4, 4, 8, -2],
    [1, -3, -5, 3],
    [3, 7, -3, 0],
    [-1, 2, 3, -2]
]

assert (iPivot(Test),jPivot(Test)) == (-1, 2)

print("Succès des tests")

############################## Exo 5 ############################## 

print("\n\n"+"-"*40+" Exo 5 "+"-"*40)

print("(1) Créer la fonction simplexe résolvant une matrice augmentée en renvoyant soit la valeur des variables et la valeur de la fonction objectif, soit un vecteur de -1 si le problème est non borné. On donnera aussi le nombre d’itérations de l’algorithme.")

def simplex(M):
    iterations = 0
    Ms = varEcart(M)
    i = iPivot(Ms)
    j = jPivot(Ms)
    print("Matrice de Base :")
    afficher(Ms)
    while i >= 0 and j >= 0:
        iterations += 1
        echelRed(Ms, i, j)
        i = iPivot(Ms)
        j = jPivot(Ms)
        print("\nPivot en ("+str(i+1)+","+str(j+1)+") :")
        afficher(Ms)
    
    if j == -1:
        print("\nSolution en",iterations," itérations :")
        sol = solBase(Ms)
        print(solBaseObj(Ms))
        return sol
    if i == -1:
        print("Problème non borné")
        return None
    print("Pas de solution")
    return None

print("(2) Utiliser la fonction simplexe pour résoudre le problème de l’exercice 1.")

M = [
    [4, 4, 8, 2],
    [1, -3, 5, 3],
    [3, 7, -3, 0],
    [-1, 2, 3, -2]
]
print(simplex(M))

print("(3) Tester l’algorithme sur un problème non borné.")

T = [
    [1, -1, 1, 0, 2],
    [-2, 1, 0, 1, 2],
    [1, 2, 0, 0, 0]
]
print(simplex(T))
    