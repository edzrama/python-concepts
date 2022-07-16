import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('sbux.csv')
print(type(df))

# first ten records
print(df.head(10))
# last ten records
print(df.tail(10))
# shows data type, memory usage
print(df.info())
# display column names
print(df.columns)
# changing column names
df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'name']

print(df[['open', 'close']])
# dataframe columns are series.
print(type(df['open']))

# accessing row in dataframe
print(df.iloc[0])
print(df.loc[0])

df2 = pd.read_csv('sbux.csv', index_col='date')
print(df2)
print(df2.iloc[0])
print(df2.loc['2018-02-05'])
# filter records by column values
print(df[df['open'] > 64])
print(df[df['name'] != 'SBUX'])

import numpy as np

A = np.arange(10)
print(A[A % 2 == 0])

print(df.values)

A = df[['open', 'close']].values
print(A)

smalldf = df[['open', 'close']]


# smalldf.to_csv('output.csv', index=False)


# Apply function
def date_to_year(row):
    return int(row['date'].split('-')[0])

# axis = 0 applies to each column, axis =1 applies to each row
print(df.apply(date_to_year, axis=1))
# add as column year
df['year'] = df.apply(date_to_year, axis=1)
print(df.head())


# plotting with pandas
# df['open'].hist()
# df['open'].plot()
# df[['open', 'high', 'low', 'close']].plot.box()
scatter_matrix(df[['open', 'high', 'low', 'close']], alpha=0.2, figsize=(6, 6))
plt.show()


