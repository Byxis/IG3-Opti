import math as m
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Annexe - Fonctions outils

def traceEx2(f, gradF, methode_gradient, x0, p=0.01, e=1E-5, linespacex=[-1, 3], linspacey=[-1, 3]):
        nbFonction = 2
        
        fig = plt.figure(figsize=(18, 12))

        ax1 = fig.add_subplot(121)

        x = np.linspace(linespacex[0], linespacex[1], 400)
        y = np.linspace(linspacey[0], linspacey[1], 400)
        x, y = np.meshgrid(x, y)

        ax1.contour(x, y, f(x, y), 50, cmap='plasma')
        ax1.title.set_text(f'Ligne de niveau de la fonction {nbFonction} avec ϵ = {e} ')


        listPoints = methode_gradient(gradF, x0, p, e)
        print("affichage : \n\n\n")
        for(i,j) in listPoints:
            print(i,j, f(i,j), gradF(i,j))

        points = np.array(listPoints)
        ax1.plot(points[:, 0], points[:, 1], 'ro')

        for i, point in enumerate(points):
            if i < 10:
                ax1.text(point[0], point[1], str(i), fontsize=12, color='red')
            elif  i < 100 and i %10 == 0:
                ax1.text(point[0], point[1], str(i), fontsize=12, color='red') 

        ax2 = fig.add_subplot(122, projection='3d')
        ax2.plot_surface(x, y, f(x, y), cmap='viridis')
        ax2.title.set_text(f'Graphe de la fonction {nbFonction}')

        plt.legend()
        plt.tight_layout()
        plt.savefig(f"ex2-{nbFonction}bis.svg")
        plt.show()

def afficherPoints(points, f, gradF):
    for i, j in points:
        print(f"Point: ({i:.4f}, {j:.4f}), f(i, j): {f(i, j):.4f}, gradF(i, j): ({gradF(i, j)[0]:.4f}, {gradF(i, j)[1]:.4f})")

def traceEx3(f, gradF, methode_gradient, x0, a=0.5, b=0.7, e=1E-5, linespacex=[-1, 3], linspacey=[-1, 3]):
        nbFonction = 2

        fig = plt.figure(figsize=(18, 12))
        ax1 = fig.add_subplot(121)

        x = np.linspace(linespacex[0], linespacex[1], 400)
        y = np.linspace(linspacey[0], linspacey[1], 400)
        x, y = np.meshgrid(x, y)

        ax1.contour(x, y, f(x, y), 50, cmap='plasma')
        ax1.title.set_text(f'Courbes de niveau de la fonction {nbFonction} avec α = {a} et β = {b} ')


        listPoints = methode_gradient(f, gradF, x0, a, b, e)
        print("affichage : \n\n\n")
        for(i,j) in listPoints:
            print(i,j, f(i,j), gradF(i,j))

        points = np.array(listPoints)
        ax1.plot(points[:, 0], points[:, 1], 'ro')
        for i, point in enumerate(points):
            if i < 10:
                ax1.text(point[0], point[1], str(i), fontsize=12, color='red')
            elif  i < 100 and i %10 == 0:
                ax1.text(point[0], point[1], str(i), fontsize=12, color='red') 

        ax2 = fig.add_subplot(122, projection='3d')
        ax2.plot_surface(x, y, f(x, y), cmap='viridis')
        ax2.title.set_text(f'Graphe de la fonction {nbFonction}')

        plt.legend()
        plt.tight_layout()
        plt.savefig(f"ex3-{nbFonction}bis.svg")
        plt.show()


# 1 - Méthode par dichotomie

def Ex1():
    def dichotomie(f, fp, a:float, b:float, eps:float):
        points = []
        while b - a > eps:
            m = (a+b)/2
            points.append((m, f(m), fp(m)))
            if fp(m) >= 0:
                b = m
            else:
                a = m
        points.append((m, f(m), fp(m)))
        return points

    fonction = lambda x: x**2
    fonctionDeriv = lambda x: 2*x

    plt.plot(dichotomie(fonction, fonctionDeriv, -2, 3, 1E-3))
    plt.xlabel('x')
    plt.ylabel('Valeur')
    plt.title('Valeurs de f et f\' associées')
    plt.legend()
    plt.savefig("ex1.svg")
    plt.show()

# 2 - Méthode du gradient

def Ex2() :
    def gradient_pas_fixe(gradF, x0, p, e):
        points = []
        gf = gradF(x0[0], x0[1])
        x = x0
        points.append(x)
        while m.sqrt(gf[0]**2 + gf[1]**2) > e:
            x[0] = x[0] - p*gf[0]
            x[1] = x[1] - p*gf[1]
            points.append([x[0], x[1]])
            gf = gradF(x[0], x[1])

        return points
        
    fonc1 = lambda x1,x2: (x1**2) + 2*(x2**2) + x1*x2 + x1 - x2 + 30
    gradFonc1 = lambda x1,x2: (2*x1 + x2 + 1, 6*(x2**2) + x1 - 1)

    fonc2 = lambda x1,x2 : x1**2 + 10*x2**2
    gradFonc2 = lambda x1,x2 : (2*x1, 20*x2)

    fonc3 = lambda x1,x2 : 2*(x1-4)**2 + 3*(x2-3)**2
    gradFonc3 = lambda x1,x2 : (4*(x1-4), 6*(x2-3))

    while True:
        choix_fonc = input("\nNumero de la fonction (1, 2, 3 ou sortie): ")
        if choix_fonc == '1':
            traceEx2(fonc1, gradFonc1, gradient_pas_fixe, x0=[3,3], p=0.01, e=1, linespacex=[-3, 3], linspacey=[-3, 3])
        elif choix_fonc == '2':
            traceEx2(fonc2, gradFonc2, gradient_pas_fixe, x0=[3,3], p=0.01, e=1, linespacex=[-3, 3], linspacey=[-3, 3])
        elif choix_fonc == '3':
            traceEx2(fonc3, gradFonc3, gradient_pas_fixe, x0=[0,0], p=0.1, e=1E-3, linespacex=[1, 6], linspacey=[1, 6])
        else:
            break

def Ex3():

    def gradient_rebr(f, gradF, x0, a, b, e):
        points = []
        x = x0
        points.append(x)
        gf = gradF(x[0], x[1])
        while m.sqrt(gf[0]**2 + gf[1]**2) > e:
            n = 1
            nfg2 = m.sqrt(gf[0]**2 + gf[1]**2)**2
            while f(x[0]-n*gf[0], x[1]-n*gf[1]) > f(x[0], x[1]) - a*n*nfg2:
                n = n*b
            x[0] = x[0] - n*gf[0]
            x[1] = x[1] - n*gf[1]
            points.append([x[0], x[1]])
            gf = gradF(x[0], x[1])
        return points
    
    fonc1 = lambda x1,x2: (x1**2) + 2*(x2**2) + x1*x2 + x1 - x2 + 30
    gradFonc1 = lambda x1,x2: (2*x1 + x2 + 1, 4*x2 + x1 - 1)

    fonc2 = lambda x1,x2 : x1**2 + 10*x2**2
    gradFonc2 = lambda x1,x2 : (2*x1, 20*x2)

    while True:
        choix_fonc = input("\nNumero de la fonction (1, 2 ou sortie): ")
        if choix_fonc == '1':
            traceEx3(fonc1, gradFonc1, gradient_rebr, x0=[3,3], a=0.1, b=0.7, e=1E-3, linespacex=[-3, 3], linspacey=[-3, 3])
        elif choix_fonc == '2':
            traceEx3(fonc2, gradFonc2, gradient_rebr, x0=[3,3], a=0.1, b=0.7, e=1E-3, linespacex=[-3, 6], linspacey=[-6, 6])
        else:
            break

    while True:
        choix_fonc = input("\nNumero de la fonction (1, 2 ou sortie) avec alpha et beta ayant varié : ")
        if choix_fonc == '1':
            traceEx3(fonc1, gradFonc1, gradient_rebr, x0=[3,3], a=0.1, b=0.7, e=1E-3, linespacex=[-3, 3], linspacey=[-3, 3])
        elif choix_fonc == '2':
            traceEx3(fonc2, gradFonc2, gradient_rebr, x0=[3,3], a=0.1, b=0.7, e=1E-3, linespacex=[-3, 6], linspacey=[-6, 6])
        else:
            break

def gradient_rebr(f, gradF, x0, a, b, e):
        points = []
        x = x0
        points.append(x)
        gf = gradF(x[0], x[1])
        while m.sqrt(gf[0]**2 + gf[1]**2) > e:
            n = 1
            nfg2 = m.sqrt(gf[0]**2 + gf[1]**2)**2
            while f(x[0]-n*gf[0], x[1]-n*gf[1]) > f(x[0], x[1]) - a*n*nfg2:
                n = n*b
            x[0] = x[0] - n*gf[0]
            x[1] = x[1] - n*gf[1]
            points.append([x[0], x[1]])
            gf = gradF(x[0], x[1])
        return points

#fonc1 = lambda x1,x2: (x1**2) + 2*(x2**2) + x1*x2 + x1 - x2 + 30
#gradFonc1 = lambda x1,x2: (2*x1 + x2 + 1, 4*x2 + x1 - 1)
#traceEx3(fonc1, gradFonc1, gradient_rebr, x0=[3,3], a=0.1, b=0.7, e=1E-3, linespacex=[-3, 3], linspacey=[-3, 3])
#traceEx3(fonc1, gradFonc1, gradient_rebr, x0=[3,3], a=0.2, b=0.1, e=1E-3, linespacex=[-3, 3], linspacey=[-3, 3])

while True:
    choix = input("\nNumero de l'exercice (1, 2, 3 ou sortie) : ")
    if choix == '1':
        Ex1()
    elif choix == '2':
        Ex2()
    elif choix == '3':
        Ex3()
    else:
        break

#lien overleaf : https://www.overleaf.com/project/6761553b0618187e0a7c195b