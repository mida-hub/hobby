import pandas as pd

df = pd.read_csv('input/item_stock.csv', encoding='utf-8', header=0)

print(f'df')
print(df)

print()

print(f'df.T')
print(df.T)

print()

print(f'df.shape')
print(df.shape)

print()

print(f'df.values')
print(df.values)
