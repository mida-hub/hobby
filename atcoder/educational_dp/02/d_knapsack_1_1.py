def print_graph(gh):
    for g in gh:
        print(g)

n, w = map(int, input().split())

dp = [[0] * (w+1) for i in range(n+1)]
# print_graph(dp)
# print('-'*50)
for i in range(n):
    w0, v0 = map(int, input().split())
    for j in range(w+1):
        if j - w0 >= 0:
            dp[i+1][j] = max([dp[i+1][j],
                              dp[i][j-w0] + v0])
        else:
            dp[i+1][j] = dp[i][j]

# print_graph(dp)
# print('-'*50)
print(max(max(dp)))
