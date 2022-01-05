n = int(input())
a = list(map(int, input().split()))
w = sum(a)

dp = [[0] * (w+1) for x in range(n+1)]

# print(n)
# print(a)

dp[0][0] = 0
for i in range(n):
    for j in range(w+1):
        if (j - a[i] >= 0):
            dp[i+1][j] = max([dp[i+1][j], 
                              dp[i][j - a[i]] + a[i]
                            ])
        dp[i+1][j] = max([dp[i+1][j], 
                            dp[i][j]
                        ])

total = []
for d in dp:
    total += d
print(len(set(total)))
