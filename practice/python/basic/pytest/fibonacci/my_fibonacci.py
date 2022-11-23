def fibonacci(n: int):
    a = 0
    b = 1

    for _ in range(n):
        print(b)

        a, b = b, a + b
