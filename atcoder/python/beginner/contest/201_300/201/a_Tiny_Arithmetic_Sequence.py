an = list(map(int, input().split()))
an = sorted(an)

if (an[2] - an[1]) == (an[1] - an[0]):
    print('Yes')
else:
    print('No')
