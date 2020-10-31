n, k = map(int, input().split())

def quad(n, k, a, b, c, d):
    if any([a > n,
            b > n,
            c > n,
            d > n]):
        return 

    if f'{a}{b}{c}{d}' in count:
        return

    if (a + b - c - d) == k:
        count.append(f'{a}{b}{c}{d}')
        return
    
    # print(f'a={a}, b={b}, c={c}, d={d}')
    quad(n, k, a + 1, b, c, d)
    quad(n, k, a, b + 1, c, d)
    quad(n, k, a, b, c + 1, d)
    quad(n, k, a, b, c, d + 1)

    return

count = []
a, b, c, d = 1, 1, 1, 1
quad(n, k, a, b, c, d)
# print(count)
print(len(count))
