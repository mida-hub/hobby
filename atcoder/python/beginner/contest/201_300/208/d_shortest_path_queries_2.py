def print_graph(gh):
    for g in gh:
        print(g)

def main():
    n, m = map(int, input().split())

    if m == 0:
        print(0)
        return

    inf = 10**10

    dist = [[inf] * (n+1) for i in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = c
    # print_graph(dist)
    # print('-'*50)
    ans = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                tmp = min([dist[i][j], dist[i][k] + dist[k][j]])
                dist[i][j] = tmp
                if tmp < inf:
                    ans += tmp
    # print_graph(dist)
    print(ans)

main()
