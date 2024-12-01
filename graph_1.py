import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.arcsin(x)

def bld():
    x = np.linspace(-1,1,100)
    y = f(x)

    plt.plot(x,y,"-r")
    plt.title("arcsin(x)")
    plt.minorticks_on()
    plt.grid(which='major')
    plt.grid(which='minor', linestyle = ':')

    plt.tight_layout()
    return plt.show()

if __name__ == "__main__":
    bld()