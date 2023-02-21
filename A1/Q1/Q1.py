import matplotlib.pyplot as plt
import numpy as np
# create matrices A and Y
data = [(-1, 1), (-0.5, 0.5), (0, 0), (0.5, 0.5), (1, 2)]
A = np.array([[t**2, t, 1] for t, y in data])
Y = np.array([y for t, y in data])

# find the coefficients using matrix multiplication
def plot_curve(data, coef):
    t = [point[0] for point in data]
    y = [point[1] for point in data]
    plt.scatter(t, y, color ='b') 
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Least-Squares Curve')
    plt.grid(True)
    plt.xlim(min(t)-1, max(t)+1)
    plt.ylim(min(y)-1, max(y)+1)
    t_values = np.linspace(min(t)-1, max(t)+1, 100)
    plt.plot(t_values, coef[0]*t_values*t_values + coef[1]*t_values + coef[2])
    plt.show()

coefficients = np.linalg.inv(A.T @ A) @ A.T @ Y
print(coefficients)
plot_curve(data, coefficients)