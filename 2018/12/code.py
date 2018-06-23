import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


population_dict = {'Germany': 80716000, 'France': 67210000, 'UK': 64100000, 'Sweden': 10004962}
area_dict = {'Germany': 357168, 'France': 643801, 'UK': 243610, 'Sweden': 449964}

population = pd.Series(population_dict)
area = pd.Series(area_dict)

df = pd.DataFrame({'population': population, 'area': area})

# print(population, population['Germany'], population['France':'UK'], sep="\n")
# print(df, df['area'], df.loc['France'], sep="\n\n")
# print(type(df['population']))

peter = {'name': 'Peter', 'fav_colour': 'blue'}
susan = {'name': 'Susan', 'fav_colour': 'green', 'pet': 'Oscar'}
df = pd.DataFrame([peter, susan])
# print(df)

df = pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 42, True])
# print(df, df.columns, df.values, df.index, sep="\n")

idx = pd.Index(['a', 'b', 'c']) # stick to one
# print(idx[1], idx[0:1:-1], idx.shape, idx.dtype)
idx = pd.Index([1, 2, 'dog']) # don't mix ints and strings
# idx[2] = 3 # oh no index is immutable

df = pd.DataFrame({'population': population, 'area': area})
# print(df.head())
# print(df.size, df.shape, df.T)
# print(df.info(), "\n")
# print(df.area.describe())


a = np.arange(16).reshape(4, 4)
# print(a)
# Takes those values of the second and fourth column that are divisible by 3
# print(a[:, [1, 3]][a[:, [1, 3]] % 3 == 0])


data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
# print(data)
# print('b' in data)
# print(data.keys() == data.index)
# print(list(data.items()))
data['e'] = 1.25
# print(data)

# print(data['a':'c']) # explicit: inclusive slice
# print(data[0:2]) # implicit: exclusive slice
# print(data[['a','e']]) # fancy!
data.index = [1, 2, 3, 4, 5]
# print(data[1])
# print(data[0:2])

# print(data, "\n")
# print(data.loc[1],
#     data.loc[1:3], "\n",
#     data.iloc[1],
#     data.iloc[1:3])

population_dict = {'Germany': 80716000, 'France': 67210000, 'UK': 64100000, 'Sweden': 10004962}
population = pd.Series(population_dict)
area_dict = {'Germany': 357168, 'France': 643801, 'UK': 243610, 'Sweden': 449964}
area = pd.Series(area_dict)

df = pd.DataFrame({'population': population, 'area': area})
# print(df['area'])
# print(df['Germany':'UK'])

# print(df.iloc[1:3, :2])
# print(df.loc['France':'Sweden', :'area'], "\n")
# print(df.loc['UK', :])

print(df['area'] > 400000)
print(df[df['area'] > 400000])