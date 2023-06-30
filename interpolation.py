import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


def correct_function(x):
    return 15 + 2.4 * x - 0.5 * x ** 2 - 0.35 * x ** 3


n_points = 21
x_list = np.linspace(-5, 5, n_points)
data0 = np.array([x_list, correct_function(x_list)])
data = np.array([data0[0] + 0.25 * np.random.rand(n_points) - 1, data0[1] + 5 * np.random.rand(n_points) - 1])

plt.figure(1)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data0[0], data0[1], 'black')
plt.scatter(data[0], data[1])
plt.show()

spline_linear_0 = interpolate.interp1d(data0[0], data0[1], kind='linear')
# try also kind = 'cubic' to have cubic splines

plt.figure(2)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data0[0], data0[1], 'black')
plt.scatter(data0[0], spline_linear_0(data0[0]))
plt.show()

plt.figure(3)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([2, 4])
plt.ylim([-5, 15])
plt.plot(data0[0], data0[1], 'black')
plt.scatter(data0[0], spline_linear_0(data0[0]))
plt.show()

spline_cubic = interpolate.interp1d(data[0], data[1], kind='cubic')
# try also kind = 'cubic' to have cubic splines

plt.figure(4)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[0], data[1], 'black')
plt.scatter(data[0], spline_cubic(data[0]))
plt.show()

spline_smooth = interpolate.UnivariateSpline(data[0], data[1])
spline_smooth.set_smoothing_factor(50)

plt.figure(5)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[0], data[1], 'black')
plt.scatter(data[0], spline_smooth(data[0]))
plt.show()

datapoly = data[:, 7:14]  # hence, seven degrees of freedom
X = np.transpose(
    np.array(
        [datapoly[0, :]**0, datapoly[0, :]**1, datapoly[0, :]**2,
             datapoly[0, :]**3, datapoly[0, :]**4,
             datapoly[0, :]**5, datapoly[0, :]**6]
    )
)

y = datapoly[1, :]
a = np.linalg.solve(X, y)
x_list = np.linspace(-2.5, 2.5, 901)
y_list = a[0]*x_list**0 + a[1]*x_list**1 + a[2]*x_list**2 + \
         a[3]*x_list**3 + + a[4]*x_list**4 + + a[5]*x_list**5 + \
         a[6]*x_list**6


plt.figure(6)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim([0, 30])
plt.scatter(datapoly[0], datapoly[1])
plt.plot(x_list, y_list)
plt.show()