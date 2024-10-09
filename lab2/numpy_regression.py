from numpy import *
import sys
import matplotlib.pyplot as plt


def powers(list: list[int], start: int, end: int):
    T = []
    for idx, base in enumerate(list):
        T.append([])
        for exponent in range(start, end+1):
            T[idx].append(base**exponent)
    return array(T)


def poly(a: list[float], x: float):
    y = 0
    for n, coefficient in enumerate(a):
        y += coefficient * x**n

    return y


m = transpose(loadtxt(sys.argv[1]))
X = m[0]
Y = m[1]
n = int(sys.argv[2])

Xp = powers(X, 0, n)
Yp = powers(Y, 1, 1)
Xpt = Xp.transpose()
a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
a = a[:, 0]

plt.plot(X, Y, 'ro')

X2 = linspace(X[0], X[-1], int((X[-1]-X[0])/0.2)).tolist()
Y2 = []
for x in X2:
    Y2.append(poly(a, x))
plt.plot(X2, Y2)

plt.show()
