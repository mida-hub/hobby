import pandas as pd

dtype = {'name': 'object', 'number': 'int8'}
df = pd.read_csv('in_sample.csv', dtype=dtype)
print(df.head())
# print(df.dtypes)
# print(df.memory_usage(index=False))

df['number'] = df['number'] + 3
print(df.head())

numbers = df.number
numbers += 3

df['number'] = numbers
print(df.head())
