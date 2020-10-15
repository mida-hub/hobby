an = list(map(int, input().split()))

a_min = 10**10
a_max = -1

for a in an:
    if a < a_min:
        a_min = a
    if a > a_max:
        a_max = a
    # print(a_min, a_max)

print(a_max - a_min)
