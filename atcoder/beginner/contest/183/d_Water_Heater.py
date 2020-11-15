def main():
    import numpy as np
    n, w = map(int, input().split())

    plan = np.zeros(10**5 * 2)
    for i in range(n):
        s, t, p = map(int, input().split())
        plan[s-1:t-1] += p

    if any(plan > w):
        print('No')
    else:
        print('Yes')

main()
