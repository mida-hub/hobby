def main():
    n, k = map(int, input().split())
    hn = list(map(int, input().split()))

    inf = 10 ** 10

    dp = [inf] * n
    dp[0] = 0
    dp[1] = abs(hn[1] - hn[0])

    for i in range(2, n):
        # for j in range(1, k+1):
        #     if i - j >= 0:
        #         tmp = dp[i-j] + abs(hn[i] - hn[i-j])
        #         dp[i] = min([dp[i], tmp])
        dp[i] = min([dp[j] + abs(hn[i] - hn[j]) for j in range(max(0, i-k), i)])
    print(dp[n-1])
main()
