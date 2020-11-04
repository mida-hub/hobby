n = int(input())
w = int(input())
a = list(map(int, input().split()))

dp = [[False] * (w+1) for x in range(n+1)]

print(n)
print(w)
print(a)

dp[0][0] = True
for i in range(n):
    for j in range(w+1):
        if j >= a[i]:
            dp[i+1][j] = dp[i][j-a[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]


for d in dp:
    print(d)
print(dp[n][w])
