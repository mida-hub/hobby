def main():
    n, w = map(int, input().split())

    sp_dict = {}

    for i in range(n):
        s, t, p = map(int, input().split())
        if sp_dict.get(s) is not None:
            sp_dict[s] += p
        else:
            sp_dict[s] = p

        if sp_dict.get(t) is not None:
            sp_dict[t] -= p
        else:
            sp_dict[t] = -p

    is_result = False
    total = 0

    # print(sorted(sp_dict.items()))

    # simulation
    for key, value in sorted(sp_dict.items()):
        # print(value)
        total += value
        if total > w:
            is_result = True
            break
    
    if is_result:
        print('No')
    else:
        print('Yes')

main()
