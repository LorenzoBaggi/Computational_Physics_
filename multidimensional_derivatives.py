import numpy as np


def gradient(f, vector, step):
    x, y, z = vector
    h = step
    partial_x = (f(np.array([x + h, y, z])) - f(np.array([x - h, y, z]))) / (2 * h)
    partial_y = (f(np.array([x, y + h, z])) - f(np.array([x, y - h, z]))) / (2 * h)
    partial_z = (f(np.array([x, y, z + h])) - f(np.array([x, y, z - h]))) / (2 * h)
    return np.array([partial_x, partial_y, partial_z])


r = np.array([0.5, -1.2, -8])
step_size = 0.0001


def divergence(g, vector, step):
    x, y, z = vector
    h = step
    dgxdx = (g(np.array([x + h, y, z]))[0] - g(np.array([x - h, y, z]))[0]) / 2 / h
    dgydy = (g(np.array([x, y + h, z]))[1] - g(np.array([x, y - h, z]))[1]) / 2 / h
    dgzdz = (g(np.array([x, y, z + h]))[2] - g(np.array([x, y, z - h]))[2]) / 2 / h
    return dgxdx + dgydy + dgzdz

def curl(g, vector, step):
    pass


