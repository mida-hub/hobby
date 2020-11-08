import numpy as np
n = int(input())
an = np.array(list(map(int, input().split())))
max_a_n = np.zeros(len(an))
rui = np.zeros(len(an))

total = 0
max_point = 0
for i, a in enumerate(an):
    if i == 0:
        rui[i] = a
        total = a
        max_a_n[i] = max([0, a])
        if total > 0:
            max_point = total
    else:
        rui[i] = rui[i-1] + a
        max_a_n[i] = an[0:i+1].sum()
        if total + max_a_n.max() > total:
            max_point = total + max_a_n.max()
        # print(max_point)
        # print(max_a_n, max_a_n.max())
        total += rui[i].sum()
        # print(total)
        # print(max_a_n)
# print(rui)
# print(total)
print(int(max_point))
