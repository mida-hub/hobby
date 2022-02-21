n = int(input())
an = list(map(int, input().split()))

an = sorted(an)
is_ok = 'Yes'

i = 1
for a in an:
    if a == i:
        i+=1
    else:
        is_ok = 'No'
        break

print(is_ok)
