import numpy as np
import matplotlib.pyplot as plt


amps = [4, 2, 1]
periods = [1, 1, 3]
colours = ['red', 'green', 'purple']

xtick = np.arange(-np.pi, np.pi+np.pi/2, np.pi/2)
xlabel = [r'$-\pi$', r'$-\frac{\pi}{2}$',
            r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']

font = {'family': 'Calibri',
        'weight': 'bold',
        'size': 16}

plt.rc('font', **font)
plt.rc('text', usetex=True)

fig = plt.figure("Inspecting Sines")
ax_tl = plt.subplot(221)
ax_tr = plt.subplot(222)
ax_b = plt.subplot(212)


def sine_plotter(amps, periods, colours):
    waves = []
    for i in range(len(amps)):
        a = amps[i]
        T = periods[i]
        colour = colours[i]

        def sine(x_offset, y_offset):
            return a * np.sin(T * (x - x_offset)) + y_offset

        waves.append(sine)
    
    return waves




for subplt in [221, 222, 212]:
    ax = plt.subplot(subplt)
    ax.set_xlim((-np.pi, np.pi))
    ax.grid(True)
    ax.margins(xmargin=0)
    ax.set_xticks(xtick)
    ax.set_xticklabels(xlabel)





def plot_sine(ax, x, amplitude, period, x_offset, y_offset, colour):
    label = f"A: {amplitude}, T: {period}"
    sine = amplitude * np.sin(period * (x - x_offset)) + y_offset
    return ax.plot(x, sine, color=colour, label=label)

x = np.linspace(-np.pi, np.pi, 100)
sines = []
for i in range(len(amps)):
    a = amps[i]
    T = periods[i]
    c = colours[i]

    y = a * np.sin(T * x)
    sines.append(ax.plot(x, y, color=c, label=labelmaker(a, T)))


def animate(i):




for i in range(len(amps)):
    a = amps[i]
    T = periods[i]
    c = colours[i]

    y = a * np.sin(T * x)
    ax.plot(x, y, color=c, label=labelmaker(a, T))

    ax.legend()

plt.show()
