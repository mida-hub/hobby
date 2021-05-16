n, q = map(int, input().split())
s = input()

lq = [-1] * q
rq = [-1] * q

for i in range(q):
    lq[i], rq[i] = map(int, input().split())

# print(n, q)
# print(s)
# print(lq, rq)

sn = [0] * n
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        sn[i + 1] = sn[i] + 1
    else:
        sn[i + 1] = sn[i]

# print(sn)

for i in range(q):
    print(sn[rq[i] - 1] - sn[lq[i] - 1])


