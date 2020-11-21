def er(s, p):
    n2 = int(p ** 0.5) + 1

    for i in range(1, n2 + 1):
        if p % i == 0:
            # print(i, p // i)
            if (p // i + i) == s:
                return True
    return False

def main():
    s, p = map(int, input().split())

    if er(s, p):
        print('Yes')
    else:
        print('No')

main()
