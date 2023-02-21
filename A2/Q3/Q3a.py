import matplotlib.pyplot as plt
import numpy as np
from random import randint

a = -(((2021101113)%5)+1)
b = ((2021101113)%5)+1

P = np.zeros(100)
rounds = 10000

for N in range(100):
    for i in range(rounds):
            count = a
            for j in range(N):
                x = randint(0,1)
                # 1 for +1 and 0 for -1
                count += (2*x-1)
            if(count==0):
                 P[N]=P[N]+1
def Division(num):
    return num/10000.00
vectorize_array = np.vectorize(Division)
plt.plot(range(1,101),vectorize_array(P))
plt.xlabel("N")
plt.ylabel("Probability")
plt.title("Probability vs N")
plt.show()
                  
