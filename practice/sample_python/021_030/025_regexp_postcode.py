import re

text = input('郵便番号:')

match = re.search(r'^\d{3}-\d{2,4}$', text)

if match is not None:
    postcode = match.group(0)
    print(f'{postcode} は正しい郵便番号のフォーマットです')
    # print(match)
else:
    print(f'{text} は不正な郵便番号フォーマットです')