# coding:utf-8
"""
format b で 2進数展開
zfillで0埋め
"""
print(12)
print(format(12, 'b').zfill(8))
print(21)
print(format(21, 'b').zfill(8))

print('-'*30)

print(format(12 & 21, 'b').zfill(8))
print(12 & 21)
print(format(12 | 21, 'b').zfill(8))
print(12 | 21)

print('-'*30)

print(5)
print(format(5, 'b').zfill(8))
print(5 >> 1)
print(format(5 >> 1, 'b').zfill(8))
print(5 << 1)
print(format(5 << 1, 'b').zfill(8))