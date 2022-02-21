max_v = 100000 + 10
inf = 10 ** 10

n, w = map(int, input().split())

dp = [[inf] * max_v for i in range(n+1)]
dp[0][0] = 0

for i in range(n):
    w0, v0 = map(int, input().split())
    # print(w0, v0)
    for j in range(max_v):
        if j - v0 >= 0:
            dp[i+1][j] = min([dp[i+1][j],
                              dp[i][j-v0] + w0])
        
        dp[i+1][j] = min([dp[i+1][j], dp[i][j]])
    # print(dp[i+1])
    # print('-'*50)
result = 0
for i in range(max_v):
    if dp[n][i] <= w:
        result = i
print(result)
