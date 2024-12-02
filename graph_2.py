import matplotlib.pyplot as plt
import numpy as np
print("строим график")
def f(x):
    return x**2

def bld():
    x = np.linspace(-5, 5, 100)
    y = f(x)

    plt.plot(x,y, '--r')
    plt.title("x^2")
    plt.minorticks_on()
    plt.grid(which='major')
    plt.grid(which='minor', linestyle = ':')
    
    plt.tight_layout()
    return plt.show()

if __name__ == "__main__":
    bld()