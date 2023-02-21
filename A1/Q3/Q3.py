import numpy as np
import matplotlib.pyplot as plt
M = np.random.normal(loc=0, scale=1, size=(500, 500))
for D in [0,1,5,10]:
    # Add diagonal elements to matrix
    np.fill_diagonal(M, -D)
    eigenvalues = np.linalg.eigvals(M)
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues))
    plt.axvline(x=-D, color='black', linestyle='--', linewidth=0.5)


plt.xlabel("Real(λ)")
plt.ylabel("Imag(λ)")
plt.title("D = 0,1,5,10")
plt.legend()
plt.show()