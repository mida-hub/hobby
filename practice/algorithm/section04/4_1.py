
def tribo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    return tribo(n-1) + tribo(n-2) + tribo(n-3)

n = 30

memo = [-1] * n

for i in range(n):
    print(f'tribo({i}) = {tribo(i)}')
