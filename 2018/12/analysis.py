import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("example.csv")
df['dist'] = np.sqrt(df['circle_x']**2 + df['circle_y']**2)

print(df)

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df['dist'], df['reaction_time'])
ax.set_xlabel("distance in pixels")
ax.set_ylabel("reaction time in ms")

plt.show()

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df['circle_x'], df['circle_y'])
ax.set_ylim(-384, 384)
ax.set_xlim(-512, 512)

plt.show()