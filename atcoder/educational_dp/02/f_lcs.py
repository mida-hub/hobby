def print_graph(gh):
    for g in gh:
        print(g)

# inf = 3000 * 3000 + 100

s = input()
t = input()

len_s = len(s)
len_t = len(t)

dp = [[0] * (len_t+1) for x in range(len_s+1)]
dp[0][0] = 0

# print_graph(dp)

for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max([dp[i-1][j], dp[i][j-1]])

# print_graph(dp)
res = ''
while len_s > 0 and len_t > 0:
    if dp[len_s][len_t] == dp[len_s-1][len_t]:
        len_s -= 1
    elif dp[len_s][len_t] == dp[len_s][len_t-1]:
        len_t -= 1
    else:
        res = s[len_s-1] + res
        # print(len_s, len_t)
        len_s -= 1
        len_t -= 1

print(res)

