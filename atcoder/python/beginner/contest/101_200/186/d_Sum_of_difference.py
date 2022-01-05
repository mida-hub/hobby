def main():
    n = int(input())
    an = list(map(int, input().split()))
    an = sorted(an)
    sn = [0] * (n-1)
    sn[n-2] = an[n-1]

    total = 0

    for i in reversed(range(1, n-1)):
        sn[i-1] = sn[i] + an[i] 

    for i in range(n-1):
        total += sn[i] - an[i] * (n-i-1)

    print(total)

main()
