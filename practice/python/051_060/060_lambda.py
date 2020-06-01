def f(x):
    y = 0 if x > 0 else 1
    return y

x = 10
print(f(x))

x = 0
print(f(x))

x = 2
lambda_a = lambda x: x * x
print(lambda_a(x))

x = 2
y = 3
lambda_b = lambda x, y, z=4: x * y * z
print(lambda_b(x, y))
print(lambda_b(x, y, 5))

x = 2
y = 3
lambda_c = lambda x, y: y if x < y else x

print(lambda_c(x, y))

x = 3
y = 2
print(lambda_c(x, y))
