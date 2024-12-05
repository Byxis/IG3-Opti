import math as m
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# 1 - Méthode par dichotomie



def dichotomie(f, a:float, b:float, eps:float):
    points = []
    while b - a > eps:
        m = (a+b)/2
        points.append((m, fonction(m), f(m)))
        if f(m) >= 0:
            b = m
        else:
            a = m
    points.append((m, fonction(m), f(m)))
    return points

fonction = lambda x: x**2
fonctionDeriv = lambda x: 2*x

plt.plot(dichotomie(fonctionDeriv, -2, 3, 1E-3))
plt.xlabel('x')
plt.ylabel('Valeur')
plt.title('Valeurs de f et f\' associées')
plt.legend()



# 2 - Méthode du gradient

def gradient_pas_fixe(F, x0, p, e):
    points = []
    gf = F(x0[0], x0[1])
    x = x0
    points.append(x)
    while m.sqrt(gf[0]**2 + gf[1]**2) > e:
        print("x =",x)
        x[0] = x[0] - p*gf[0]
        x[1] = x[1] - p*gf[1]
        points.append(x)
        gf = F(x[0], x[1])
    print("x =",x)
    return points

fonc1 = lambda x1,x2: (x1**2) + 2*(x2**3) + x1*x2 + x1 - x2 + 30
gradFonc1 = lambda x1,x2: (2*x1 + x2 + 1, 6*(x2**2) + x1 - 1)



fig = plt.figure(figsize=(18, 12))

x = np.linspace(-1, 0, 400)
y = np.linspace(0, 1, 400)
x, y = np.meshgrid(x, y)

ax2 = fig.add_subplot(111)
contour = ax2.contour(x, y, fonc1(x, y), 20, cmap='plasma')
ax2.clabel(contour, inline=True, fontsize=8)
ax2.title.set_text('Courbes de niveau de la fonction 1')


points = gradient_pas_fixe(gradFonc1, [0,0], 0.1, 1E-3)
points = np.array(points)
ax2.plot(points[:, 0], points[:, 1], 'ro-')


plt.legend()
plt.tight_layout()
plt.show()
print(gradient_pas_fixe(gradFonc1, [0,0], 0.1, 1E-3))