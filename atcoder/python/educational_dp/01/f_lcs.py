s = input()
t = input()

len_s = len(s)
len_t = len(t)

dp = [[0] * (len_t + 1) for x in range(len_s + 1)]
# print(dp)

dp[0][0] = 0

for i in range(0, len_s + 1):
    for j in range(0, len_t + 1):
        if i > 0 and j > 0:
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max([dp[i-1][j], dp[i][j-1]])

for j, d in enumerate(dp):
        print(d[:][:])
# print(dp[len_s][len_t])
dp_len = dp[len_s][len_t]
ans = ''

dp_len -= 1
len_s -= 1
len_t -= 1

while dp_len >= 0:
    # print(f'dp_len:{dp_len}')
    # print(f'len_s:{len_s}')
    # print(f'len_t:{len_t}')
    if s[len_s] == t[len_t]:
        ans = s[len_s] + ans
        dp_len -= 1
        len_s -= 1
        len_t -= 1
    elif dp[len_s][len_t] == dp[len_s-1][len_t]:
        len_s -= 1
    else:
        len_t -= 1
print(ans)
