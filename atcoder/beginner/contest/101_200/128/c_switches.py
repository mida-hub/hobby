# inputの収集
n ,m = map(int, input().split())
km = []

for i in range(m):
    sn = [0] * n
    for j, s in enumerate(map(int, input().split())):
        if j == 0:
            continue
        sn[s-1] = 1
        # print(j, s)
    # print(sn)
    km.append(sn)

pm = list(map(int, input().split()))

# print(n)
# print(m)
# print(km)
# print(pm)

total = 0

# bit全探索
for i in range(2 ** n):
    is_ok = True
    switch = [0] * n

    # フラグ作成
    for j in range(n):
        if ((i >> j) & 1):
            # print(i, j)
            switch[j] = 1

    # スイッチon/offごとに電球の判定
    for km_index, ki in enumerate(km):
        # print('-'*20)
        sub_total = 0
        # 関連するスイッチonの個数を計算
        for k_index, k in enumerate(ki):
            # print(k * switch[k_index])
            sub_total += k * switch[k_index]
        # piとの判定
        if sub_total % 2 != pm[km_index]:
            is_ok = False
            break
    # 全部点灯している
    if is_ok:
        total += 1

print(total)
