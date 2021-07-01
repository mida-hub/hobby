n = int(input())
hn = list(map(int, input().split()))

# print(n)
# print(hn)

dp = [0] * n

for i in range(1, n):
    if i == 1:
        dp[i] = abs(hn[i] - hn[i-1])
    else:
        dp[i] = min([dp[i-1] + abs(hn[i] - hn[i-1]),
                     dp[i-2] + abs(hn[i] - hn[i-2])])
#     print(dp)
# print(dp)
print(dp[-1])
