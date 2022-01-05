n = int(input())
hn = list(map(int, input().split()))

inf = 10 ** 10

dp = [inf] * n
dp[0] = 0
dp[1] = abs(hn[1] - hn[0])

for i in range(2, n):
    tmp_1 = dp[i-1] + abs(hn[i] - hn[i-1])
    tmp_2 = dp[i-2] + abs(hn[i] - hn[i-2])
    # print(tmp_1, tmp_2)
    dp[i] = min([tmp_1, tmp_2])

print(dp[n-1])
