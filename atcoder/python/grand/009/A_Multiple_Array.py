n = int(input())
an = []
bn = []
for i in range(n):
    a, b = map(int, input().split())
    an.append(a)
    bn.append(b)

# print(n)
# print(an)
# print(bn)

total = 0
for i in reversed(range(n)):
    an[i] += total
    # print(an)
    residue = an[i] % bn[i]
    if residue != 0:
        dn = bn[i] - residue
        total += dn
        an[i] += dn
# print(an)
print(total)
