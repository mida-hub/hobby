def many_balls(n):
    result = ''
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            result = 'B' + result
        else:
            n -= 1
            result = 'A' + result
    print(result)
n = int(input())
many_balls(n)
