def output(result):
    print(len(result), end=" ")
    for r in result:
        print(r, end=" ")
    print()

def main():
    n = int(input())
    an = list(map(int, input().split()))

    bk = [0] * 200

    cnt = min([n, 8])

    # print(an)
    # print(cnt)

    for i in range(1, 2 ** cnt):
        sig = 0
        s = []
        # フラグ作成
        for j in range(cnt):
            if ((i >> j) & 1):
                s.append(j+1)
                sig += an[j]
                sig %= 200
                # print(i, j, end=" ")
        # print()
        # print(s)
        # print(sig)
        # print(bk[sig])
        if bk[sig] != 0:
            print('Yes')
            output(bk[sig])
            output(s)
            return
        else:
            bk[sig] = s
    print('No')
main()
