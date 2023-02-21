import numpy as np
import matplotlib.pyplot as plt
N = 500
M = np.random.normal(loc=0, scale=1, size=(500, 500))

Darray = [0]
for D in Darray:
    np.fill_diagonal(M, -D)
    R = (M + M.T)/2
    eigenvalues = np.linalg.eigvals(R)
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues))
plt.xlabel("Real(λ)")
plt.ylabel("Imag(λ)")
plt.title("When M is real and symmetric and D = 0")
plt.legend()
plt.show()
