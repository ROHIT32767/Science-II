import matplotlib.pyplot as plt
import numpy as np
# create matrices A and Y
data = [[1,0,0,0,2.95],[0,1,0,0,1.74],[0,0,1,0,-1.45],[0,0,0,1,1.32],[1,-1,0,0,1.23],[1,0,-1,0,4.45],[1,0,0,-1,1.61],[0,1,-1,0,3.21],[0,1,0,-1,0.45],[0,0,1,-1,-2.75]]
A = np.array([[a,b,c,d] for a,b,c,d,e in data])
Y = np.array([y for a,b,c,t,y in data])
coefficients = np.linalg.inv(A.T @ A) @ A.T @ Y
print(coefficients)
