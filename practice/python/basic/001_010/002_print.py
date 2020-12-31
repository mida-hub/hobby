value = 5
print(f'3桁でゼロ埋めしたいとき: {value:03}')

value = 12345678
print(f'3桁ずつカンマ区切りしたいとき: {value:,}')

value = '右寄せ'
print(f'8桁で: {value:_>8}')

value = '左寄せ'
print(f'8桁で: {value:_<8}')

value = '中央'
print(f'8桁で: {value:_^8}')