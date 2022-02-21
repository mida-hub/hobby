n, q = map(int, input().split())
an = list(map(int, input().split()))
kq = []

an_count_less = []

a_min = an[0]
a_max = an[n-1]

# print(a_min, a_max)

for i in range(q):
    k = int(input())
    kq.append(k)

for i in range(n):
    a = an[i]
    if i == 0:
        an_count_less.append(a-1)
    else:
        an_count_less.append(a - an[i-1] + an_count_less[i-1] - 1)
an_count_less_min = an_count_less[0]
an_count_less_max = an_count_less[n-1]
# print(an_count_less)

import bisect
for k in kq:
    # print(k)
    if k < a_min:
        print(k)
        continue
    if k > a_max:
        print(k+n)
        continue
    
    bi_left = bisect.bisect_left(an_count_less, k)
    # print(f'bi_left:{bi_left}')

    if bi_left > an_count_less_max:
        print(an[n-1]+k-an_count_less_max)
    else:
        print(an[bi_left-1]+k-an_count_less[bi_left-1])
