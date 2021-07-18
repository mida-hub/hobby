def main():
    n = int(input())
    an = list(map(int, input().split()))

    cnt = [0] * 401

    an_abs = []
    for a in an:
        cnt[a+200] += 1
        an_abs.append(a+200)
    an_abs = sorted(set(an_abs))
    
    total = 0
    for a in an_abs:
        for b in an_abs:
            if a == b: continue
            if a < b: continue
            # print(a, b)
            total += (b - a) ** 2 * cnt[a] * cnt[b]
    print(total)

main()
