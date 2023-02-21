import numpy as np
import matplotlib.pyplot as plt

def integrand(x):
    return np.exp(x) * np.cos(x)

def monte_carlo_integration(func, a, b, N):
    x = np.random.uniform(a, b, N)
    y = func(x)
    area = (b - a) * np.mean(y)
    return area

a, b = -np.pi/2, np.pi/2
N = 100000

result = monte_carlo_integration(integrand, a, b, N)
print(f"Integration value for N={N}: {result}")
