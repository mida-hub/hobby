N = int(input())

declared_list = [0] * 2 * (N + 1)
for _ in range(2 * N + 1):
    for i in range(1, 2 * (N + 1)):
        if declared_list[i] == 0:
            declared_list[i] = 1
            print(i)
            break

    t = int(input())
    if t == 0:
        break

    declared_list[t] = 1
