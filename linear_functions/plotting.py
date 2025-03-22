import matplotlib.pyplot as plt
import numpy as np

def plot_linear_function(a, b, x_range=(-10, 10)):
    """Rysuje wykres funkcji liniowej y = ax + b."""
    x = np.linspace(x_range[0], x_range[1], 400)
    y = a * x + b
    plt.plot(x, y, label=f'y = {a}x + {b}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()