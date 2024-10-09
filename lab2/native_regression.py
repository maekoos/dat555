from matrix import *
import sys
import matplotlib.pyplot as plt

m = transpose(loadtxt(sys.argv[1]))
X = m[0]
Y = m[1]


Xp = powers(X, 0, 1)
Yp = powers(Y, 1, 1)
Xpt = transpose(Xp)

[[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))


plt.plot(X, Y, 'ro')
Y2 = []
for x in X:
    Y2.append(b+x*m)

plt.plot(X, Y2)
plt.show()
