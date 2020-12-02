def main():
    n = int(input())
    hn = []
    sn = []
    inf = 2**60
    tn = [0] * n

    for i in range(n):
        h, s = map(int, input().split())
        hn.append(h)
        sn.append(s)

    # print(n)
    # print(hn)
    # print(sn)
    # print(inf)

    left = 0
    right = inf

    while right - left > 1:
        mid = (left + right) // 2
        ok = True

        for i in range(n):
            if mid < hn[i]:
                ok = False
            else:
                tn[i] = (mid - hn[i]) / sn[i]
                # print(tn)
            
        tn = sorted(tn)
        # print('-'*20)
        # print(tn)
        # print(right)
        # print(left)

        for i in range(n):
            if tn[i] < i:
                ok = False
        
        if ok:
            right = mid
        else:
            left = mid
        
    print(right)

main()
