# x + y = 4
# 2x - y = 2
# one answer x = 2, y = 2

# 2x + y = 6
# 4x + 2y = 10
# no answer

# 3x + 2y = 12
# 6x + 4y = 24
# unlimited answers

import matplotlib.pyplot as plt
import numpy 

def plot_system(eq1, eq2, title):
    x = np.linspace(-10, 10, 400)
    y1 = eq1(x)
    y2 = eq2(x)

    plt.figure()
    plt.plot(x, y1, label='first mishvaa')
    plt.plot(x, y2, label='second mishvaa')
    plt.title(title)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

plot_system(lambda x: -x + 4, lambda x: 2*x - 2, "first targil: one answer")

plot_system(lambda x: -2*x + 6, lambda x: -2*x + 5, "second targil: no answer")

plot_system(lambda x: -1.5*x + 6, lambda x: -1.5*x + 6, "third targil: unlimited answer")