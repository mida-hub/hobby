def main():
    n, w = map(int, input().split())
    dp = [-1] * (w + 1)
    dp[w] = 0

    for i in range(n):
        w0, v0 = map(int, input().split())
        for j in range(w0, w + 1):
            if dp[j] == -1:
                continue
            # print(j, j-w0)
            if dp[j-w0] < dp[j] + v0:
                dp[j-w0] = dp[j] + v0
            # print(dp)

    print(max(dp))
main()
