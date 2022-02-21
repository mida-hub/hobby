coin = []
tmp = 1
for i in range(1, 11):
    tmp *= i
    coin.append(tmp)
coin.reverse()

p = int(input())

count = 0
for c in coin:
    # print(c)
    while p >= c:
        p -= c
        count += 1
        # print(p)
print(count)
