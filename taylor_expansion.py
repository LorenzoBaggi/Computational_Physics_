import numpy as np
import matplotlib.pyplot as plt


# we expand a continous function as an infinite series of polynomials

def exptaylor(x, x0, nmax):
    # x: argument
    # x0: argument at which the derivative will be calculated
    # nmax: n at which the series will break
    t = 0
    for n in range(nmax + 1):
        t = t + np.exp(x0) * (x - x0) ** n / np.math.factorial(n)
    return t


n_max = 5
x_list = np.linspace(-5, 5, 101)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-5, 100])
plt.scatter(x_list, np.exp(x_list))
plt.plot(x_list, exptaylor(x_list, 0, n_max), 'blue')
plt.plot(x_list, exptaylor(x_list, -2, n_max), 'green')
plt.plot(x_list, exptaylor(x_list, 2, n_max), 'red')
plt.show()
