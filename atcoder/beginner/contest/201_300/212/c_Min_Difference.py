def main():
    n, m = map(int, input().split())
    an = list(map(int, input().split()))
    bn = list(map(int, input().split()))

    max_mn = max([max(an), max(bn)])
    # print(max_mn)

    xn = {}
    for a in an:
        xn[a] = 'a'

    for b in bn:
        if b in xn and xn[b] == 'a':
            print(0)
            return
        xn[b] = 'b'
    
    # print(an)
    # print(bn)
    # print(xn)

    result = max_mn

    xn = sorted(xn.items(), key=lambda x:x[0])
    # print(xn)
    a = 0
    b = 0
    for x in xn:
        # print(x)
        if x[1] == 'a':
            a = x[0]
        if x[1] == 'b':
            b = x[0]
            
        if a != 0 and b != 0:
            if result > abs(a-b):
                result = abs(a-b)
    print(result)

main()
