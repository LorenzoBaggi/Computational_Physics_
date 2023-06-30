# implementation of a general function to get the derivative of a function
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return 2*np.sin(x)**2 + x


def first_derivative(f, x, h):
    # f: function
    # x: argument
    # h: step size
    return (f(x+h) - f(x)) / h


def n_derivative(f, x, h, n):
    # f: function
    # x: argument
    # h: step size
    # n: nth derivative
    t = 0
    for k in range(n+1):
        t = t + (-1)**(k + n) * np.math.factorial(n) / np.math.factorial(k) / np.math.factorial(n - k) * f(x + k*h)
        return t / h**n


def taylor_expansion(f, x, x0, nmax, h):
    # f: function
    # x: argument
    # x0: argument at which derivatives are calculated
    # nmax: number of derivatives
    # h: step size
    t = 0
    for n in range(nmax):
        t = t + n_derivative(f, x0, h, n) * (x-x0)**n / np.math.factorial(n)
    return t


nmax = 5
h = 0.1

x_list = np.linspace(-5, 8, 101)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-2, 2])
plt.scatter(x_list, func(x_list))
plt.plot(x_list, taylor_expansion(func, x_list, 0, nmax,  h), 'blue')
plt.plot(x_list, taylor_expansion(func, x_list, 2, nmax,  h), 'green')
plt.plot(x_list, taylor_expansion(func, x_list, -3, nmax,  h), 'red')
plt.show()

