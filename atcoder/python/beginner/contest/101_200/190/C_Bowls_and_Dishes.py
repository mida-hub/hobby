def main():
    n, m = map(int, input().split())

    cond = []

    for i in range(m):
        cond.append(list(map(int, input().split())))

    # print(cond)

    k = int(input())

    put = []
    for i in range(k):
        put.append(list(map(int, input().split())))

    # print(put)

    put_list = []
    check_dict = {}

    for i in range(2 ** k):
        tmp = []
        for j in range(k):
            if ((i >> j) & 1):
                tmp.append(put[j][0])
                # print(1, end="")
            else:
                tmp.append(put[j][1])
                # print(0, end="")
        # print()
        # print(list(set(tmp)))
        put_list.append(list(set(tmp)))

    for put in put_list:
        tmp = ','.join(map(str, put))
        if tmp not in check_dict:
            check_dict[tmp] = set(put)
    
    max_result = 0
    for put in check_dict:
        result = []
        for l in range(m):
            result.append(len(set(cond[l]) & check_dict[put]) == 2)
        sum_result = sum(result)
        if sum_result > max_result:
            max_result = sum_result
    print(max_result)
main()
