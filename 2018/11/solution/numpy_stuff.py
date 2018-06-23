import numpy as np


a = np.array([1, 2, 3])
b = np.array([-1, 2, -3])
c = np.arange(1, 10).reshape(3, 3)
d = np.array([[1, 2], [-2, -1], [5, 5]])

print(
    f"a: {a}", f"b: {b}", f"c:\n{c}", f"d:\n{d}",
    f"dot(a, b): {np.dot(a, b)}",
    f"dot(c, a): {np.dot(c, a)}",
    f"c * d:\n{np.matmul(c, d)}",
    f"d^T * c^T:\n{np.matmul(d.T, c.T)}",
    f"mean(a, b): {np.mean([a,b]): .3f}",
    sep="\n"
)