import collections

n = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))

# print(n, an, bn, cn)

bcn = []

for i in range(len(cn)):
    bcn.append(bn[cn[i]-1])

an_count = collections.Counter(an)
bcn_count = collections.Counter(bcn)
# print(an_count)
# print(bcn_count)

total = 0
for i in range(1, n+1):
    if an_count.get(i) is not None and bcn_count.get(i) is not None:
        total += an_count.get(i) * bcn_count.get(i)

print(total)
