# %% imports
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd

# %% get data
df = pd.read_csv('midtermsurvey.csv')

# %%
col = df.columns
hw_difficulty = df[col[6]]
walk_in_used = df[col[9]]
walk_in_used[walk_in_used=='No'] = 0
walk_in_used[walk_in_used=='Yes'] = 1

# %% inspect
