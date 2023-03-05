import numpy as np
import matplotlib.pyplot as plt

def integrand(x):
    return np.exp(x) * np.cos(x)

def integration(func, a, b, N):
    x = np.random.uniform(a, b, N)
    y = func(x)
    area = (b - a) * np.mean(y)
    return area

a= -np.pi/2
b = np.pi/2
N = 100000
N_vals = [1] 
arr = np.arange(1000, 100001, 1000)
# print(arr)
N_vals = np.concatenate((N_vals, arr))
# print(N_vals)
results = [integration(integrand, a, b, N) for N in N_vals]

plt.plot(N_vals, results)
plt.xlabel('N')
plt.axhline(y = 2.509178478658057, color ="red", linestyle ="--")
plt.ylabel('Integration value')
plt.show()