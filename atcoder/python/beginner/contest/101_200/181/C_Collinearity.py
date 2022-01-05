def IsCollinear(a, b, c):
    a0 = a[0]
    a1 = a[1]
    b0 = b[0]
    b1 = b[1]
    c0 = c[0]
    c1 = c[1]

    b0 -= a0
    b1 -= a1
    c0 -= a0
    c1 -= a1

    return b0 * c1 == b1 * c0

n = int(input())
xn = []
yn = []
for i in range(n):
    x, y = map(int, input().split())
    xn.append(x)
    yn.append(y)

import itertools

c_list = [x for x in range(n)]

isExist = False
for v in itertools.combinations(c_list, 3):
    a = [xn[v[0]], yn[v[0]]]
    b = [xn[v[1]], yn[v[1]]]
    c = [xn[v[2]], yn[v[2]]]
    isExist = IsCollinear(a, b, c)
    if isExist:
        break

if isExist:
    print('Yes')
else:
    print('No')
