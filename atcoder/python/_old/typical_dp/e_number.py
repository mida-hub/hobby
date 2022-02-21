def main():
    d = int(input())
    n = input()
    MOD = 1000000007

    dp = [[[0] * d for i in range(2)] for j in range(len(n) + 1)]

    dp[0][0][0] = 1

    for i in range(len(n)):
        for j in range(d):
            for k in range(10):
                dp[i + 1][1][(j + k) % d] += dp[i][1][j]
                dp[i + 1][1][(j + k) % d] %= MOD
            
            for k in range(int(n[i])):
                dp[i + 1][1][(j + k) % d] += dp[i][0][j]
                dp[i + 1][1][(j + k) % d] %= MOD

            dp[i + 1][0][(j + int(n[i])) % d] = dp[i][0][j]

    # for i in dp:
    #     print(i)

    print(dp[len(n)][0][0] + dp[len(n)][1][0] - 1)
main()
