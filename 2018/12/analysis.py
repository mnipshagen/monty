"""
Plots reaction time against distance to stimulus with data read from a file.

Reads in data from a file named `experiment.csv`, which needs to supply the
field values `circle_x` and `circle_y` which give the stimulus position, and
`reaction_time` for the reaction time in milliseconds.

It then calculates the distance from the center to the stimulus and plots the
reaction time against the calculated distance. It assumues that the distance
is in pixels.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# get the csv data and calculate the distance.
# saving it in a new column for accessability
df = pd.read_csv("experiment.csv")
df['dist'] = np.sqrt(df['circle_x']**2 + df['circle_y']**2)

# on to the plot
fig, ax = plt.subplots() # subplots defaults to a single plot
# reactiontime over distance
ax.scatter(df['dist'], df['reaction_time'])
ax.set_xlabel("distance in pixels")
ax.set_ylabel("reaction time in ms")

plt.show()