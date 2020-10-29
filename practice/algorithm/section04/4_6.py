def func(i, w, an):
    if i == 0:
        if w == 0: return True
        else: return False
    
    # print(i, w)
    # print(f'memo[{i}][{w}] : {memo[i][w]}')
    if memo[i][w] != -1: return memo[i][w]

    # an[i - 1] を選ばない
    if func(i - 1, w, an):
        memo[i][w] = 1
        return memo[i][w]

    # an[i - 1] を選ぶ
    if func(i - 1, w - an[i - 1], an):
        memo[i][w] = 1
        return memo[i][w]

    memo[i][w] = 0
    return memo[i][w]

n, w = map(int, input().split())
an = list(map(int, input().split()))

# print(n, w)
# print(an)

memo = [[-1] * (w + 1) for i in range(n + 1)]
# print(memo)

if func(n, w, an):
    print('Yes')
else:
    print('No')
