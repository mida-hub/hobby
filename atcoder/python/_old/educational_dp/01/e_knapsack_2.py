def main():
    max_v = 100100
    inf = 10 ** 10
    n, w = map(int, input().split())
    dp = [[inf] * max_v for i in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        w0, v0 = map(int, input().split())
        for value in range(max_v):
            if value - v0 >=0:
                dp[i+1][value] = min([dp[i+1][value], dp[i][value-v0] + w0])
            
            dp[i+1][value] = min([dp[i+1][value], dp[i][value]])
    
    result = 0
    for i in range(max_v):
        if dp[n][i] <= w:
            result = i
    print(result)
main()
