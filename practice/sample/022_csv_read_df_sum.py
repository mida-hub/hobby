import pandas as pd

df = pd.read_csv('input/item_stock.csv', encoding='utf-8', header=0)

sales = sum(df['売上数'])
print(f'売上数合計: {sales}')
