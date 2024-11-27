import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

x = np.linspace(0, 5, 100)
y = f(x)


print("строим график")
plt.plot(x,y, '--r')
plt.show()