#Exercice 1

M = [
    [4, 4, 8, 2],
    [1, -3, 5, 3],
    [3, 7, -3, 0],
    [-1, 2, 3, -2]
]

def afficher(T : list):
    for i in range(len(T)):
        print(T[i])

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

#Ex 2

def solBase(Ts):
    B = base(Ms)
    S = []
    for i in range(len(B)):
        if(B[i] != -1):
            S.append(Ts[B[i]][-1])
        else:
            S.append(0)
    return S

sol = solBase(Ms)
print("\nsol :")
print(sol)

def solBaseObj(Ts):
    S = solBase(Ts)
    maxf = 0

    for i in range(len(Ts[-1])-1):
        maxf += S[i]*Ts[-1][i]
    maxf-= Ts[-1][-1]
    return maxf

maxf = solBaseObj(Ms)
print("\nmaxf :")
print(maxf)

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