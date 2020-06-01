def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(2, 10):
    print(f'fib({i})={fib(i)}')
