def main():
    import itertools
    n, k = map(int, input().split())

    tn = []
    for i in range(n):
        tn.append(list(map(int, input().split())))

    result = 0
    for v in itertools.permutations(range(1, n), n - 1):
        pattern = list(v) + [0]
        # print(pattern)

        tmp = 0
        total = 0
        for i in pattern:
            # print(tn[tmp][i])
            total += tn[tmp][i]
            tmp = i

        if total == k:
            result += 1

    # print(tn)
    print(result)

main()
