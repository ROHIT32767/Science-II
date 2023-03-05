import matplotlib.pyplot as plt
import numpy as np

A = 106
C = 1283
M = 6075

I = np.zeros(1000)

I[0] = 1

for i in range(1,1000):
    I[i] = (I[i-1]*A + C)%M

plt.scatter(I[0:999],I[1:1000])
plt.xlabel("I(j)")
plt.ylabel("I(j+1)")
plt.title("I(j+1) vs I(j)")
plt.show()