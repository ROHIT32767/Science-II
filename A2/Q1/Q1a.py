import matplotlib.pyplot as plt
import numpy as np

A = 106
C = 1283
M = 6075

I = np.zeros(1000)

I[0] = 1

for i in range(1,1000):
    I[i] = (I[i-1]*A + C)%M

plt.plot(range(1,1001),I)
plt.xlabel("j")
plt.ylabel("I(j)")
plt.title("I(j) vs j")
plt.show()