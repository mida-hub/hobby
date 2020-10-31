n = 6
W = 9
weight_value = ((2,3),(1,2),(3,6),(2,1),(1,3),(5,85))
print(weight_value)

dp = [[0] * (W + 1) for i in range(n + 1)]

for i in range(n):
# for i in range(3):
    for w in range(W+1):
    # for w in range(3):
        # print(f'i={i}, w={w}, weight={weight_value[i][0]}')
        if (w - weight_value[i][0] >= 0):
            dp[i+1][w] = max([dp[i+1][w], 
                              dp[i][w - weight_value[i][0]] + weight_value[i][1]
                            ])
        dp[i+1][w] = max([dp[i+1][w], 
                            dp[i][w]
                        ])
    for j, d in enumerate(dp):
        if j == 0:
            continue
        if j > i+1:
            break
        print(d[1:][:])
    print('-'*50)

print(dp[n][W])
