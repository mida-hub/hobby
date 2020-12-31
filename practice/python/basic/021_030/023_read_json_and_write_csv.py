import csv
import locale
import pandas as pd

encoding = locale.getpreferredencoding()
df = pd.read_json('input/train_line.json', encoding='utf-8')
df.to_csv(
            'output/train_line.csv',
            index=False,
            quoting=csv.QUOTE_NONNUMERIC,
            columns=['time', 'destination', 'platform', 'type'],
            header=['時刻', '目的地', 'プラットフォーム', '種別'],
            encoding=encoding
        )
