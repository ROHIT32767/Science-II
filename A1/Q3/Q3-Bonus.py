import numpy as np
import matplotlib.pyplot as plt
N = 500
M = np.random.normal(loc=0, scale=1, size=(500, 500))

# Plot eigenvalues for different values of D
# for D in [1]:
    # Add diagonal elements to matrix
for D in [0,1,5,10]:
    N = (M - M.T)/2
    np.fill_diagonal(N, -D)
    eigenvalues = np.linalg.eigvals(N)
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues))
plt.xlabel("Real(λ)")
plt.ylabel("Imag(λ)")
plt.title("When M is correlated & skew-symmetric and D = 0")
plt.legend()
plt.show()