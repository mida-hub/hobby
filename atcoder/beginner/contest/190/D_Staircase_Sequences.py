"""
解説より
https://www.youtube.com/watch?v=VXm-9nBgQG0&feature=youtu.be

初項s, 長さl
総和は平均 * l

平均は(初項 + 末項) / 2

末項は s + l - 1 なので
平均は(2s + l - 1) / 2

総和は (2s + l - 1) * l / 2 = n
(2s + l - 1) * l = 2 * n

l > 0 より
2s + l - 1 = 2 * n / l
2s = 2 * n / l - l + 1
s = (2 * n / l - l + 1) / 2

右辺が整数になる
2 * n / l - l + 1 が 偶数になる
2 * n / l に着目すると
l は 2 * n の約数

方針としてlを試していく
O(sqrt(n))
"""

n = int(input())

total = 0
for i in range(1, int((2 * n) ** 0.5) + 1):
    # iが2*nの約数か、かつ2 * n / i - i + 1が偶数か
    if 2 * n % i == 0 and (2 * n / i - i + 1) % 2 == 0:
        total += 1
# マイナス項を考慮して * 2
print(total * 2)
