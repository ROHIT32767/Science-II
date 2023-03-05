import numpy as np
import matplotlib.pyplot as plt

A = 106
C = 1283
M = 6075

def generate_random_numbers(N):
    I = np.zeros(N)
    I[0] = 1
    for j in range(1, N):
        I[j] = (A * I[j-1] + C) % M
    return I

N_values = [1, 10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
E_I = []
for N in N_values:
    I = generate_random_numbers(N)
    E_I.append(np.mean(I))

plt.plot(N_values, E_I)
plt.xlabel('N')
plt.ylabel('E(I(j))')
plt.title('E(I(j)) vs N')
plt.show()
