import matplotlib.pyplot as plt
import numpy as np


x_direct = np.array([2.95,1.74,-1.45,1.32])
x_computed = np.array([2.96,1.746,-1.46,1.314])
print(x_computed)

plt.bar(np.arange(4),x_direct,label = "Direct Measurements")
plt.bar(np.arange(4),x_computed,label = "Computed Value")

plt.xlabel("Altitudes (x1,x2,x3,x4)")
plt.ylabel("Values")
plt.ylim([-1.48,3.5])
plt.title("Proximity Between Direct Measurements and Computed Values")

plt.legend()
plt.show()