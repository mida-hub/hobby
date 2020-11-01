from decimal import Decimal

def IsCollinear(a, b, c):
    a0 = Decimal(str(a[0]))
    a1 = Decimal(str(a[1]))
    b0 = Decimal(str(b[0]))
    b1 = Decimal(str(b[1]))
    c0 = Decimal(str(c[0]))
    c1 = Decimal(str(c[1]))

    ab = ((b0 - a0) ** Decimal('2') + (b1 - a1) ** Decimal('2')) ** Decimal('0.5')
    ac = ((c0 - a0) ** Decimal('2') + (c1 - a1) ** Decimal('2')) ** Decimal('0.5')
    bc = ((c0 - b0) ** Decimal('2') + (c1 - b1) ** Decimal('2')) ** Decimal('0.5')

    # ab = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    # ac = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5
    # bc = ((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2) ** 0.5

    # print(ab)
    # print(ac)
    # print(bc)

    if any([(ab + ac == bc),
            (ab + bc == ac),
            (ac + bc == ab)]):
        return True
    else:
        return False

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
    # print(v)
    a = [xn[v[0]], yn[v[0]]]
    b = [xn[v[1]], yn[v[1]]]
    c = [xn[v[2]], yn[v[2]]]
    # print(a, b, c)
    # print(IsCollinear(a, b, c))
    isExist = IsCollinear(a, b, c)
    if isExist:
        break

if isExist:
    print('Yes')
else:
    print('No')
