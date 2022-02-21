n, s, d = map(int, input().split())

result = False

for i in range(n):
    x, y = map(int, input().split())
    if not (x >= s or y <= d):
        result = True

if result:
    print('Yes')
else:
    print('No')
