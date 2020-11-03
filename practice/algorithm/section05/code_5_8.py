S = 'logistic'
T = 'algorithm'

len_s = len(S)
len_t = len(T)

inf = 2 ** 29

dp = [[inf] * (len_t + 1) for x in range(len_s + 1)]
# print(dp)

dp[0][0] = 0

for i in range(0, len_s + 1):
    for j in range(0, len_t + 1):
        # 変更操作
        # print(S[i - 1])
        # print(T[j - 1])
        if i > 0 and j > 0:
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min([dp[i][j], dp[i - 1][j - 1]])
            else:
                dp[i][j] = min([dp[i][j], dp[i - 1][j - 1] + 1])

        # 削除操作
        if i > 0:
            dp[i][j] = min([dp[i][j], dp[i - 1][j] + 1])

        # 挿入操作
        if j > 0:
            dp[i][j] = min([dp[i][j], dp[i][j - 1] + 1])

for j, d in enumerate(dp):
        # if j == 0:
        #     continue
        # if j > i+1:
        #     break
        print(d[:][:])
    # print('-'*50)
# print(dp)
