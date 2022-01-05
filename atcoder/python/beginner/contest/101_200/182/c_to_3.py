n = input()
n_len = len(n)

min_era = 2 ** 10
is_baisuu = False

for i in range(1, 2 ** n_len):
    baisuu = []
    # print(f'i: {i}')
    for j in range(n_len):
        if ((i >> j) & 1):
            # print(n[j])
            baisuu.append(n[j])
    # print(baisuu)
    tmp_baisuu = int(''.join(baisuu))
    if tmp_baisuu % 3 == 0:
        is_baisuu = True
        tmp_era = n_len - len(baisuu)
        if min_era > tmp_era:
            min_era = tmp_era

if is_baisuu:
    print(min_era)
else:
    print(-1)
