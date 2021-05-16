n = int(input())
an = []
bn = []
for i in range(n):
    a, b = map(int, input().split())
    an.append(a)
    bn.append(b)

total = 0
for i in range(n):
    total += (an[i] + bn[i]) * (bn[i] - an[i] + 1) // 2

print(total)
