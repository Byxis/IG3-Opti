#Exercice 1

M = [
    [4, 4, 8, 2],
    [1, -3, 5, 3],
    [3, 7, -3, 0],
    [-1, 2, 3, -2]
]

def afficher(T : list):
    for row in T:
        print("[", end="")
        print(" ".join(f"{val:>5}" for val in row), end = "")
        print("]")

print("\nM : ")
afficher(M)

def varEcart(T : list):
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

def base(Ts):
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

#Exercice 2

def solBase(Ts):
    B = base(Ms)
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

def solBaseObj(Ts):
    S = solBase(Ts)
    maxf = 0

    for i in range(len(Ts[-1])-1):
        maxf += S[i]*Ts[-1][i]
    maxf -= Ts[-1][-1]
    return maxf

maxf = solBaseObj(Ms)
print("\nmaxf :")
print(maxf)

#TEST

Test = [
    [4, 0, 3, 1, 4],
    [2, 1, 2, 0, 2],
    [1, 0, 4, 0, -1]
]

print(base(Test))
print(solBase(Test))
print(solBaseObj(Test))


def echanger(i, j, B):
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

Test = [
    [1, 1, 1, 0, 2],
    [2, -1, 0, 1, 1],
    [2, 1, 0, 0, 0]
]

#B attendu : [-1, -1, 0, 1]
assert base(Test) == [-1, -1, 0, 1]

#B échangé en (1,0) attendu : [1, -1, 0, -1]
assert echanger(1, 0, base(Test)) == [1, -1, 0, -1]

print("\n\n")
#Exercice 3


def echelRed(M, i, j):
    pivot = M[i][j]
    for k in range(len(M[0])):
        M[i][k] /= pivot

    for l in range(len(M)):
        if l != i:
            factor = M[l][j]
            for k in range(len(M[0])):
                M[l][k] -= factor * M[i][k]

afficher(Test)
echelRed(Test, 0, 1)
print("\n")
afficher(Test)


print("\n\n")
#Exercice 4


def jPivot(M):
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

def iPivot(M):
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


#Exercice 5

def simplex(M):
    Ms = varEcart(M)
    i = 0
    j = 0
    print("Matrice de Base :")
    afficher(Ms)
    while i >= 0 and j >= 0:
        i = iPivot(Ms)
        j = jPivot(Ms)
        if i >= 0 and j >= 0:
            echelRed(Ms, i, j)
            print("\nPivot en ("+str(i+1)+","+str(j+1)+") :")
            afficher(Ms)
    
    print("\nSolution :")
    sol = solBase(Ms)
    print(solBaseObj(Ms))
    return sol

print(simplex(M))
    