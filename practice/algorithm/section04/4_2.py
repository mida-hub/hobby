
def tribo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    if memo[n] != -1:
        return memo[n]

    memo[n] = tribo(n-1) + tribo(n-2) + tribo(n-3)

    return memo[n]

n = 50

memo = [-1] * n

for i in range(n):
    print(f'tribo({i}) = {tribo(i)}')
