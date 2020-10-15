n = int(input())
an = list(map(int, input().split()))

count = 0
is_divide = True

while True:
    for i in range(n):
        if an[i] % 2 == 0:
            an[i] = an[i] / 2
        else:
            is_divide = False
            break

    if not is_divide:
        break

    count += 1

print(count)
