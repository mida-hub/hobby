def main():
    import numpy as np

    n = int(input())
    an = list(map(int, input().split()))
    base = np.array(an)
    base_com = []

    for i in range(n):
        base_com = np.concatenate([base_com, base[i+1:] - an[i]], 0)
    print(int(sum(base_com*base_com)))

main()
