import numpy as np
import matplotlib.pyplot as plt


# we expand a continous function as an infinite series of polynomials

def sin_taylor(x, nmax):
    # x: argument
    # nmax: n at which the series will break
    t = 0
    for n in range(nmax + 1):
        t = t + (-1) ** n * x ** (2 * n + 1) / np.math.factorial(2 * n + 1)
    return t


x_list = np.linspace(-10, 10, 101)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-2, 2])
plt.scatter(x_list, np.sin(x_list))
plt.plot(x_list, sin_taylor(x_list, 3), 'blue')
plt.plot(x_list, sin_taylor(x_list, 6), 'green')
plt.plot(x_list, sin_taylor(x_list, 9), 'red')
plt.show()
