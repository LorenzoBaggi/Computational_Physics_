import numpy as np
import matplotlib.pyplot as plt


def correct_function(x):
    return 15 + 2.4 * x - 0.5 * x ** 2 - 0.35 * x ** 3


n_points = 21
x_list = np.linspace(-5, 5, n_points)
data0 = np.array([x_list, correct_function(x_list)])
data = np.array([data0[0] + 0.25 * np.random.rand(n_points) - 1, data0[1] + 5 * np.random.rand(n_points) - 1])
a0 = np.array([-2, 2.4, -0.5, -0.35])


def polynomialModel(x, a):
    t = 0
    for k in range(len(a)):
        t = t + a[k] * x ** k
    return t


plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_list, polynomialModel(x_list, a0), 'black')
plt.show()


def errorFit(f, coefficients, data):
    # f: the fit function
    # coefficients: the values that we try to optimize
    # data: data we try to fit
    error = 0
    for i in range(len(data[0])):
        error = error + (data[1, i] - f(data[0, i], coefficients)) ** 2
    return error


def errorFitGradient(f, coefficients, vals):
    # f: the fit function
    # coefficients: the values that we try to optimize
    # data: data we try to fit
    return -2 * np.array([
        np.sum(np.array([(vals[1, i] - f(vals[0, i], coefficients)) * vals[0, i] ** k for i in range(len(vals[0]))]))
        for k in range(len(coefficients))])


iterations = 1_000
h = 0.0000001
a_guess = np.array([-2, 2, 2, -2])

for _ in range(iterations):
    a_guess = a_guess - h * errorFitGradient(polynomialModel, a_guess, data)

print(a_guess)