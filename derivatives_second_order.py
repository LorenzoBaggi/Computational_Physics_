import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) * x - 1 / 100 * x ** 3


x_list = np.linspace(-10, 10, 201)
y_list = f(x_list)

analytical_d2_list = - np.sin(x_list) * x_list + 2 * np.cos(x_list) - 6 / 100 * x_list
h = 0.01
forward_d2_list = (f(x_list + 2 * h) - 2 * f(x_list + h) + f(x_list)) / h**2
backward_d2_list = (f(x_list) - 2 * f(x_list - h) + f(x_list - 2*h)) / h**2
central_d2_list = (f(x_list + h) - 2 * f(x_list) + f(x_list - h)) / h**2

plt.figure(1)
plt.xlabel('x')
plt.ylabel("f''(y)")
plt.plot(x_list, forward_d2_list)
plt.plot(x_list, backward_d2_list)
plt.plot(x_list, central_d2_list)
plt.plot(x_list, analytical_d2_list)
plt.show()

plt.figure(2)
plt.xlabel('x')
plt.ylabel("Error of f''(y)")
plt.plot(x_list, analytical_d2_list - forward_d2_list, 'black')
plt.plot(x_list, analytical_d2_list - backward_d2_list, 'blue')
plt.plot(x_list, analytical_d2_list - central_d2_list, 'green')
plt.show()
