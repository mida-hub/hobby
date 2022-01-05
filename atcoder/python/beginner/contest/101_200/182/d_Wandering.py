n = int(input())
an = list(map(int, input().split()))

p = 0   # 座標の変化
q = 0   # 開始から終了までの最大値
r = 0   # 座標の最大値
x = 0   # 動作結果
for i in range(n):
    p += an[i]
    q = max([p, q])
    r = max([r, x + q])
    x += p

    # print('-'*10)
    # print(f'a:{an[i]}')
    # print(f'p:{p}')
    # print(f'q:{q}')
    # print(f'r:{r}')
    # print(f'x:{x}')

print(r)
