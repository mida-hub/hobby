n = int(input())
an = []
bn = []

for i in range(n):
    a, b = map(int, input().split())
    an.append(a)
    bn.append(b)

result = 10**5+10
for i in range(n):
    for j in range(n):
        if i == j:
            tmp = an[i] + bn[j]
        else:
            tmp = max(an[i], bn[j])
        
        if result > tmp:
            result = tmp
print(result)
