"""A simple script to test some numpy functionality"""
import numpy as np


# the arrays we are going to work with
a = np.array([1, 2, 3])
b = np.array([-1, 2, -3])
c = np.arange(1, 10).reshape(3, 3)
d = np.array([[1, 2], [-2, -1], [5, 5]])

# sine none of the results are further needed we do the calculation directy 
# in the output function
# Note that f-strings evaluate the statements in curly braces as python
# statements before converting them to string. Therefore, we can do all the
# numpy calculations inside the f-strings
print(
    f"a: {a}", f"b: {b}", f"c:\n{c}", f"d:\n{d}",
    f"dot(a, b): {np.dot(a, b)}",
    f"dot(c, a): {np.dot(c, a)}",
    f"c * d:\n{np.matmul(c, d)}",
    f"d^T * c^T:\n{np.matmul(d.T, c.T)}",
    f"mean(a, b): {np.mean([a,b]): .3f}",
    sep="\n"
)