n = int(input())
a = list(range(-n+1, 0)) + list(range(n)) + [n]
print(a)

dp = [[0] * (len(a) + 1) for i in range(n + 1)]
# print(dp)

dp[0][0] = 1

