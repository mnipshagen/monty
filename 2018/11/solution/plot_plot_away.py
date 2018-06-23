import numpy as np
import matplotlib.pyplot as plt

from plot_me import get_x_y


y1 = lambda x: 2*x - 2
y2 = lambda x: -2*x + 6
y3 = lambda x: -0.25*(x - 2)**2 + 2
y4 = lambda x: 0.25*(x - 2)**2 + 2

x = np.linspace(-4, 8, 100)

fig = plt.figure()
plt.title("Crossed Out")
plt.plot(x, y1(x))
plt.plot(x, y2(x))
plt.plot(x, y3(x))
plt.plot(x, y4(x))
plt.show()

fig = plt.figure()
y = np.random.normal(0, 5, (10000))
plt.title("Markers all around")
plt.hist(y, bins=25, rwidth=.9)
plt.show()

fig = plt.figure()
x, y = get_x_y()
plt.title("Who is that plot?!")
plt.scatter(x, y, s=0.5)
plt.show()