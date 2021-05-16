n, x = map(int, input().split())
an = list(map(int, input().split()))
an = [a for a in an if a != x]

if len(an) == 0:
    print()

for i, a in enumerate(an):
    if i == len(an)-1: 
        print(a)
    else:
        print(a, end=" ")
