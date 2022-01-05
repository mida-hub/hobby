n, k = map(int, input().split())
hn = list(map(int, input().split()))

dp = [0] * n
dp[1] = abs(hn[0] - hn[1])

for i in range(2, n):
    # print(max(0, i-k), i)
    # print(min([dp[j] + abs(hn[i] - hn[j]) for j in range(max(0, i-k), i)]))
    dp[i] = min([dp[j] + abs(hn[i] - hn[j]) for j in range(max(0, i-k), i)])


print(dp[n - 1])
# print(dp)
