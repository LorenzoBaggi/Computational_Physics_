import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return 0.5 + 0.1 * x + 0.2 * x**2 + 0.03 * x**3


x_list = np.linspace(-3.5, 3.5, 71)

# plt.figure()
# plt.plot(x_list, func(x_list))
# plt.show()

x_points = np.linspace(-3, 3, 13)
data = np.array([x_points, func(x_points)])

# plt.figure()
# plt.scatter(data[0], data[1])
# plt.show()


def integralSum(data):
    return np.sum(data[1]) * (data[0, -1] - data[0, 0]) / (len(data[1]) - 1)


res = integralSum(data)
print(f"The result of integralSum is: {res:.5f}")


def integralTrapezoidal(data):
    a = 0
    for i in range(len(data[0]) - 1):
        a = a + (data[1, i + 1] + data[1, i]) / 2 * (data[0, i + 1] - data[0, i])
    return a


res = integralTrapezoidal(data)
print(f"The result of integralTrapezoidal is: {res:.5f}")


def integralTrapezoidalEQ(data):
    return ( 1/2 * data[1, 0] + np.sum(data[1, 1:-1]) + 1/2 * data[1, -1]) * (data[0, -1] - data[0, 0]) / (len(data[1]) - 1)


res = integralTrapezoidal(data)
print(f"The result of integralTrapezoidalEQ is: {res:.5f}")