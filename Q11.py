import numpy as np

# set of 5 data points (t,y)
data = [(-1, 1), (-0.5, 0.5), (0, 0), (0.5, 0.5), (1, 2)]

# create matrices A and Y
A = np.array([[t**2, t, 1] for t, y in data])
Y = np.array([y for t, y in data])

# find the coefficients using matrix multiplication
coefficients = np.linalg.inv(A.T @ A) @ A.T @ Y

print(coefficients)