import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) * x - 1 / 100 * x ** 3


x_list = np.linspace(-10, 10, 201)
y_list = f(x_list)

plt.figure(1)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_list, y_list)
plt.show()

analytical_d_list = np.cos(x_list) * x_list + np.sin(x_list) - 3 / 100 * x_list ** 2
h = 0.01
forward_d_list = (f(x_list + h) - f(x_list)) / h
backward_d_list = (f(x_list) - f(x_list - h)) / h
central_d_list = (f(x_list + h) - f(x_list - h)) / 2 / h

plt.figure(2)
plt.xlabel('x')
plt.ylabel("f'(y)")
plt.plot(x_list, forward_d_list)
plt.plot(x_list, backward_d_list)
plt.plot(x_list, central_d_list)
plt.plot(x_list, analytical_d_list)
plt.show()

plt.figure(3)
plt.xlabel('x')
plt.ylabel("Error f'(y)")
plt.plot(x_list, analytical_d_list - forward_d_list, 'blue')
plt.plot(x_list, analytical_d_list - backward_d_list, 'black')
plt.plot(x_list, analytical_d_list - central_d_list, 'green')
plt.show()


def D1Richardson(f, x, h):
    # f: function
    # x: argument
    # h: step size
    return 1 / (12 * h) * (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h))


richardson_d_list = D1Richardson(f, x_list, h)

plt.figure(4)
plt.xlabel('x')
plt.ylabel("Error f'(y)")
# plt.plot(x_list, analytical_d_list - forward_d_list, 'blue')
# plt.plot(x_list, analytical_d_list - backward_d_list, 'black')
plt.plot(x_list, analytical_d_list - central_d_list, 'green')
plt.plot(x_list, analytical_d_list - richardson_d_list, 'red')
plt.show()


def D1nRichardson(nmax, f, x, h):
    # nmax: order of iteration for first derivative
    # f: function
    # x: argument
    # h: step size
    d0 = np.array(
        [
            1 / (12 * h * 2 ** j) * (f(x - 2 * h * 2 ** j) - 8 * f(x - h * 2 ** j) +
                                     8 * f(x + h * 2 ** j) - f(x + 2 * h * 2 ** j)) for j in range(0, nmax)
        ]
    )
    for n in range(1, nmax):
        print(d0)
        d = np.array([(2 ** (2 * n) * d0[j] - d0[j + 1]) / (2 ** (2 * n) - 1) for j in range(0, len(d0) - 1)])
        d0 = d
    return d
