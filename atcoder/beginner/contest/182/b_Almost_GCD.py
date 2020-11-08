import numpy as np
n = int(input())
an_org = np.array(list(map(int, input().split())))

max_sum = 0
max_gcd = 0
for i in range(2, max(an_org)+1):
    an = an_org
    tmp_sum = sum(an % i == 0)

    if tmp_sum > max_sum:
        max_sum = tmp_sum
        max_gcd = i

print(max_gcd)
