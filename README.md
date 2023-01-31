# Assignment-1
# 2021101113
# Science - II
# Gowlapalli Rohit

>##### All these commands are tested on Ubuntu Version 20.04.3 LTS (Focal Fossa) 
```

```
> * Q1

`$ python3 Q1.py`  
```cpp
import matplotlib.pyplot as plt
import numpy as np
data = [(-1, 1), (-0.5, 0.5), (0, 0), (0.5, 0.5), (1, 2)]
A = np.array([[t**2, t, 1] for t, y in data])
Y = np.array([y for t, y in data])

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
```

![Q11.jpg](Q11.jpg)

![Q12.jpg](Q12.jpg)

![Q1.png](Q1.png)
> * Q2

![Q21.jpg](Q21.jpg)

![Q22.jpg](Q22.jpg)

![Q23.jpg](Q23.jpg)
> * Q3

`$ python3 Q3.py`
```cpp
import numpy as np
import matplotlib.pyplot as plt
M = np.random.normal(loc=0, scale=1, size=(500, 500))
for D in [0,1,5,10]:
    # Add diagonal elements to matrix
    np.fill_diagonal(M, -D)
    eigenvalues = np.linalg.eigvals(M)
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues))

plt.xlabel("Real(λ)")
plt.ylabel("Imag(λ)")
plt.show()
```

```cpp
import numpy as np
import matplotlib.pyplot as plt
N = 500
M = np.random.normal(loc=0, scale=1, size=(500, 500))

# Plot eigenvalues for different values of D
# for D in [1]:
    # Add diagonal elements to matrix
D = 1
np.fill_diagonal(M, -D)
M = (M + M.T)/2
eigenvalues = np.linalg.eigvals(M)
plt.scatter(np.real(eigenvalues), np.imag(eigenvalues))
plt.xlabel("Real(λ)")
plt.ylabel("Imag(λ)")
plt.show()
``` 
```cpp
import numpy as np
import matplotlib.pyplot as plt
N = 500
M = np.random.normal(loc=0, scale=1, size=(500, 500))
for D in [0,1,5,10]:
    N = (M - M.T)/2
    np.fill_diagonal(N, -D)
    eigenvalues = np.linalg.eigvals(N)
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues))
plt.xlabel("Real(λ)")
plt.ylabel("Imag(λ)")
plt.show()
```
##### D= 0 
![D0.png](D0.png)
##### D =1 
![D1.png](D1.png)
##### D =5 
![D5.png](D5.png)
##### D = 10 
![D10.png](D10.png)
##### All
![ALl.png](All.png)

> * Q4

`$ python3 Q4.py` 
```cpp
import matplotlib.pyplot as plt
import numpy as np
data = [[1,0,0,0,2.95],[0,1,0,0,1.74],[0,0,1,0,-1.45],[0,0,0,1,1.32],[1,-1,0,0,1.23],[1,0,-1,0,4.45],[1,0,0,-1,1.61],[0,1,-1,0,3.21],[0,1,0,-1,0.45],[0,0,1,-1,-2.75]]
A = np.array([[a,b,c,d] for a,b,c,d,e in data])
Y = np.array([y for a,b,c,t,y in data])
coefficients = np.linalg.inv(A.T @ A) @ A.T @ Y
print(coefficients)
```
