"""
This script implements the functionality of the whole task 1.2

Each subtask is plotted in its own figure so everytime one is closed the
next one opens to show the result.

Only works with the module plot_me present.
"""
import numpy as np
import matplotlib.pyplot as plt

from plot_me import get_x_y # convenience

# ------------------------------------------------------------------------------
# Task 1.2.1: Crossed Out
# ------------------------------------------------------------------------------
# since the functions are rather simple we can implement them as lambdas
y1 = lambda x: 2*x - 2
y2 = lambda x: -2*x + 6
y3 = lambda x: -0.25*(x - 2)**2 + 2
y4 = lambda x: 0.25*(x - 2)**2 + 2

# 100 should be enough for a rather smooth curve
x = np.linspace(-4, 8, 100)

# and plot them all. We could have done that in one plot function, but I prefer
# the longer version.
fig = plt.figure()
plt.title("Crossed Out") # they all meet in one point :)
plt.plot(x, y1(x))
plt.plot(x, y2(x))
plt.plot(x, y3(x))
plt.plot(x, y4(x))
plt.show()

# ------------------------------------------------------------------------------
# Task 1.2.2: Markers All Around
# ------------------------------------------------------------------------------
fig = plt.figure()
# draw the sample from a normal distribution, with center 0 and std 5
# we want a 1d array with 10000 entries
y = np.random.normal(0, 5, (10000))
plt.title("Markers All Around")
# and plot the thing. bins as an integer automatically divides the whole range
# into evenely spaced bins. rwidth as .9 so they are cleared distinguishable
plt.hist(y, bins=25, rwidth=.9)
plt.show()

# ------------------------------------------------------------------------------
# Task 1.2.3: Who Is That Plot
# ------------------------------------------------------------------------------
fig = plt.figure()
x, y = get_x_y() # get the data from the supplied function
plt.title("Who Is That Plot?!") # it's a pikachu!
# setting the scale makes it more visible as the dots are very close
plt.scatter(x, y, s=0.5)
plt.show()
